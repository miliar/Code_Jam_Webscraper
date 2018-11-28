#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

#include<cstdio>
#include<queue>
#include<list>
#include<stack>
#include<utility>
#include<numeric>
#include<map>
#include<cctype>
#include<cstring>
#include<sstream>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define s scanf
#define p printf

#define INF 1000000000

int main()
{
	int t;
	s("%d",&t);
	int n,m;
	int inp[105][105];
	char ch;
	bool fl;
	//int d[][2]={{-1,0},{1,0},{0,-1},{0,1}};
	int d[][2]={{1,0},{0,1},{0,-1},{-1,0}};
	int ti,tj,tmpi,tmpj;
	int minal,mini,minj;
	char fill;
	F(tc,t)
	{
		s("%d%d",&n,&m);
		F(i,n)
		{
			F(j,m)
				s("%d",&inp[i][j]);
		}
		char str[105][105]={};

		ch='a';
		F(i,n)
		{
			F(j,m)
			{
				if(str[i][j]==0)
				{
					stack< pair<int,int> > P;
					P.push(make_pair(i,j));
					fl=true;
					while(fl)
					{
						ti=P.top().first;
						tj=P.top().second;
						fl=false;
						minal=INF;
						mini=minj=-1;
						F(k,4)
						{
							tmpi=ti+d[k][0];
							tmpj=tj+d[k][1];
							if(tmpi>=0 && tmpi<n && tmpj>=0 && tmpj<m && inp[tmpi][tmpj]<=minal && inp[tmpi][tmpj]<inp[ti][tj])
							{
								fl=true;
								//minal=min(minal,inp[tmpi][tmpj]);
								if(minal>=inp[tmpi][tmpj])
								{
									minal=inp[tmpi][tmpj];
									mini=tmpi;
									minj=tmpj;
								}
							}
						}
						if(fl)
						{
							P.push(make_pair(mini,minj));
						}
					}
					if(str[P.top().first][P.top().second]==0)
					{
						fill=ch++;
					}
					else
					{
						fill=str[P.top().first][P.top().second];
					}
					while(!P.empty())
					{
						str[P.top().first][P.top().second]=fill;
						P.pop();
					}
				}
			}
		}
		p("Case #%d:\n",tc+1);
		F(i,n)
		{
			F(j,m)
			{
				if(j!=m-1)
					p("%c ",str[i][j]);
				else
					p("%c",str[i][j]);
			}
			p("\n");
		}
	}
	return 0;
}
