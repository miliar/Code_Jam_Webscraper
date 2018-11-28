#include<set>
#include<iostream>
using namespace std;

int R, C;
char grid[16][16];

int dir[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
bool valid(int r, int c){
	return r >= 0 && r < R && c >= 0 && c < C;
}

struct state{
	int r,c, br,bc,bd,yr,yc,yd,s;
	bool operator<(const state& st)const{
		return s < st.s;
	}
};

multiset<state> pq;
int table[15][15][15][15][5][15][15][5];

void add(state& st){
	
	if(table[st.r][st.c][st.br][st.bc][st.bd][st.yr][st.yc][st.yd] == -1 || 
	st.s < table[st.r][st.c][st.br][st.bc][st.bd][st.yr][st.yc][st.yd]){
			pq.insert(st);
			table[st.r][st.c][st.br][st.bc][st.bd][st.yr][st.yc][st.yd] = st.s;
	}
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cin >> R >> C;
		int r, c, sr, sc, tr, tc;
		
		for(r = 0 ; r < R ; r++)
			for(c = 0 ; c < C ; c++){
				cin >> grid[r][c];
				if(grid[r][c] == 'O'){
					sr = r;
					sc = c;
					grid[r][c] = '.';
				}
				if(grid[r][c] == 'X'){
					tr = r;
					tc = c;
					grid[r][c] = '.';
				}
			}
		
		//
		//memset(table, -1, sizeof table);
		for(int a1 = 0 ; a1 < R ; a1++)
			for(int a2 = 0 ; a2 < C ; a2++)
				for(int a3 = 0 ; a3 < R ; a3++)
					for(int a4 = 0 ; a4 < C ; a4++)
						for(int a5 = 0 ; a5 <= 4 ; a5++)
							for(int a6 = 0 ; a6 < R ; a6++)
								for(int a7 = 0 ; a7 < C ; a7++)
									for(int a8 = 0 ; a8 <= 4 ; a8++)
										table[a1][a2][a3][a4][a5][a6][a7][a8] = -1;
									
		pq.clear();
		
		state start = {sr, sc, 0, 0, 4, 0, 0, 4, 0};
		pq.insert(start);
		table[sr][sc][0][0][4][0][0][4] = 0;
		
		bool sol = false;
		while(!pq.empty()){
			state current = *pq.begin(); 
			
		//	cout << current.r << " " <<current.c << " " << current.br << " " << current.bc << " " << current.bd << " " << current.yr << " " << current.yc << " " << current.yd << " " << current.s << endl;
			 
			pq.erase(pq.begin());
			if(current.r == tr && current.c == tc){
				cout << "Case #" << t+1 << ": " << current.s << endl;
				sol = true;
				break;
			}
			  
			int i;
			//move
			for(i = 0 ; i < 4 ; i++){
				
				//blue portal
				if(current.r == current.br && current.c == current.bc && i == current.bd && current.yd != 4){
					state ns = {current.yr, current.yc, current.br, current.bc, current.bd, current.yr, current.yc, current.yd, current.s+1};
					add(ns);
				}
				//yellow portal
				if(current.r == current.yr && current.c == current.yc && i == current.yd && current.bd != 4){
					state ns = {current.br, current.bc, current.br, current.bc, current.bd, current.yr, current.yc, current.yd, current.s+1};
					add(ns);
				}
				
				//move
				int nr = current.r + dir[i][0];
				int nc = current.c + dir[i][1];
				
				if(valid(nr,nc) && grid[nr][nc] != '#'){
					state ns = {nr, nc, current.br, current.bc, current.bd, current.yr, current.yc, current.yd, current.s+1};
					add(ns);				
				}
				
				//shoot
				int sr = current.r, sc = current.c;
				while(true){
					int srr = sr+dir[i][0];
					int scc = sc+dir[i][1];
					if(!valid(srr,scc) || grid[srr][scc] == '#'){
						
						//shoot blue
						if(sr != current.yr || sc != current.yc || i != current.yd){
							state b = {current.r, current.c, sr, sc, i, current.yr, current.yc, current.yd, current.s};
							add(b);
						}
						
						//shoot yello
						if(sr != current.br || sc != current.bc || i != current.bd){
							state y = {current.r, current.c, current.br, current.bc, current.bd, sr, sc, i, current.s};
							add(y);
						}			
						
						break;			
					}else{
						sr = srr;
						sc = scc;
					}
				}
			}
		}
		
		if(!sol)
			cout << "Case #" << t+1 << ": THE CAKE IS A LIE" << endl;
		
	}

	return 0;	
}
