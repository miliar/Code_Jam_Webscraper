#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
typedef long long llong;
const int Max=1024;
llong G[Max*2],sum[Max],val[Max];
int vst[Max];
llong R,K,N;
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int TT;
	scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		scanf("%lld %lld %lld",&R,&K,&N);
		for(int i=0;i<N;++i){
		    scanf("%lld",G+i);
		    G[i+N]=G[i];
		}
		sum[0]=0;
		for(int i=0;i<=N*2;++i)
		    sum[i+1]=sum[i]+G[i];
		memset(vst,-1,sizeof(vst));
		int curr=0,Ta=0,Tb=0;
		val[0]=0;
		for(int i=1;true;++i){
			if(vst[curr]!=-1){
				Ta=vst[curr]-1;
				Tb=i-vst[curr];
				break;
			}
			else{
				vst[curr]=i;
				int pos=upper_bound(sum+curr,sum+(curr+N+1),sum[curr]+K)-sum;
				--pos;
				val[i]=val[i-1]+(sum[pos]-sum[curr]);
				curr=pos%N;
			}
		}
		llong res=0;
		if(R<=Ta) res=val[R];
		else{
			R-=Ta;
			res=val[Ta]+(val[Ta+Tb]-val[Ta])*(R/Tb);
			R%=Tb;
			res+=(val[Ta+R]-val[Ta]);
		}
		printf("Case #%d: %lld\n",cas,res);
	}
	return 0;
}

