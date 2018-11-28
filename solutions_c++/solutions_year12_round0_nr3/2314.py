#include<cstdio>
using namespace std;
int z[10000000];
int x[1<<21];
void ppp(){
	for(int l=1,r=10,d=1;l<=1000000;l=r,r*=10,++d)
		for(int k=l,t;k<r;++k)
		if(!z[t=k])
		for(int c=0;c<d;++c){
			t=t/10+(t%10)*l;
			if(t>=l)z[t]=k;
		}
}
long long solve(){
	int A,B;
	long long ret =0;
	memset(x,0,sizeof(x));
	scanf("%d%d",&A,&B);
	for(int k=A;k<=B;++k)
		ret	+= x[z[k]]++;
	return ret;
}
int main(){
	ppp();
	int Tc;
	scanf("%d",&Tc);
	for(int tc=1;tc<=Tc;++tc)
		printf("Case #%d: %lld\n",tc,solve());
	return 0;
}
