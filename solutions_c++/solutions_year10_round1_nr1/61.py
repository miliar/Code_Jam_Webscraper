#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

char tab[51][51];

int dx[] = {0,0,1,-1,1,1,-1,-1};
int dy[] = {1,-1,0,0,-1,1,1,-1};

typedef pair<int, int> pii;

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		int n, k;
		scanf("%d%d", &n, &k);
		for(int i = 0; i < n; i++){
			scanf("%s", tab[i]);
			vector<char> mean;
			for(int j = 0; j < n; j++) if(tab[i][j]!='.') mean.push_back(tab[i][j]);
			const int s = (int)mean.size();
			for(int j = 0; j < n-s; j++) tab[i][j] = '.';
			int next = 0;
			for(int j = n-s; j < n; j++) tab[i][j] = mean[next++];  
		}
		
		bool R = false, B = false;
		vector<pii> start;
		for(int i = 0; i < n; i++){
			start.push_back(pii(0,i));
			start.push_back(pii(n-1,i));
			start.push_back(pii(i,0));
			start.push_back(pii(i,n-1));
		}
		for(int dir = 0; dir < 8; dir++){
			for(int s = 0; s < (int)start.size(); s++){
				int aa = start[s].first;
				int bb = start[s].second;
				int len = 1;
				char prev = tab[aa][bb];
				while(1){
					aa += dx[dir];
					bb += dy[dir];
					if( aa < 0 || bb < 0 || aa>= n || bb >= n){  break; }
					
					if( tab[aa][bb] != '.' && tab[aa][bb] == prev) len++;
					else len = 1;
					
					if(len >= k && tab[aa][bb] == 'R') R = true;
					if(len >= k && tab[aa][bb] == 'B') B = true;
					prev = tab[aa][bb]; 
				}
			}
		}
		
		if(R && B) printf("Case #%d: Both\n", cnt);
		else if(R && !B) printf("Case #%d: Red\n", cnt);
		else if(!R && B) printf("Case #%d: Blue\n", cnt);
		else if(!R && !B) printf("Case #%d: Neither\n", cnt);
	}
	return 0;
}
