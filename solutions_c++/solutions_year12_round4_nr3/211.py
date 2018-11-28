#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int T;
int N;
int s[2000];
int h[2000];

vector<int> child[2000];

void solve(int p, int v, int r)
{
	//r: ŒX‚«
	h[p] = v;
	for(int i=0;i<child[p].size();i++){
		++r;
		solve(child[p][i], v - r * (p - child[p][i]), r);
	}
}

int main()
{
	scanf("%d", &T);
	for(int t=0;t++<T;){
		scanf("%d", &N);
		for(int i=0;i<N-1;i++){
			scanf("%d", s+i);
			s[i]--;
			h[i] = 0;
		}
		for(int i=0;i<N;i++) child[i].clear();

		/*
		h[N-1] = 1<<28;
		
		bool flg = false;
		for(int i=N-2;i>=0;i--){
			double low = h[i+1] - (1 << (2*N+2 - 2*i)), high = 1<<28;

			int k = s[i];
			for(int j=i+1;j<N;j++){
				if(k==j) continue;
				if(k > j){
					low = max(low, ((k-i)*h[j]-(j-i)*h[k])/(double)(k-j));
				}else{
					high = min(high, ((k-i)*h[j]-(j-i)*h[k])/(double)(k-j));
				}
			}

			//printf("%.f %.f\n", low, high);
			if(low > high){
				flg = true;
				break;
			}
			h[i] = (int)(low + high) / 2;
			//printf("%d %d\n", i, h[i]);
		}
		*/

		bool flg = false;
		for(int i=0;i<N-1;i++){
			for(int j=i+1;j<N-1;j++){
				if(j < s[i] && s[i] < s[j]){
					flg = true;
				}
			}
		}

		printf("Case #%d:", t);
		if(flg){
			puts(" Impossible");
			continue;
		}

		for(int i=0;i<N-1;i++){
			child[s[i]].push_back(i);
		}
		solve(N-1, 1000000000, 1);
		for(int i=0;i<N;i++) printf(" %d", h[i]);
		puts("");
	}

	return 0;
}
