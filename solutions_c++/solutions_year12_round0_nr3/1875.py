#include <cstdio>
#include <iostream>
#include <cstring>
const int maxn=2000012;
bool flag[maxn];
int f[]={0,1,10,100,1000,10000,100000,1000000};
inline int countx(int n){
	int ret=0;
	for(;n;n/=10,++ret);
	return ret;
}
int main(){
	//freopen("c.in","r",stdin);
	//freopen("c.out","w",stdout);
	int T,tt,res;
	int A,B;
	int i,j,k;
	scanf("%d",&T);
	for(tt=1;tt<=T;++tt){
		scanf("%d%d",&A,&B);
		res=0;
		for(i=A;i<=B;++i) flag[i]=0;
		for(i=A;i<=B;++i){
			if(!flag[i]){
			int len=countx(i);
			int c=1;
			flag[i]=1;
			for(j=i/10,k=i%10*f[len];
				j>0;
				k=k/10+j%10*f[len],j/=10)
			{
				//printf("test:%d ",j+k);
				if(j+k>=A&&j+k<=B&& !flag[j+k]) {
					//++res;
					flag[j+k]=1;
					++c;
					//printf("(%d,%d) ",i,j+k);
				}
			}
			res+=c*(c-1)/2;
			}
		}
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;
}