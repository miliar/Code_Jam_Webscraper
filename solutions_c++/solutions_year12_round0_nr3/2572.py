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

vector<int>v[2000001];

int main(){
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    
    
    int tc;
    cin>>tc;
    for(int i=1;i<2000001;i++){
        string s=tos(i);
        set<int>S;
        for(int j=1;j<s.size();j++){
            if(s[j]=='0')continue;
            S.insert(toi(s.substr(j)+s.substr(0,j)));    
        }    
        vector<int>x(all(S));
        for(int j=0;j<x.size();j++)v[i].push_back(x[j]);
    }
    
    
    for(int caso=1;caso<=tc;caso++){
        int a,b;
        cin>>a>>b;
        int cont=0;
        for(int i=a;i<=b;i++){
            for(int j=0;j<v[i].size();j++){
                if(v[i][j]>=a && v[i][j]<=b && v[i][j]>i)
                    cont++;    
            }    
        }
            
        cout<<"Case #"<<caso<<": "<<cont<<endl;
    }
    return 0;
}
