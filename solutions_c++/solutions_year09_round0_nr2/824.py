#pragma warning(disable: 4786)
#include <vector>
#include <sstream>
#include <list>
#include <bitset>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

double Pi =acos(-1.0);
#define oo 2147483647
#define inf 1e17
#define LL __int64
#define eps 1e-8
#define sign(x) ((x)>eps?1:((x)<-eps?-1:0)) 
#define MIN(a,b) (a)<(b)?(a):(b)
#define REP(i,N) for(i=0;i<N;++i)
#define FOR(i,a,b) for(i=(a);i<=(b);++i)
int mp[100][100];
char ans[100][100];
int main()
{
	//freopen("small_in.txt","r",stdin);
	//freopen("small_out.txt","w",stdout);	
	freopen("large_in.txt","r",stdin);	
	freopen("large_out.txt","w",stdout);

	int N,cs;
	int i,j,ci,cj;
	int w,h;
	char cur,nc;
	int path[10000][2],plen,low,cl;
	cin>>N;
	FOR(cs,1,N)
	{
		cin>>h>>w;
		REP(i,h)
		{
			REP(j,w)
				cin>>mp[i][j];
		}
		memset(ans,0,sizeof(ans));
		nc='a'-1;
		REP(i,h)
		{
			REP(j,w)
			{
				if(ans[i][j]>0) continue;
				plen=1;
				path[0][0]=i;
				path[0][1]=j;
				while(true)
				{
					ci=path[plen-1][0];
					cj=path[plen-1][1];
					low=mp[ci][cj];
					cl=0;
					if(ci>0&&mp[ci-1][cj]<low)
					{
						low=mp[ci-1][cj];
						cl=1;
					}
					if(cj>0&&mp[ci][cj-1]<low)
					{
						low=mp[ci][cj-1];
						cl=2;
					}
					if(cj<w-1&&mp[ci][cj+1]<low)
					{
						low=mp[ci][cj+1];
						cl=4;
					}
					if(ci<h-1&&mp[ci+1][cj]<low)
					{
						low=mp[ci+1][cj];
						cl=3;
					}					
					if(cl>0)
					{
						path[plen][0]=ci;
						path[plen][1]=cj;
						if(cl==1)
							--path[plen][0];
						else if(cl==2)
							--path[plen][1];
						else if(cl==3)
							++path[plen][0];
						else if(cl==4)
							++path[plen][1];
						++plen;
						if(ans[path[plen-1][0]][path[plen-1][1]]>0)
							break;
					}
					else
						break;
				}
				if(ans[path[plen-1][0]][path[plen-1][1]]>0)
					cur=ans[path[plen-1][0]][path[plen-1][1]];
				else
				{
					++nc;
					cur=nc;
				}
				while(--plen>=0)
					ans[path[plen][0]][path[plen][1]]=cur;				
			}
		}
		cout<<"Case #"<<cs<<": "<<endl;
		REP(i,h)
		{
			REP(j,w)
				cout<<ans[i][j]<<" ";
			cout<<endl;
		}
		//printf("Case #%d: %I64d\n",cs,ans);
	}
	return 0;		
}
