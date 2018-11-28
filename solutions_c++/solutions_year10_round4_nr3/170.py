#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int n;
int t[110][110];
typedef pair<int,int> ii;
vector<ii> u[2];

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		scanf("%d", &n);
		memset(t, 0, sizeof(t));
		for(int i=0; i<n; ++i){
			int a, b, c, d;
			scanf("%d%d%d%d", &a, &b, &c, &d);
			for(int i=a; i<=c; ++i)
				for(int j=b; j<=d; ++j)
					t[i][j] = 1;
		}
		u[0].clear();
		int kt = 0;
		for(int i=1; i<=100; ++i) for(int j=1; j<=100; ++j) if(t[i][j] != 0) u[0].push_back(ii(i,j));
		int res = 0;
		while(!u[kt].empty()){
			res++;
			int k = 1-kt;
			u[k].clear();
			for(int i=0; i<u[kt].size(); ++i){
				ii p = u[kt][i];
				int x = p.first, y = p.second;
				if(t[x][y+1] != res){ if(t[x-1][y+1] == res) u[k].push_back(ii(x,y+1)); }
			}
			for(int i=0; i<u[kt].size(); ++i){
				ii p = u[kt][i];
				int x = p.first, y = p.second;
				if(t[x-1][y] == res || t[x][y-1] == res) u[k].push_back(ii(x,y));
			}
			for(int i=0; i<u[k].size(); ++i) t[u[k][i].first][u[k][i].second] = res+1;
			kt = k;
		}
		printf("Case #%d: %d\n", iii, res);
	}
	return 0;
}
