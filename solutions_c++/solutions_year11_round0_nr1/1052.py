#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstdlib>
using namespace std;

int main(){
	int T;
	int N;
	int p;
	char s[5];
	
	scanf("%d",&T);
	for (int k=1; k <= T; ++k){
		scanf("%d",&N);
		vector< pair<int,int> > M[2];
		for (int i=0; i < N; ++i){
			scanf("%s %d",s,&p);
			p--;
			M[(s[0]=='O')? 0:1].push_back(make_pair(i,p));
		}
		int x,y;
		x = y = 0;
		int pos[2] = {0};
		int t[2] = {0,0};
		for (int i=0; (x < M[0].size() && y < M[1].size()) && i < N; ++i){
			if (pos[0] != M[0][x].second){
				t[0] += abs(M[0][x].second - pos[0]);
				pos[0] = M[0][x].second;
			}
			if (pos[1] != M[1][y].second){
				t[1] += abs(M[1][y].second - pos[1]);
				pos[1] = M[1][y].second;
			}
			if (x < M[0].size() && M[0][x].first < M[1][y].first){
				t[0]++;
				x++;
				if (t[0] > t[1]){ t[1] = t[0]; }
			}
			else  {
				t[1]++;
				y++;
				if (t[1] > t[0]){ t[0] = t[1]; }
			}
		}
		if (x < M[0].size()){
			for (int i=x; i < M[0].size(); ++i){
				t[0] += abs(M[0][i].second - pos[0]);
				pos[0] = M[0][i].second;
				t[0]++;
			}
		}
		else if (y < M[1].size()){
			for (int i=y; i < M[1].size(); ++i){
				t[1] += abs(M[1][i].second - pos[1]);
				pos[1] = M[1][i].second;
				t[1]++;
			}
		}
		printf("Case #%d: %d\n",k,max(t[0],t[1]));
	}

	return 0;
}