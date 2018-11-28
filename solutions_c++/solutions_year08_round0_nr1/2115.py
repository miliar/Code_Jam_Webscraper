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
    hash_map<string, int, str_hash, str_compare> entonum;
    int en[large];
    hash_map<string, int, str_hash, str_compare>::iterator pos;
    int num;   
    int n;
    int i,j,k = 0,l;
    cin>>n;
    while(n--)
    {
              int res = 0 ;
              ++k;
              cout<<"Case #"<<k<<": ";
              int s,q;
              cin>>s;
              string t;
              getline(cin,t);
              for(i = 0;i < s;++i)
              {
                    en[i] = 0;
              }
              num = 0;
              i = 0;
              l = s;
              while(l--)
              {
                        getline(cin, t);
                        entonum[t] = i++;
                        t = "";
              }
              cin>>q;
              getline(cin, t);
              num = 0;
              while(q--)
              {
                        getline(cin, t);
                        if(!en[entonum[t]])
                        {
                                           ++num;
                                           en[entonum[t]] = 1;
                        }
                        if(num == s)
                        {
                               ++res;
                               num = 1;
                               for(i = 0;i < s;++i)
                               {
                                     en[i] = 0;
                               }
                               en[entonum[t]] = 1;
                        }      
              }
              cout<<res<<endl;
    }
    return 0;
}
