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
//char array[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
   
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w+", stdout);
    int count=0;
    int t;
    int j=0;
    int tt=0;
    int person;
    int a[100];
    int counta=0;
    int surprise;
    int better;
    int p;
    int cond;
    
    cin >> t;

    REP (tt, t+1)
    {           
            //string s;
            //getline(cin,s);
            cin>>person;
            cin>>surprise;
            cin>>better;
          //  cout<<person;
         //   cout<<surprise;
         //  cout<<better;
            vector <string> ss;
            REP (j, person)
            {
            cin>>a[j];
          // cout<<a[j];
            if(surprise)
            {
            //cond=((better*3)-3 ||(better*3)-4));
            if((better-2)>=0)
            p=(better+((2)*(better-2)));
            else 
            p=1;
            if((a[j]>=p && (a[j]!=0) || better==0))
            counta++;
            if( a[j]==( (better*3)-3) ||(a[j]==((better*3)-4)))
            surprise--;
            }
            else
            {
                if((better-1)>=0)
            p=(better+((2)*(better-1)));
            else 
            p=0;
            if((a[j]>=p && (a[j]!=0) || better==0))
            counta++;
            }
            
            }
           count++;
           if((count>1)&& (count<=t))
           cout<<'\n';
           if(count<=t)
           {
             cout << "Case #" << (tt+1) << ": ";
             counta=counta;//+(surprise-1);
             cout<<counta;
           }
             counta=0;
          
    }
    return 0;
}
