# include <cstdio>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <map>
# include <set>
# include <algorithm>
# include <cstdlib>

using namespace std;

int T, N, val;
char letra[12];

vector<pair<int, int> > orange, blue;

int ABS(int a){
	if( a < 0 ) return -a;
	return a;
}

int main (void){
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		scanf("%d", &N);
		orange.clear();
		blue.clear();
		for(int i = 0 ; i < N; i++){
			scanf(" %s %d", letra, &val);
			if( letra[0] == 'O' ) orange.push_back(make_pair(val,i));
			else blue.push_back(make_pair(val,i));
		}
		int pos[2];
		pos[0] = pos[1] = 1;
		int p0 = 0;
		int p1 = 0;
		int sz0 = orange.size();
		int sz1 = blue.size();
		int tempo = 0;
		while(1){
			if( p0 == sz0 && p1 == sz1) break;
			else if(p0 == sz0){
				int dif = ABS(pos[1]-blue[p1].first);
				dif++;
				tempo += dif;
				pos[1] = blue[p1].first;
				p1++;
				continue;
			}
			else if(p1 == sz1){
				int dif = ABS(pos[0]-orange[p0].first);
				dif++;
				tempo += dif;
				pos[0] = orange[p0].first;
				p0++;
				continue;
			}
			if( blue[p1].second < orange[p0].second){
				int dif = ABS(pos[1]-blue[p1].first);
				dif++;
				tempo += dif;
				pos[1] = blue[p1].first;
				p1++;
				if(orange[p0].first > pos[0]){
					pos[0] = pos[0] + dif;
					if( pos[0] > orange[p0].first) pos[0] = orange[p0].first;
				}
				else{
					pos[0] = pos[0] - dif;
					if( pos[0] < orange[p0].first) pos[0] = orange[p0].first;
				}
			}
			else{
				int dif = ABS(pos[0]-orange[p0].first);
				dif++;
				tempo += dif;
				pos[0] = orange[p0].first;
				p0++;
				if(blue[p1].first > pos[1]){
					pos[1] = pos[1] + dif;
					if( pos[1] > blue[p1].first) pos[1] = blue[p1].first;
				}
				else{
					pos[1] = pos[1] - dif;
					if( pos[1] < blue[p1].first) pos[1] = blue[p1].first;
				}
			}
		}
		
				
		printf("Case #%d: %d\n", tc, tempo);
	}
	return 0;
}