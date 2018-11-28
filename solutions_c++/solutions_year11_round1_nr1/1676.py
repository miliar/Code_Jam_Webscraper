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
    int cases;
    cin>>cases;
    for(int tc=1;tc<=cases;tc++){
        int dev=0;
        long long n,pd,pg;
        cin>>n>>pd>>pg;
        if(pg==100&& pd!=100){
            cout<<"Case #"<<tc<<": Broken"<<endl;   
            continue;
        }
        if(pd==0 && pg==0){
            cout<<"Case #"<<tc<<": Possible"<<endl;   
            continue;
        }
        if(pd==0 && pg!=0){
            cout<<"Case #"<<tc<<": Possible"<<endl;   
            continue;
        }
        if(pd!=0 && pg==0){
            cout<<"Case #"<<tc<<": Broken"<<endl;   
            continue;
        }
        long long h=(long long)(100/gcd(pd,100));
        if(h<=n){
            cout<<"Case #"<<tc<<": Possible"<<endl;   
            continue;    
        }else{
            cout<<"Case #"<<tc<<": Broken"<<endl;   
            continue;    
        }
    }
    return 0;
}
