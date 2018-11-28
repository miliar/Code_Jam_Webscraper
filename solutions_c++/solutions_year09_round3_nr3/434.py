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
vi vec;
int nn;
int solve(int mask,vi cell)
{
    int ans = INT_MAX;
    FORZ(i,nn)
    {
	if(!((1<<i)& mask))
	{
	    int cnt = 0;
	    cell[vec[i]] = 0;
	    int j = vec[i]+1;
	    while(cell[j] == 1)
	    {
		cnt++;
		j++;
	    }
//	    cout << cnt << endl;
	    j = vec[i] -1;
	    while(cell[j] == 1)
	    {
		cnt++;
		j--;
	    }
//	    cout << cnt << endl;
	    ans <?= cnt + solve(mask | (1<<i),cell);
	    cell[vec[i]] = 1;
	}
    }

    return ans == INT_MAX ? 0 : ans;
}
int main()
{
    int nC;
    cin >> nC;
    for(int nc = 1; nc <= nC;++nc)
    {
	printf("Case #%d: ",nc);
	int  P ;
	cin >> P;
	vi cell(P+4);
	cell[0] = 0;
	FOR(i,1,P+1)
	    cell[i] = 1;
	cell[P+1] = 0;
	vec.clear();
	cin >> nn;
	FORZ(i,nn)
	{
	    int xx;
	    cin >> xx;
	    vec.PB(xx);
	}
	cout << solve(0,cell) << endl;

    }
    return 0;
}
