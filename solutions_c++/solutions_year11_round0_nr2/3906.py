                           /*in the name of Allah */
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

# define MEM(array,w)   memset(array,w,sizeof array)
# define ULL unsigned long long
# define eps 1e-9
# define SS stringstream
# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i, 0, a)
# define rive(s) reverse(s.begin(),s.end())
# define PII pair<int , int>
# define MPSS map<string, string>
# define MPIS map<int, string>
# define MPSI map<string, int>
# define MPII map<int, int>
# define MPIC map<int,char>
# define MPCI map<char, int>
# define all(c) (c).begin(), (c).end()
# define VS vector<string>
# define VI vector<int>
# define VC vector<char>
# define VB vector<bool>
# define sz(x) x.size()
# define pb push_back
# define STI set<int>
# define STC set<char>
# define STS set<string>
# define OK(R,C) if(i<0 && j<0 && j==C && i==R)
# define MP make_pair
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}

int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}

bool isprime(int n){if( n<2) return 0;for( int i=2; i*i<=n ; i++)if(n%i==0)return 0; return 1;return 0;}

int pel(string s){string t;t=s;reverse(t.begin(),t.end());if(s==t)return 1;return 0;}

char graph[100][100];
bool visited[100][100];
int row,col;

int dr[]={0,0,1,-1};
int dc[]={1,-1,0,0};
int rchange[] = {-1,0,1,-1,0,1};
int cchange[] = {-1,-1,0,0,1,1};

typedef pair<string,string> PSC;

int main()
{

    freopen("B-small-attempt1.in","r",stdin);
    freopen("b.out","w",stdout);

    int test,Ctest=0;

    cin>>test;

    while(test--)
    {
        vector <PSC> vin;
        vector< pair<char,char> > vop, vop2;

        string res="";
        int c;
        cin>>c;
        string invoke="";
        REP(i,c)
        {
            string s;
            cin>>s;
            invoke+=s[0];invoke+=s[1];
            sort(all(invoke));
            vin.pb(MP(invoke,s.substr(2)));
        }
        int d;
        cin>>d;
        REP(i,d)
        {
            string t;
            cin>>t;
            vop.pb(MP(t[0],t[1]));
            vop2.pb(MP(t[1],t[0]));
        }
        int n;
        cin>>n;
        string u;
        cin>>u;

        REP(i,sz(u))                           /*in the name of Allah */
        {
            res+=u[i];

            string sb="";
            sb+=res[res.size()-1];
            if(res.size()-2>=0)
            sb+=res[res.size()-2];


            sort(all(sb));

            bool f=0;
            REP(j,sz(vin))
            {
                if(vin[j].first==sb)
                {
                    res.replace(res.size()-2,2,vin[j].second);f=1;
                }
            }
            if(f==0)
            {
                REP(j,sz(vop))
                {
                    if(res[res.size()-1]==vop[j].first)
                    {for(int k=0;k<res.size();k++)
                    if(res[k]==vop[j].second)res.clear();
                    }
                    else if(res[res.size()-1]==vop2[j].first)
                    {
                        for(int k=0;k<res.size();k++)
                        if(res[k]==vop2[j].second)res.clear();
                    }
                }
            }
        }
        if(res.size()!=0){printf("Case #%d: [",++Ctest);
        REP(i,sz(res)-1)cout<<res[i]<<", ";cout<<res[sz(res)-1];
        printf("]\n");
        }
        else printf("Case #%d: []\n",++Ctest);

    }
    return 0;

}
