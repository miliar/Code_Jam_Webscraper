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
bool orden(pair<int,int>a,pair<int,int>b){
    if(a.second!=b.second)return a.second<b.second;
    return a.first>b.first;    
}
int main(){
   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int tc;
    cin>>tc;
    for(int cases=1;cases<=tc;cases++){
        cout<<"Case #"<<cases<<": ";
        int X,S,R,T,N;
        cin>>X>>S>>R>>T>>N;
        vector<pair<int,int> >p(N);
        int sum=0;
        for(int i=0;i<N;i++){
            int a,b,c;
            cin>>a>>b>>c;
            p[i]=make_pair(b-a,c);
            sum+=b-a;
        }
        int cantw=X-sum;
        sort(p.begin(),p.end(),orden);
        double mini=1e+8;        
        // Primero
        if(R*T<=cantw){
            double h=T+(cantw-R*T)/(double)S;
            for(int i=0;i<p.size();i++){
                h+=(double)p[i].first/( S+p[i].second);    
            }
            mini=h;    
        }else{
            double h=(cantw)/(double)(R);
            double tot=h;
            for(int i=0;i<p.size();i++){
                if(tot+(double)p[i].first/(p[i].second+R)<=T ){
                    tot+=(double)p[i].first/(p[i].second+R);    
                }else{
                    double distan=p[i].first;
                    distan-=(p[i].second+R)*(T-tot);
                    tot=T;
                    tot+=(double)(distan)/(S+p[i].second); 
                    for(int j=i+1;j<p.size();j++){
                        tot+=(double)p[j].first/(S+p[j].second);    
                    }
                    break;
                }    
            }
            mini=tot;
        }
        double mini2=1e+8;
        //segundo
        double tot=0;
        for(int i=0;i<p.size();i++){
            if(tot+(double)p[i].first/(p[i].second+R)<=T ){
                tot+=(double)p[i].first/(p[i].second+R);    
            }else{
                double distan=p[i].first;
                distan-=(p[i].second+R)*(T-tot);
                tot=T;
                tot+=(double)(distan)/(S+p[i].second); 
                for(int j=i+1;j<p.size();j++){
                    tot+=(double)p[j].first/(S+p[j].second);    
                }
                break;
            }    
        }
        mini2=tot;
        if(tot>T){
            mini2+=(double)cantw/S;    
        }else{
            double tiemp_res=T-tot;
            if(tiemp_res>=(double)cantw/R){
                mini2+=(double)cantw/R;
            }else{
                mini2+=tiemp_res+(double)(cantw-tiemp_res*R)/S;   
            }        
        }
        mini=min(mini,mini2);
        printf("%.10lf\n",mini);
    }
    return 0;
}
