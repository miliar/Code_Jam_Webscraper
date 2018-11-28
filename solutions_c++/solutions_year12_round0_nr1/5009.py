#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
 char array[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
   
	freopen("A-small-attempt4.in", "r", stdin);
	freopen("output.txt", "w+", stdout);
    int count=0;
    int t;
    int j=0;
    int tt=0;
    
    cin >> t;

    REP (tt, t+1)
    {           
            string s;
            getline(cin,s);
            vector <string> ss;
            REP (j, s.size())
           {
           if ( s[j] >= 'a' && s[j] <= 'z' ) 
              s[j]=array[s[j]-'a'];
              cout<<s[j];
            
            }
           count++;
           if((count>1)&& (count<=t))
           cout<<'\n';
           if(count<=t)
             cout << "Case #" << (tt+1) << ": ";
          
    }
    return 0;
}
