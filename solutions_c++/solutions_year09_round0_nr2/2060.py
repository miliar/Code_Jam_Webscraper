#include <iostream>
#include <map>
using namespace std;

#define MAX 100*100+100

struct set{
	int p[MAX],rank[MAX], number[MAX];
	int size, sets;
 
	void init(int s){
		size = sets = s; // cada elemento é um conjunto
		for (int i = 0; i < size; i++) 
			{p[i]=i; rank[i]=0; number[i]=1;}
	}
 
	void link(int x, int y) {
		if(x == y) return; //andre.sp fix: ja tao ligados nao queremos contar o comprimento 2 vezes
		if (rank[x] <= rank[y]) {
		    p[x] = y;
                    --sets; //pedro.silva: se unimos dois conjuntos temos menos um
		    number[y] += number[x];
		    if (rank[x] == rank[y])
		      rank[y]++;
		} else link(y, x);
	}
 
	int find_set(int x) {
	  if (x != p[x]) p[x] = find_set(p[x]);
	  return p[x];
	}
	int find_length(int x) {
	  return number[ find_set(p[x]) ];
	}
	void union_set(int x,int y) {
	  link(find_set(x), find_set(y));
	}
};

set s;
int m[110][110];
int T, H, W;
int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

bool 
inside(int i, int j) {
	return i >= 0 && i < H && j >= 0 && j < W;
}

int 
main()
{
	cin >> T;
	
	for (int c = 1; c <= T; c++) {
		cin >> H >> W;
		s.init(H*W+100);
		
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				cin >> m[i][j];
			}
		}
		
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				int neigh = -1;
				int nHeigh = 10001;
				
				for (int k = 0; k < 4; k++) {
					int newI = i + di[k];
					int newJ = j + dj[k];
					
					if (! inside(newI, newJ)) continue;
					
					if (m[newI][newJ] < m[i][j] && m[newI][newJ] < nHeigh) {
						nHeigh = m[newI][newJ];
						neigh = k;
						//cout << "drain: " << i << " " << j << " " << newI << " " << newJ << endl;
						
					}
				}
				
				if (neigh != -1) {
					s.union_set(i*W + j, (i+di[neigh])*W + (j+dj[neigh]));
					//cout << "drain: " << m[i][j] << " to " << m[i+di[neigh]][j+dj[neigh]]<< endl;
					//cout << s.find_set(i*100 + j)  << " " << s.find_set((i+di[neigh])*100 + j+dj[neigh]) << endl;
				}
			}
		}
		
		map<int, char> mapa;
		char car = 'a';
		
		printf("Case #%d:\n", c);
		
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				int s_ = s.find_set(i*W + j);
				
				if (j != 0) cout << " ";

				if (mapa.find(s_) != mapa.end()) {
					cout <<  mapa[s_];
				} else {
					mapa[s_] = car;
					cout << car++;
				}
			}
			cout << endl;
		}
	}
	return 0;
}
