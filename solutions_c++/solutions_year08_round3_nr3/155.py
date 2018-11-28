#include<cstdlib>
#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
#include<cmath>
#include<numeric>
#include<string>
#include<deque>
#include<list>
#include<map>
#include<set>
#include<stack>
#include<sstream>
#include<ostream>
#include<istream>
#include<iomanip>
#include<ext/hash_map> 
#define large 100
#define small 10

using namespace std;
using namespace __gnu_cxx;

struct str_hash{
        size_t operator()(const string& str) const
        {
                return __stl_hash_string(str.c_str());
        }
};

struct str_compare{
        bool operator()(const string &p1, const string &p2) const{
                if(p1 == p2)
                {
                             return true;
                }
                else return false;
        }
};

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    vector<long long> count;
    vector<long long> a;
    vector<long long> ra;
    long long N,m,x,y,z;   
    int n;
    long long i,j,k = 0,l;
    cin>>n;
    while(n--)
    {
              long long res = 0;
              ++k;
              cout<<"Case #"<<k<<": ";
              cin>>N>>m>>x>>y>>z;
              a.clear();
              a.resize(m);
              ra.clear();
              ra.resize(N);
              count.clear();
              count.resize(N);
              for(i = 0;i < m; ++i)
              {
                    cin>>a[i];                
              }
              for(i = 0;i < N;++i)
              {
                    ra[i] = a[i%m];
                    count[i] = 0;
                    //cout<<ra[i]<<endl;
                    a[i%m] = (x * a[i%m] + y * (i + 1))% z;
              }
              count[0] = 1;
              for(i = 1;i < N;++i)
              {        
                    count[i]+=1;           
                    for(j = 0; j < i ;++j)
                    {
                       if(ra[i] > ra[j])
                       {
                                count[i] += count[j];
                                count[i] %= 1000000007;
                       }   
                    }                    
              }
              for(i = 0;i < N;++i)
              {
                    res+=count[i];
                    res%=1000000007;
              }
              cout<<res<<endl;
    }
    return 0;
}
