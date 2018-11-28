      		      				   /*Bismillahir Rahmanur Rahim*/
//Template created by topcoder00

//headers

# include <list>
# include <deque>
# include <bitset>
# include <algorithm>
# include <functional>
# include <numeric>
# include <utility>
# include <sstream>
# include <iostream>
# include <iomanip>
# include <cstdio>
# include <cmath>
# include <cstdlib>
# include <ctime>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <limits>
# include <stack>
# include <vector>
# include <cstring>
# include <cstdio>
# include <fstream>
using namespace std;

//functions

int pel(string s){string t;t=s;reverse(t.begin(),t.end());if(s==t)return 1;return 0;}
string toString(int n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
bool isprime(int m){if(m<2) return 0;for( int i=2; i*i<=m ; i++)if(m%i==0)return 0; return 1;return 0;}

//Defines

# define __(array,w)   memset(array,w,sizeof array)
# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)
# define all(c) (c).begin(), (c).end()
# define sz(x) x.size()
# define pb push_back
# define MP make_pair
# define SBS(s,a,b) (s).substr(a,b)
# define UNQ(s) {sort(all(s));(s).erase(unique(all(s)),s.end());}
# define rive(s) reverse(s.begin(),s.end())
# define VI vector<int>
# define VS vector<string>
# define VC vector<char>
# define X first
# define Y second
# define out(a) cout<<#a<<"= "<<a<<endl;

//anything more


//coding start

int main()
{

    //freopen("A-small-attempt0.in","r",stdin);
    freopen("aout.txt","w",stdout);

    int test,tcase=0;
    cin>>test;
    while(test--)
    {
        char graph[55][55];
        int R,C;

        cin>>R>>C;
        bool nai=0;
        REP(i,R)
        {
           REP(j,C)
           {
                cin>>graph[i][j];
                if(graph[i][j]=='.')nai=1;
           }
        }
        REP(i,R)
        {
            REP(j,C)
            {
                if(i+1<R && j+1<C && graph[i][j]=='#'&&graph[i][j+1]=='#'&&graph[i+1][j]=='#'&&graph[i+1][j+1]=='#')
                graph[i][j]='/',graph[i][j+1]='\\',graph[i+1][j]='\\',graph[i+1][j+1]='/';
            }
        }
        bool rit=1;
        REP(i,R)
        {
            REP(j,C)
            {
               if(graph[i][j]=='#')rit=0;
            }
        }
        printf("Case #%d:\n",++tcase);
        if(!rit)cout<<"Impossible\n";
        else
        {
            REP(i,R)
            {
                REP(j,C)
                {
                    cout<<graph[i][j];
                }cout<<endl;
            }
        }

    }

    return 0;
}
//end of coding
