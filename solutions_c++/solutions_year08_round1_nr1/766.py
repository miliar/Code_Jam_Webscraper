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
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    //hash_map<string, int, str_hash, str_compare> entonum;
    vector<int> xi;
    vector<int> yi;
    
    //hash_map<string, int, str_hash, str_compare>::iterator pos;
    int num;   
    int n;
    int i,j,k = 0,l,t;
    cin>>n;
    while(n--)
    {
              xi.clear();
              yi.clear();
              int res = 0;
              ++k;
              cout<<"Case #"<<k<<": ";
              cin>>t;
              for(i = 0;i < t;++i)
              {
                    int tt;
                    cin>>tt;
                    xi.push_back(tt);
              }
              for(i = 0;i < t;++i)
              {
                    int tt;
                    cin>>tt;
                    yi.push_back(tt);
              }
             sort(xi.begin(),xi.end(),less<int>() );
             sort(yi.begin(),yi.end(),greater<int>() );
             for(i = 0;i < t;++i)
             {
                    res+=xi[i]*yi[i];
             }
             cout<<res<<endl;
    }
    return 0;
}
