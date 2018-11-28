#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn (10005)
using namespace std;

int f[maxn],l[maxn],d[maxn],D,N,test;

int main(){
	freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++){
		printf("Case #%d: ",cnt);
		scanf("%d",&N);
		for (int i=0;i<N;i++) scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&D);
		memset(f,0,sizeof(f));
		f[0]=d[0];
		for (int i=0;i<N;i++){
			for (int j=i+1;j<N;j++){
				if (d[i]+f[i]>=d[j]) f[j]=max(f[j],min(d[j]-d[i],l[j]));
			}			
		}
		bool ok=false;
		for (int i=0;i<N;i++) if (D-d[i]<=f[i]) ok=true;
		if (ok) puts("YES");
			else puts("NO");
	}
	return 0;
}
