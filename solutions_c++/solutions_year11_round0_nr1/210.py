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
    int tc;
    cin>>tc;
    string s;
    for(int cases=1;cases<=tc;cases++){
        cout<<"Case #"<<cases<<": ";
        int dev=0;
        int tam;
        cin>>tam;
        vector<int>v(tam);vector<bool>ok(tam,1);
        for(int i=0;i<tam;i++){
            char ad;cin>>ad;
            if(ad=='O')ok[i]=0;
            cin>>v[i];    
        }
        int o=1;int b=1;
        for(int i=0;i<v.size();i++){
            if(ok[i]==0){
                int aum=abs(v[i]-o)+1;
                dev+=aum;
                o=v[i];
                for(int j=i+1;j<v.size();j++){
                    if(ok[j]==1){
                        if(v[j]>b){
                            b=min(v[j],b+aum);
                        }else
                        if(v[j]<b){
                            b=max(v[j],b-aum);   
                        }
                        break;    
                    }    
                }
            }else{
                int aum=abs(v[i]-b)+1;
                dev+=aum;
                b=v[i];
                for(int j=i+1;j<v.size();j++){
                    if(ok[j]==0){
                        if(v[j]>o){
                            o=min(v[j],o+aum);
                        }else
                        if(v[j]<o){
                            o=max(v[j],o-aum);   
                        }
                        break;    
                    }    
                }    
            }   
        }
        cout<<dev<<endl;    
        // o 1 2 3 4 
        // b 1 2 3 4 5
    }
    return 0;
}
