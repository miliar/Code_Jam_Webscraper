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
#include <string.h>
#include <stdio.h>
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
using namespace std;  // H A M L E T
long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}long long lcm(long long a,long long b){return a*(b/gcd(a,b));}

int main(){
    
   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    char a[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t;
    cin>>t;
    string s;
    getline(cin,s);
    
    for(int i=1;i<=t;i++){
        cout<<"Case #"<<i<<": ";
        getline(cin,s);
        for(int j=0;j<s.size();j++){
            if(s[j]==' ')cout<<' ';
            else cout<<a[s[j]-'a'];
        }
        cout<<endl;
    }
    
    return 0;
}
