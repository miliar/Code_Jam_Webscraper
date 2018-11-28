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
vector<int>v;
int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int tc;
    cin>>tc;
    for(int cases=1;cases<=tc;cases++){
        cout<<"Case #"<<cases<<": ";
        int n;
        cin>>n;
        v=vector<int>(n);
        for(int i=0;i<n;i++){
            cin>>v[i];
        }
        int dev=0;
        int x=v[0];
        int sum=v[0];
        for(int i=1;i<n;i++){
            x=x^v[i];
            sum+=v[i];
        }
        sum-=*min_element(all(v));
        if(x==0){
            cout<<sum<<endl;    
        }else{
            cout<<"NO"<<endl;    
        }
    }
    //system("pause");
    return 0;
}
