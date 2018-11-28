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

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);

    int test,Ctest=0;

    cin>>test;

    while(test--)
    {
        int n;
        cin>>n;

        VI Bt,Ot,B,O,seqi;
        VC seq;
        int ko=0,kb=0,to=0,tb=0;
        int ans=0;


        REP(i,n)
        {
          char c;
          int b;
          cin>>c>>b;

          if(c=='O')O.pb(b);
          else B.pb(b);
          seq.pb(c);
          seqi.pb(b);
        }


        for(int i=0;i<sz(seq);i++)
        {
           if(i==0)
           {
            if(seq[i]=='B')
           {ans+=B[kb];Bt.pb(ans);kb++;}
           else {ans+=O[ko],Ot.pb(ans),ko++;}
            }

           else
           {
               if(seq[i]=='B')
               {
                   if(kb==0){
                       if(B[kb]-ans<=0)ans+=1;
                       else ans+= abs(ans-B[kb]);
                       Bt.pb(ans);
                   }
                   else
                   {
                       if((abs(B[kb]-B[kb-1])-abs(Bt[tb]-ans))<0)ans+=1;
                       else ans+= (1+( abs(B[kb]-B[kb-1])-abs(Bt[tb]-ans)));
                       tb++;
                       Bt.pb(ans);
                   }

                   kb++;

               }
               else if(seq[i]=='O')
               {
                   if(ko==0){
                       if(O[ko]-ans<=0)ans+=1;
                       else ans+= abs(ans-O[ko]);Ot.pb(ans);
                   }
                   else
                   {
                       if((abs(O[ko]-O[ko-1])-abs(Ot[to]-ans))<0)ans+=1;
                       else ans+= (1+(abs(O[ko]-O[ko-1])-abs(Ot[to]-ans)));
                       to++;Ot.pb(ans);
                   }

                   ko++;
               }
           }

        }
    printf("Case #%d: %d\n",++Ctest,ans);
    Bt.clear();Ot.clear();B.clear();O.clear();seqi.clear();seq.clear();
    }
    return 0;
}
