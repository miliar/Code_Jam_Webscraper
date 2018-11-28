#include <cstdio>
#include <queue>
#include <stack>
#include <map>
#include <vector>

using namespace std;

	int a[501], x[501], y[501];
	bool b[50000001];
	
int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int t, n;
	scanf("%d", &t); int cnt=0;
	while (t--){ int sum=-1;
		memset(b, 0, sizeof(b));
		scanf("%d", &n);
		for (int i=0; i<n; i++)
			scanf("%d", &a[i]);
		
		b[0]=true;
		vector<int> v[501]; v[0].push_back(0);
		
		for (int i=0; i<n && sum<0; i++){
			int sz=v[i].size();
			for (int j=0; j<sz; j++){
				v[i+1].push_back(v[i][j]);
				if (b[v[i][j]+a[i]]){ sum=v[i][j]+a[i]; break;}
				v[i+1].push_back(v[i][j]+a[i]); b[v[i][j]+a[i]]=true;
			}
		}
		
		printf("Case #%d:\n", ++cnt);
		if (sum<0) puts("IMPOSSIBLE"); else{
			int res=sum, cx=0, cy=0;
			while (res>0){
				for (int i=0; i<n; i++)
					if (res>=a[i] && a[i]>0 && b[res-a[i]]){
						x[cx++]=a[i];
						b[res]=false; res-=a[i]; a[i]=-1; break;
					}
			}

			res=sum;
			while (res>0){
				for (int i=0; i<n; i++)
					if (res>=a[i] && a[i]>0 && b[res-a[i]]){
						y[cy++]=a[i];
						b[res]=false; res-=a[i]; a[i]=-1; break;
					}
			}
			
			for (int i=0; i<cx-1; i++)
				printf("%d ", x[i]); printf("%d\n", x[cx-1]);
			
			for (int i=0; i<cy-1; i++)
				printf("%d ", y[i]); printf("%d\n", y[cy-1]);
		}
	}
	return 0;
}
