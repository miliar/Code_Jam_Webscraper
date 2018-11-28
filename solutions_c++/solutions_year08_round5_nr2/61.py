//some code in here may be from Abdenego's library
//at http://shygypsy.com/tools/
//(you will see a comment near the relevant code if that's
//the case!)
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#define V(type) vector< type >
#define Vall(t) t.begin(),t.end()
#define llint long long
#define forV(var, vec) for(int var=0;var<vec.size();var++)
#define for0(var, lim) for(int var=0;var<lim;var++)
#define for1(var,lim) for(int var=1;var<lim;var++)
#define btw(x,a,b) ((x) >= (a) && (x) <= (b))
#define permute(vec) next_permutation( vec.begin(),vec.end())
#define MP make_pair
#define dpExp MP(a,b)

using namespace std;

char memo[16][16][225*4 + 3][225*4 + 3];

typedef pair<int,pair<pair<int,int>,pair<int,int> > > node;
#define cst first
#define rr second.first.first
#define cc second.first.second
#define BLU second.second.first
#define ORA second.second.second

#define pr(x) (((x) >> 2) / C)
#define pc(x) (((x) >> 2) % C)
#define pp(x) ((x) % 4)

int nnid[20][20][5];
#define nid(a,b,c) nnid[a][b][c]

int dr[] = {1,-1,0,0};
int dc[] = {0,0,-1,1};

int main(void)
{
	int CASES;
	cin >> CASES;
	for(int _cn = 1;_cn <= CASES;++_cn)
	{
		memset(memo,0,sizeof(memo));
		memset(nnid,0,sizeof(nnid));
		int R,C;
		cin >> R >> C;
		int BAD = R*C*4;
		vector<string> v;v.clear();
		string s;
		for(int i=0;i<R;++i)
		{
			cin >> s;v.push_back(s);
		}
		int G_r,G_c;
		priority_queue<node> pq;while(!pq.empty()){pq.pop();}
		bool found = false;
		forV(i,v)
		{
			forV(j,v[i])
			{
				if(v[i][j] == 'O'){pq.push(MP(0,MP(MP(i,j),MP(BAD,BAD))));v[i][j] = '.';}
				if(v[i][j] == 'X'){G_r = i;G_c = j;v[i][j] = '.';}
			}
		}
		forV(i,v)
		{
			forV(j,v[i])
			{
				for0(t,4)
				{
					//find nid
					nid(i,j,t) = BAD;
					if(v[i][j] == '#'){continue;}
					//search
					int ii = i,jj = j;
					while(btw(ii,0,R-1) && btw(jj,0,C-1) && v[ii][jj] != '#'){ii += dr[t];jj += dc[t];}
					//undo one
					//if(ii == i && jj == j){continue;}
					ii -= dr[t];jj -= dc[t];
#define mk(a,b,c) ((c) + 4*((a)*C + (b)))
					nid(i,j,t) = mk(ii,jj,t);
				}
			}
		}
		int out = 0;
		while(!pq.empty())
		{
			node n = pq.top();
			pq.pop();
			//cerr << n.cst << " " << n.rr << " " << n.cc << " " << n.BLU << " " << n.ORA << endl;
			if(n.rr == G_r && n.cc == G_c){found = true;out = -n.cst;break;}
			if(memo[n.rr][n.cc][n.BLU][n.ORA]){continue;}
			memo[n.rr][n.cc][n.BLU][n.ORA] = 1;
		//	cerr << n.cst << " " << n.rr << " " << n.cc << " " << n.BLU << " " << n.ORA << endl;
			//new moves
			//current portal state
#define news(t,q,w,e,r) if(btw(q,0,R-1) && btw(w,0,C-1) && v[q][w] != '#' && !memo[q][w][e][r]){pq.push(MP(t,MP(MP(q,w),MP(e,r))));}
			if(n.BLU != BAD && pr(n.BLU) == n.rr && pc(n.BLU) == n.cc)
			{
				//go through orange
				news(n.cst - 1,pr(n.ORA),pc(n.ORA),n.BLU,n.ORA);
			}
			if(n.ORA != BAD && pr(n.ORA) == n.rr && pc(n.ORA) == n.cc)
			{
				//go through blue
				news(n.cst - 1,pr(n.BLU),pc(n.BLU),n.BLU,n.ORA);
			}
			for0(t,4)
			{
				news(n.cst-1,n.rr + dr[t],n.cc + dc[t],n.BLU,n.ORA);
			}
			//no change blu
			for0(t,4)
			{
				if(nid(n.rr,n.cc,t) != BAD)
				{
				int nb = nid(n.rr,n.cc,t);
				int no = n.ORA;
				if(nb == no){continue;}
				news(n.cst,n.rr,n.cc,nb,no);
				/*if(nb != BAD && pr(nb) == n.rr && pc(nb) == n.cc)
				{
					//go through orange
					news(n.cst - 1,pr(no),pc(no),nb,no);
				}
				if(no != BAD && pr(no) == n.rr && pc(no) == n.cc)
				{
					//go through blue
					news(n.cst - 1,pr(nb),pc(nb),nb,no);
				}
				for0(tq,4)
				{
					//move!
					news(n.cst-1,n.rr + dr[tq],n.cc + dc[tq],nb,no);
				}*/
				}
			}
			for0(t,4)
			{
				if(nid(n.rr,n.cc,t) != BAD)
				{
				int nb = n.BLU;
				int no = nid(n.rr,n.cc,t);
				if(nb == no){continue;}
				news(n.cst,n.rr,n.cc,nb,no);
				/*if(nb != BAD && pr(nb) == n.rr && pc(nb) == n.cc)
				{
					//go through orange
					news(n.cst - 1,pr(no),pc(no),nb,no);
				}
				if(no != BAD && pr(no) == n.rr && pc(no) == n.cc)

				{
					//go through blue
					news(n.cst - 1,pr(nb),pc(nb),no,no);
				}
				for0(tq,4)
				{
					//move!
					news(n.cst-1,n.rr + dr[tq],n.cc + dc[tq],nb,no);
				}*/
				}
			}
			//new portal states
#if 0
			for(int t=0;t<4;++t)
			{
				for(int ot=0;ot<4;++ot)
				{
					int nb = nid(n.rr,n.cc,t);
					int no = nid(n.rr,n.cc,ot);
					news(n.cst,n.rr,n.cc,nb,no);
					if(nb != BAD && pr(nb) == n.rr && pc(nb) == n.cc)
					{
						//go through orange
						news(n.cst - 1,pr(no),pc(no),nb,no);
					}
				if(no != BAD && pr(no) == n.rr && pc(no) == n.cc)

					{
						//go through blue
						news(n.cst - 1,pr(nb),pc(nb),no,no);
					}
					for0(tq,4)
					{
						//move!
						news(n.cst-1,n.rr + dr[tq],n.cc + dc[tq],nb,no);
					}
				}
			}
#endif
		}
		if(!found)
		{
			cout << "Case #" << _cn << ": " << "THE CAKE IS A LIE" << endl;
			cerr << "Case #" << _cn << ": " << "THE CAKE IS A LIE" << endl;
		}
		else
		{
			cout << "Case #" << _cn << ": " << out << endl;
			cerr << "Case #" << _cn << ": " << out << endl;
		}
	}
	return 0;
}

