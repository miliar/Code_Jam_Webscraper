#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#define ss(x)   cout<<"DEBUG : "#x" = "<<(x)<<"\n"
#define pv(i,n) ((i)>0?(i)-1:(n)-1)
#define nx(i,n) ((i)+1<(n)?(i)+1:0)
#define umap    tr1::unordered_map
#define uset    tr1::unordered_set
#define TT      template<typename T>
#define TAB     template<typename A,typename B>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
TT T abs(const T&x) {return x<0?-x:x;}
TT T sq(const T&x) {return x*x;}
TT void mil(T&a,const T&b) {if(a>b)a=b;}
TT void mal(T&a,const T&b) {if(a<b)a=b;}
TT void usort(vector<T>&a) {sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());}
TT T gcd(T a,T b) {while(b!=0){T t=a%b;a=b;b=t;}return a;}
TT pair<T,T> operator+(const pair<T,T>&a,const pair<T,T>&b) {return pair<T,T>(a.first+b.first,a.second+b.second);}
TT pair<T,T> operator-(const pair<T,T>&a,const pair<T,T>&b) {return pair<T,T>(a.first-b.first,a.second-b.second);}
TAB istream&operator>>(istream&i,pair<A,B>&v) {return i>>v.first>>v.second;}
TAB B conv(const A&i) {stringstream s;s<<i;B o;s>>o;return o;}

int n,d;
int p[200];
int v[200];

void york() {
    cout<<fixed<<setprecision(10);
    int ts;
    cin>>ts;
    for (int cs=1;cs<=ts;cs++) {
        cout<<"Case #"<<cs<<": ";
        cin>>n>>d;
        for(int i=0;i<n;++i)cin>>p[i]>>v[i];
        double l=0.0,r=1e20;
        for(int rp=0;rp<128;rp++){
            double m=(l+r)/2.0;
            double x=-1e20;
            bool flag=true;
            for(int i=0;i<n;++i){
                double e=max(x+d,p[i]-m)+(v[i]-1.0)*d;
                if(e-p[i]>m){
                    flag=false;
                    break;
                }
                mal(x,e);
            }
            if(flag)r=m;
            else l=m;
        }
        cout<<(l+r)/2.0<<"\n";
    }
}

int main() {
    //freopen("b.in","r",stdin);
    //freopen("b.out","w",stdout);
    
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    york();
    return 0;
}
