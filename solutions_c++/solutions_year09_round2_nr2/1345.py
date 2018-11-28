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
#define FORI(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++) 
#define all(a) (a).begin(),(a).end()
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FORZ(i,y) FOR(i,0,y)
typedef long long int ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
#define PB push_back
#define SZ size()
int main()
{
    int nC;
    cin >> nC;
    for(int nc = 1; nc <= nC;++nc)
    {
	printf("Case #%d: ",nc);
	int n;
	cin >> n;
	vi vis(10);
	int x = n;
	while(x)
	{
	    vis[x % 10] ++;
	    x /= 10;
	}
	vis[0] = 0;
	int i;
	for( i = n +1 ;; ++i)
	   {
	       int j = i;
	       vi te(10);
	       while(j)
	       {
		   te[ j %10] ++;
		   j /= 10;
	       }
	       te[0] = 0;
	       if(te == vis) 
	       break;
	   }
	cout << i << endl;

    }
    return 0;
}
