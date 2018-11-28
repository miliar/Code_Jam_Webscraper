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
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

string s[60];
int T,N;

int main()
{
    cin>>T;
    F(xx,T)
     {
            cin>>N;
            Repi(N)
             cin>>s[i];

       //     cout<<"\n";            Repi(N)             cout<<s[i]<<"\n";

            int ans=0;
            Repj(N)
             {
                    int st=N;
                    Repi(N)
                     {
                        bool yes=0;
                        for (int k=j;k<N;k++)
                         if (s[i][k]=='1')
                          { yes=1; break; }
                       if (yes)
                        { st=i; break; }
                     }
                    if (st>=j) continue;
              //      cout<<" fix col "<<j<<" : st "<<st<<"\n";
                    int en=-1;
                    for (int i=st+1;i<N;i++)
                     if (s[i][j]=='0')
                      {
                            bool yes=1;
                            for (int k=j+1;k<N;k++)
                             if (s[i][k]=='1') { yes=0; break; }
                            if (!yes) continue;
                            en=i; break;
                      }
                  //  cout<<"                 en "<<en<<"\n";
                    int diff=en-st;
                    ans+=diff;
                    Repk(diff)
                       swap(s[en],s[en-1]) , en--;
                //      F(l,N)                       cout<<"                    "<<s[l]<<"\n";
                    j--;
             }
            cout<<"Case #"<<xx+1<<": "<<ans<<"\n";
     }
    return 0;
}
