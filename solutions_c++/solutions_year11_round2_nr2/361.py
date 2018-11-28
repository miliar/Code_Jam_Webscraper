#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
using namespace std;  // H A M L E T
long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}long long lcm(long long a,long long b){return a*(b/gcd(a,b));}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int casitos;
    cin>>casitos;
    for(int tc=1;tc<=casitos;tc++){
        cout<<"Case #"<<tc<<": ";
        int D,c;
        cin>>c>>D;
        vector<double>v;
        for(int i=0;i<c;i++){
            int p,q;
            cin>>p>>q;
            for(int j=0;j<q;j++)
                v.push_back(p);
        }
        sort(v.begin(),v.end());
        double low=0;
        double hi=1e+7;
        for(int beso=0;beso<100;beso++){
            double me=(low+hi)/2;
            double izq=-1e+7;
            bool ok=1;
            for(int j=0;j<v.size();j++){
                if(izq<v[j]){
                    if(izq+D<v[j]){
                        if(v[j]-izq-D<=me)
                            izq=izq+D;    
                        else
                            izq=v[j]-me;    
                    }else{
                        if(izq+D-v[j]>me){
                            ok=0;
                            break;    
                        }else{
                            izq=izq+D;    
                        }    
                    } 
                }else{
                    if(izq+D-v[j]>me){
                        ok=0;
                        break;    
                    }else{
                        izq=izq+D;
                    }
                }
            }
            if(ok)
                hi=me;    
            else
                low=me;
        }
         printf("%.12lf\n",low);
    }
    return 0;
}
