#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		int n,m;
		scanf("%d %d\n",&n,&m);
		vector<int> a(m);
		for(int i=0; i<m; i++)
			a[i]=i;
		vector<int> b(m);
		for(int i=0; i<m; i++)
			scanf("%d ",&b[i]);
		int ans = 10000;
		do{
			int cnt = 0;
			vector<int> c(n+1);
			for(int i=1; i<=n; i++)
				c[i]=1;
			for(int i=0; i<m; i++){
				int now = b[a[i]];
				c[now]=0;
				now--;
				while(now>=1 && c[now]==1){
					cnt++;
					now--;
				}
				now=b[a[i]];
				now++;
				while(now<=n && c[now]==1){
					cnt++;
					now++;
				}
			}
			if(cnt<ans)
				ans=cnt;
		}while(next_permutation(a.begin(),a.end()));
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}