#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <cctype>
#include <deque>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

const int inf=100000000;

int n,m;

string a[100];

struct pos
{
	int x,y;
	int p1x,p1y,p1d;
	int p2x,p2y,p2d;
	pos(){}
	pos(int x,int y,int p1x,int p1y,int p1d,int p2x,int p2y,int p2d)
		:x(x),y(y),p1x(p1x),p2x(p2x),p1y(p1y),p2y(p2y),p1d(p1d),p2d(p2d)
	{}
	bool bad()
	{
		return p1x==19 || p2x==19;
	}
	int hash()
	{
		return ((((((x*20+y)*20+p1x)*20+p1y)*20+p2x)*20+p2y)*5+p1d)*5+p2d;
	}
	friend bool operator<(pos p1,pos p2)
	{
		return p1.hash()<p2.hash();
	}
};

map<pos,int> M;

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

bool good(int x,int y)
{
	return x>=0 && x<n && y>=0 && y<m;
}

int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++)
	{
		M.clear();
		printf("Case #%d: ",ic+1);
		cin >> n >> m;
		int sx,sy,fx,fy;
		a[0]=string(m+2,'#');
		a[n+1]=a[0];
		for(int i=1;i<=n;i++)
		{
			cin >> a[i];
			a[i]="#"+a[i]+"#";
			for(int j=0;j<m+2;j++){
				if(a[i][j]=='O')
					sx=i,sy=j;
				if(a[i][j]=='X')
					fx=i,fy=j;
			}
		}
		n+=2;
		m+=2;
		int res=inf;
		deque<pos> q;
		pos sp(sx,sy,19,19,0,19,19,0);
		q.push_back(sp);
		M[sp]=0;
		while(!q.empty())
		{
			pos cur=q.front();			
			q.pop_front();
			int cd=M[cur];
			if(cur.x==fx && cur.y==fy)
			{
				res=min(res,cd);				
				break;
			}
			for(int dir=0;dir<4;dir++)
			{
				int x=cur.x,y=cur.y;
				while(good(x,y) && a[x][y]!='#')
					x+=dx[dir],y+=dy[dir];
				pos p;
				p=cur;
				p.p1x=x;
				p.p1y=y;
				p.p1d=dir;
				if(!M.count(p))
				{
					M[p]=cd;
					q.push_front(p);
				}
				p=cur;
				p.p2x=x;
				p.p2y=y;
				p.p2d=dir;
				if(!M.count(p))
				{
					M[p]=cd;
					q.push_front(p);
				}
			}
			for(int dir=0;dir<4;dir++)
			{
				int x=cur.x,y=cur.y;
				x+=dx[dir],y+=dy[dir];
				if(!good(x,y)) continue;
				if(a[x][y]!='#')
				{
					pos p=cur;
					p.x=x;
					p.y=y;
					if(!M.count(p))
					{
						M[p]=cd+1;
						q.push_back(p);
					}
				}
				else
				{
					if(cur.bad()) continue;
					if(x==cur.p1x && y==cur.p1y && dir==cur.p1d)
					{
						x=cur.p2x;
						y=cur.p2y;
						x-=dx[cur.p2d];
						y-=dy[cur.p2d];
						pos p;
						p=cur;
						p.x=x;
						p.y=y;
						if(!M.count(p))
						{
							M[p]=cd+1;
							q.push_back(p);
						}
					}
					else
					{
						if(x==cur.p2x && y==cur.p2y && dir==cur.p2d)
						{
							x=cur.p1x;
							y=cur.p1y;
							x-=dx[cur.p1d];
							y-=dy[cur.p1d];
							pos p;
							p=cur;
							p.x=x;
							p.y=y;
							if(!M.count(p))
							{
								M[p]=cd+1;
								q.push_back(p);
							}
						}
					}
				}
			}
		}
		if(res>=inf/2)
		{
			cout << "THE CAKE IS A LIE\n";
		}
		else
			cout << res << "\n";
	}
	return 0;
}
