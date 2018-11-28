#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

const int maxp = 1000000 + 1;
int prime[maxp],np;
bool isp[maxp];
void getprime(){
	fill(isp,isp+maxp,true);
	isp[0] = isp[1] = false;
	int i,j;
	np = 0;
	for(i=2;i<maxp;i++){
		if(isp[i])
			prime[np++] = i;
		for(j=0;j<np&&i<=maxp/prime[j];j++){
			isp[i * prime[j]] = false;
			if(i%prime[j]==0)break;
		}
	}
}

typedef long long LL;
int pmod(int a,int b,int c){
	int res = 1;
	for(;b;b>>=1,a = (LL)a*a%c){
		if(b&1)
			res = (LL)res * a %c;
	}
	return res;
}


int D,K;
int seq[10+10];

int main(){
	getprime();
	int tc,tt,maxt;
	cin>>tc;
	for(tt=1;tt<=tc;tt++){
		printf("Case #%d: ",tt);
		scanf("%d%d",&D,&K);
		int base = 1,i,j;
		while(D--)base *= 10;
		for(i=0;i<K;i++)scanf("%d",&seq[i]);
		maxt = seq[0];
		for(i=1;i<K;i++)maxt = max(maxt,seq[i]);
		if(K<2)printf("I don't know.\n");
		else
		if(K==2){
			if(seq[0]==seq[1])printf("%d\n",seq[0]);
			else
				printf("I don't know.\n");
		}else{
			int res = -1;
			i = 0;
			while(i<np&&prime[i]<=maxt)i++;
			for(;i<np&&prime[i]<base;i++){
				int inv = (seq[1] - seq[0])%prime[i],A,B,temp;
				//cout<<prime[i]<<endl;
				if(inv==0)A = 0;
				else{
					if(inv<0)inv += prime[i];
					inv = pmod(inv,prime[i] - 2,prime[i]);
				}
				A = (LL)(seq[2] - seq[1])*inv%prime[i];
				if(A<0)A += prime[i];
				B = ((LL)seq[1] - (LL)seq[0] * A)%prime[i];
				if(B<0)B += prime[i];
				temp = seq[2];
				for(j=3;j<K;j++){
					temp = ((LL)temp * A + B)%prime[i];
					if(temp!=seq[j])break;
				}
				if(j<K)continue;
				temp = ((LL)seq[K - 1] * A + B)%prime[i];
				if(res<0||temp==res)res = temp;
				else{
					//cout<<temp<<' '<<res<<endl;
					res = -1;
					break;
				}
			}
			if(res<0)printf("I don't know.\n");
			else
				printf("%d\n",res);
		}
	}
	return 0;
}
