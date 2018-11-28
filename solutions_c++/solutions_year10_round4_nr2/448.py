#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

__int64 t,p;
__int64 two[30];
__int64 s[2048][30];
__int64 z[2048];
__int64 c[2048];

void ask1(__int64 pos){
	if(pos*2+1<two[p+1]){
		ask1(pos*2);
		ask1(pos*2+1);
	}else{
		z[pos]=c[pos];
		__int64 i;
		for(i=29;i>=z[pos];i--)
			s[pos][i]=0;
		return;
	}
	__int64 i,q=z[2*pos]>z[2*pos+1]?z[2*pos]:z[2*pos+1];
	if(s[pos][q]>s[2*pos][q]+s[2*pos+1][q])
		s[pos][q]=s[2*pos][q]+s[2*pos+1][q];
	for(i=28;i>=0;i--){
		if(s[pos][i]>s[2*pos][i+1]+s[2*pos+1][i+1]+c[pos])
			s[pos][i]=s[2*pos][i+1]+s[2*pos+1][i+1]+c[pos];
		if(s[pos][i]>s[2*pos][i]+s[2*pos+1][i])
			s[pos][i]=s[2*pos][i]+s[2*pos+1][i];
	}
	z[pos]=q-1>0?q-1:0;
}

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	__int64 h,i,j,k;
	two[0]=1;
	for(i=1;i<30;i++)two[i]=two[i-1]*2;
	scanf("%I64d",&t);
	for(h=1;h<=t;h++){
		for(i=0;i<2048;i++)
			for(j=0;j<12;j++){
				s[i][j]=2000000000;
				s[i][j]*=10000;
			}

		scanf("%I64d",&p);
		for(j=0;j<two[p];j++){
			scanf("%I64d",&c[two[p]+j]);
			c[two[p]+j]=p-c[two[p]+j];
		}
		for(j=p-1;j>=0;j--)
			for(i=0;i<two[j];i++)
				scanf("%I64d",&c[two[j]+i]);
		ask1(1);
		printf("Case #%I64d: %I64d\n",h,s[1][0]);
	}
	return 0;
}