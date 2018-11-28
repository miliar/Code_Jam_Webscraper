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
        int n;
        cin>>n;
        char c[n][n];
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                cin>>c[i][j];
        vector<double>wp(n,0.0);
        for(int i=0;i<n;i++){
            int juegos=0;
            int win=0;
            for(int j=0;j<n;j++){
                if(c[i][j]!='.'){
                    juegos++;
                if(c[i][j]=='1')
                    win++;
                }
            }
            wp[i]=(double)win/juegos;
        }
        vector<double>owp(n,0.0);
        for(int i=0;i<n;i++){
            double sum=0;  
            int cant=0;  
            for(int j=0;j<n;j++){
                if(c[i][j]!='.'){
                    int juegos=0;
                    int win=0;
                    for(int k=0;k<n;k++){
                        if(k==i)continue;
                        if(c[j][k]!='.'){
                            juegos++;    
                        }
                        if(c[j][k]=='1'){
                            win++;    
                        }
                    }
                    sum+=(double)win/juegos;
                    cant++;
                }
            }
            owp[i]=(double)sum/cant;
        }
        
        vector<double>oowp(n,0.0);
        for(int i=0;i<n;i++){
            double sum=0;
            int juegos=0;
            for(int j=0;j<n;j++){
                if(c[i][j]!='.'){
                    juegos++;
                    sum+=owp[j];
                }
            }
            oowp[i]=(double)sum/juegos;
        }
        cout<<"Case #"<<tc<<":"<<endl;
        for(int i=0;i<n;i++)
            printf("%.12lf\n",0.25 *wp[i]+ 0.50*owp[i]+0.25*oowp[i]);
        
    }
    return 0;
}
