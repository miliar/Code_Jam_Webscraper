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

int P;
bool ev(int t){
    if(t%3==0)return (t/3)>=P;
    return (t/3+1)>=P;    
}

bool ev2(int t){
    if(t%3==2)return (t/3+2)>=P;
    return (t/3+1)>=P;
}

int main(){
  
      int tc;
    cin>>tc;
    
    for(int caso=1;caso<=tc;caso++){
        int N,S;
        cin>>N>>S>>P;
        vector<int>v(N);
        
        for(int i=0;i<N;i++)cin>>v[i];    
        
        sort(all(v));
        int cont=0;
        int usado=0;
        
        for(int i=0;i<v.size();i++){
            if(ev(v[i])){
                cont++;    
                continue;
            }
            
            if(usado==S)continue;
            if(v[i]<2)continue;
            if(ev2(v[i])){
                usado++;
                cont++;
                continue;    
            }
            
        }
        
        cout<<"Case #"<<caso<<": "<<cont<<endl;
    }
    // 0 1 1
    
    // 1 2 3 -> 6 - 0
    // 1 3 3 -> 7 - 1
    // 2 2 4 -> 8 - 2 
    return 0;
}
