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
using namespace std;
#define inf 987654321
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++) 
#define FR(i,x,y) for(int i=x;i<y;++i)
#define FRZ(i,y) FR(i,0,y)
typedef long long int ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ll> vl;
#define GV ({int t;scanf("%d",&t);t;})
#define CS c_str()
#define PB push_back
#define SZ size()
int main()
{
    int test = GV;
    FR(z,1,test+1)
    {
	int s = GV;
	char names[s][105];
	getchar();
	for(int i=0;i<s;++i)
            gets(names[i]);
           
	int q = GV;
	getchar();
	map<string,int> vis;
	char t[105];
	int ans =0 ;
	FRZ(i,q)
	{
	    gets(t);
	    if(vis.find(t)==vis.end())
	    {
		if(vis.size() == s-1)
		{
		    vis.clear();
		    vis[t]=1;
		    ans++;
		}
		else
		 vis[t] = 1;
	    }
	}	
	printf("Case #%d: %d\n",z,ans);
    }
}
