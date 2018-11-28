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
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    vector<int> times;
    int p,k,l;
    int num;   
    int n;
    int i,j,mk = 0;
    cin>>n;
    while(n--)
    {
              long long res = 0 ;
              ++mk;
              times.clear();
              cout<<"Case #"<<mk<<": ";
              cin>>p>>k>>l;
              int t;
              for(i = 0;i < l;++i)
              {
                    cin>>t;
                    times.push_back(t);
              }
              sort(times.begin(),times.end(),greater<int>());
              int step = 0;
              if(l%k == 0) step = l/k;
              else step = l/k + 1;
              for(i = 1;i<= step;++i)
              {
                    long long sum= 0;
                    j = 0;
                    while(j < k && j + (i - 1)*k < times.size())
                    {
                            sum+=times[j + (i - 1)*k];
                            ++j;
                    }
                    res+=sum*i;
              } 
              cout<<res<<endl;
    }
    return 0;
}
