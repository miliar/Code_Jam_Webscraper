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
    for(int cases=1;cases<=tc;cases++){
        cout<<"Case #"<<cases<<": [";
        int a,b,c;
        cin>>a;
        map<string,string>C;
        for(int i=0;i<a;i++){
            string aux;
            cin>>aux;
            C[aux.substr(0,2)]=aux.substr(2);
            C[string(1,aux[1])+string(1,aux[0])]=aux.substr(2);
        }
        cin>>b;
        set<string>S;
        for(int i=0;i<b;i++){
            string aux;
            cin>>aux;
            S.insert(aux);
            reverse(all(aux));
            S.insert(aux);
        }
        int tam;cin>>tam;
        string s;
        cin>>s;
        string dev="";
        for(int i=0;i<s.size();i++){
            dev+=s[i];
            if(dev.size()==1)continue;
            string combina="";
            combina+=dev[dev.size()-2];
            combina+=dev[dev.size()-1];
            if( C.find(combina) !=C.end() ){
                dev=dev.substr(0,dev.size()-2)+C[combina];
                continue;
            }
            combina="";
            combina+=dev[0];
            combina+=dev[dev.size()-1];
            for(int j=0;j<dev.size();j++)
                for(int k=j+1;k<dev.size();k++){
                    string beso=""; beso+=dev[j];
                    beso+=dev[k];
                    if(S.find(beso)!=S.end()){    
                        dev="";
                    }
                }
        }
        for(int i=0;i<dev.size();i++){
            if(i==dev.size()-1){
                cout<<dev[i]<<"]";
            }else{
                cout<<dev[i]<<", ";
            }    
        }
        if(dev.size()==0)cout<<"]";
        cout<<endl;
    }
    return 0;
}
