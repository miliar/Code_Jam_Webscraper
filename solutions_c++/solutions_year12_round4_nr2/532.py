#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxn	=	1005;

int n,W,L,r[maxn],id[maxn],px[maxn],py[maxn];

inline long long sqr(long long x)
{
	return x*x;
}

inline bool cmpR(const int &i,const int &j)
{
	return r[i]>r[j];
}

int main()
{
	freopen("B_small.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test){
		scanf("%d%d%d",&n,&W,&L);
		for (int i=0;i<n;++i){
			scanf("%d",&r[i]);
			id[i]=i;
		}
		sort(id,id+n,cmpR);
		while (1){
			bool flg=true;
			for (int i=0;i<n && flg;++i){
				int type=rand()&1,x=0,y=0;
				if (type==0){
					for (int j=0;j<i;++j){
						x=max(x,px[id[j]]+r[id[j]]+r[id[i]]);
					}
					for (int j=0;j<i;++j)
					if (abs(x-px[id[j]])<r[id[i]]+r[id[j]]){
						y=max(y,py[id[j]]+r[id[j]]+r[id[i]]);
					}
					if (x>W || y>L) flg=false;
				}else{
					for (int j=0;j<i;++j){
						y=max(y,py[id[j]]+r[id[j]]+r[id[i]]);
						
					}
					for (int j=0;j<i;++j)
					if (abs(y-py[id[j]])<r[id[i]]+r[id[j]]){
						x=max(x,px[id[j]]+r[id[j]]+r[id[i]]);
					}
					if (x>W || y>L) flg=false;
				}
				px[id[i]]=x;
				py[id[i]]=y;
				
			}
			if (flg) break;
			random_shuffle(id,id+n);
		}
		
		printf("Case #%d:",test);
		for (int i=0;i<n;++i)
			printf(" %d %d",px[i],py[i]);
		for (int i=0;i<n;++i)
			for (int j=i+1;j<n;++j)
			if (sqr(px[i]-px[j])+sqr(py[i]-py[j])<sqr(r[i]+r[j])){
				puts("WA!~!!!");
				return 0;
			}
		puts("");
	}
	return 0;
}
