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
        cout<<"Case #"<<cases<<": ";
        int R,C,D;
        cin>>R>>C>>D;
        int c[R][C];
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++){
               char ad;
               cin>>ad;
               c[i][j]=ad-'0';
            }
        int maxi=-1;
        for(int k=3;k<=min(R,C);k++)
            for(int i=0;i+k-1<R;i++)
                for(int j=0;j+k-1<C;j++){
                    double inix=0.5;double iniy=0.5+k-1;
                    double centrox=k/2.0;double centroy=k/2.0;    
                    double sumx=0.0;double sumy=0.0;
                    for(int ii=i;ii<i+k;ii++)
                        for(int jj=j;jj<j+k;jj++){
                            if(ii==i && jj==j)continue;
                            if(ii==i && jj==j+k-1)continue;
                            if(ii==i+k-1 && jj==j)continue;
                            if(ii==i+k-1 && jj==j+k-1)continue;
                            double x=inix+jj-j;
                            double y=iniy+i-ii;
                            sumx+=(x-centrox)*c[ii][jj];
                            sumy+=(y-centroy)*c[ii][jj];
                        }
                    if(abs(sumx)<1e-6 && abs(sumy)<1e-6){
                        maxi=max(maxi,k);    
                    }
                }
        if(maxi==-1)cout<<"IMPOSSIBLE"<<endl;
        else cout<<maxi<<endl;  
    }
    return 0;
}
