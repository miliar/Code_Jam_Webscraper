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

int main()
{
    int T;
    cin>>T;
    F(xx,T)
     {
            string s;
            cin>>s;
            bool can=0;

            multiset<char> m;
            Repi(s.SZ)
             if (s[i]!='0')
             m.insert(s[i]);

           // cout<<s<<"\n";
            for (int i=(int)s.SZ-1;i>=0;i--)
             {
                        //cout<<"       spos "<<i<<"\n";
                        multiset<char> w=m;
                        string res;
                        Repj(i)
                         {
                                if (s[j]!='0')
                                    w.erase(w.find(s[j]));
                                res+=s[j];
                         }
                        if (w.upper_bound(s[i])==w.end()) continue;
                        res+=*w.upper_bound(s[i]);
                        w.erase(w.upper_bound(s[i]));
                        int left=s.SZ-res.SZ;
                        ///cout<<"                 OK! "<<res<<"  left "<<left<<"\n";
                        Repj(left-(int)w.SZ)
                         {
                                res+="0";
                         }
                        for (multiset<char>::iterator it=w.begin(); it!=w.end(); it++ )
                         res+=*it;
                        cout<<"Case #"<<xx+1<<": "<<res<<"\n";
                        can=1;
                        break;
             }
            if (!can)
             {
                    cout<<"Case #"<<xx+1<<": ";
                    cout<<*m.begin();
                    m.erase(m.begin());
                    Repi((int)s.SZ-(int)m.SZ)
                     cout<<"0";
                    for (multiset<char>::iterator it=m.begin(); it!=m.end(); it++ )
                     cout<<*it;
                    cout<<"\n";
             }
     }
    return 0;
}
