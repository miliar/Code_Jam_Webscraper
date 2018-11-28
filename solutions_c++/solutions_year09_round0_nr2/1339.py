//Grzegorz Prusak: problem "Watersheds" (Google code jam 2009)
#include <iostream>

//debug mode
#define DEBUG_MODE 1
#define DEBUG(i) if((1<<i)&DEBUG_MODE)

//loops
#define REP(i,n)    for(int i=0 ; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

const int t_max = 100	+10;
const int w_max = 100	+10;
const int h_max = 100	+10;

const int cells = w_max*h_max;
const int inf = 1000000;

class Union
{
	public:
		void clear(){ REP(i,cells) parent[i] = i; }
		int operator[](int a){ return root(a); }
		void join(int a, int b){ parent[root(a)] = parent[root(b)]; }
	
	private:
		int root(int a){ if(parent[a]==a) return a; return parent[a] = root(parent[a]); }
		int parent[cells];
};

inline int index(int x, int y){ return y*w_max+x; }

Union u;

int (*map)[h_max] = new int[w_max][h_max]+1;

char letter[cells];

int main()
{
	int t; std::cin >> t;
	REP(i,t)
	{
		//input
		int w,h; std::cin >> h >> w;
		REP(y,h) REP(x,w) std::cin >> map[x][y];
		
		//guards
		REP(x,w){ map[x][-1] = map[x][h] = inf; }
		REP(y,h){ map[-1][y] = map[w][y] = inf; }
		
		//find union
		u.clear(); REP(x,w) REP(y,h)
		{
			int v = map[x][y-1], id = index(x,y-1), nv;
			nv = map[x-1][y]; if(nv<v){ v = nv; id = index(x-1,y); } 
			nv = map[x+1][y]; if(nv<v){ v = nv; id = index(x+1,y); }
			nv = map[x][y+1]; if(nv<v){ v = nv; id = index(x,y+1); }
			if(v<map[x][y]) u.join(index(x,y),id);
		}
		
		//assign letters
		REP(j,cells) letter[j] = 0; char nl = 'a';
		REP(y,h) REP(x,w){ int r = u[index(x,y)]; if(!letter[r]) letter[r] = nl++; }
		
		//output
		std::cout << "Case #" << i+1 << ":\n";
		REP(y,h){ REP(x,w){ std::cout << letter[u[index(x,y)]]; if(x!=w-1) std::cout << " "; } std::cout << "\n"; }
	}
	return 0;
}

