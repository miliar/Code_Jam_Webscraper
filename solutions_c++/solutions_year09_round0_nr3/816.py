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
int cnum[500][50];
char wel[]="welcome to code jam";
char line[510];
int main()
{
	//freopen("small_in.txt","r",stdin);
	//freopen("small_out.txt","w",stdout);	
	freopen("large_in.txt","r",stdin);	
	freopen("large_out.txt","w",stdout);

	int N,cs;
	int i,j;
	int lw,ll;
	cin>>N;
	lw=strlen(wel);
	cin.getline(line,505);
	FOR(cs,1,N)
	{
		cin.getline(line,505);
		memset(cnum,0,sizeof(cnum));
		ll=strlen(line);
		REP(i,ll)
		{
			if(i>0)
			{
				REP(j,lw)
					cnum[i][j]=cnum[i-1][j];
			}
			REP(j,lw)
			{
				if(line[i]==wel[j])
				{
					if(j==0)
						++cnum[i][j];
					else
						cnum[i][j]+=cnum[i][j-1];
					if(cnum[i][j]>=10000)
						cnum[i][j]-=10000;
				}
			}
		}
		printf("Case #%d: %04d\n",cs,cnum[ll-1][lw-1]);
	}
	return 0;		
}
