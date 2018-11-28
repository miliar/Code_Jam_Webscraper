
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int tbl[20][20];
int dist_wall[20][20];
#define CONS make_pair
int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		int h,w;
		cin >> h >> w;
		vector<string> field;
		field.push_back(string(w+2, '#'));
		for(int y=0; y<h; y++){
			string s;
			cin >> s;
			s = string(1,'#') + s + "#";
			field.push_back(s);
		}
		field.push_back(string(w+2, '#'));
		h += 2;
		w += 2;
		int sx,sy,gx,gy;
		for(int y=0; y<h; y++)
			for(int x=0; x<w; x++)
				if(field[y][x] == 'O'){
					sx = x; sy = y;
					field[y][x] = '.';
				}else if(field[y][x] == 'X'){
					gx = x; gy = y;
					field[y][x] = '.';
				}
		for(int y=0; y<h; y++){
			for(int x=0; x<w; x++){
				pair<int,int> p = CONS(x,y);
				vector<pair<int,int> > curs, nexts;
				vector<vector<bool> > memo(h, vector<bool>(w, false));
				curs.push_back(p);
				int score = 0;
				bool ok = false;
				while(true){
					for(int i=0; i<curs.size(); i++){
						if(field[curs[i].second][curs[i].first] == '#'){
							ok = true;
							break;
						}
						for(int dir=0; dir<4; dir++)
							nexts.push_back(CONS(curs[i].first +dx[dir],
																	 curs[i].second+dy[dir]));
					}
					if(ok) break;
					curs.swap(nexts);
					nexts.clear();
					score++;
				}
				dist_wall[y][x] = score;
			}
		}
		memset(tbl, 0x1f, sizeof(tbl));
		priority_queue<pair<int,pair<int,int> > >q;
		q.push(CONS(0, CONS(sx,sy)));
		bool ok = false;
		int ans = 0;
		while(q.size()){
			int score = -q.top().first;
			int cx    =  q.top().second.first;
			int cy    =  q.top().second.second;
			q.pop();
			if(field[cy][cx] == '#') continue;
			if(score >= tbl[cy][cx]) continue;
			tbl[cy][cx] = score;
			if(cx == gx && cy == gy){
				ok = true;
				ans = score;
				break;
			}
			for(int dir=0; dir<4; dir++){
				int nx = cx + dx[dir];
				int ny = cy + dy[dir];
				if(field[ny][nx] != '#')
					q.push(CONS(-(score+1), CONS(nx, ny)));
			}
			
			for(int dir=0; dir<4; dir++){
				int tx = cx, ty = cy;
				int nx, ny;
				while(true){
					nx = tx + dx[dir];
					ny = ty + dy[dir];
					if(field[ny][nx] == '#') break;
					tx = nx;
					ty = ny;
				}
				q.push(CONS(-(score+dist_wall[cy][cx]), CONS(tx,ty)));
			}
		}
		
		cout << "Case #"<<case_no<<": ";
		if(ok){
			cout << ans;
		}else{
			cout << "THE CAKE IS A LIE";
		}
		cout << endl;
	}
	return 0;
}
