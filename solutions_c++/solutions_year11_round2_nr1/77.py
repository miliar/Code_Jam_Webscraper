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

char mat[100][101];
int f[100][2];
double wp[100],owp[100],oowp[100];

void york() {
    cout<<fixed<<setprecision(10);
    int ts;
    cin>>ts;
    for (int cs=1;cs<=ts;cs++) {
        cout<<"Case #"<<cs<<":\n";
        int n;
        cin>>n;
        for (int i=0;i<n;++i) {
        	cin>>mat[i];
        }
        for (int i=0;i<n;++i) {
            int m=0;
            int w=0;
        	for (int j=0;j<n;++j) {
        		if (mat[i][j]=='1') {
        			++m;
        			++w;
        		}
        		if (mat[i][j]=='0') {
        			++m;
        		}
        	}
        	f[i][0]=w;
        	f[i][1]=m;
        	wp[i]=w==0?0:(double)w/m;
        }
        for (int i=0;i<n;++i) {
            int m=0;
            double s=0.0;
        	for (int j=0;j<n;++j) {
        		if (mat[i][j]!='.') {
        			++m;
        			double t;
        			if (mat[j][i]=='1') t=(f[j][0]-1.0)/(f[j][1]-1.0);
        			else t=(f[j][0]-0.0)/(f[j][1]-1.0);
        			s+=t;
        		}
        	}
        	owp[i]=m==0?0:s/m;
        }
        for (int i=0;i<n;++i) {
            int m=0;
            double s=0.0;
        	for (int j=0;j<n;++j) {
        		if (mat[i][j]!='.') {
        			++m;
        			s+=owp[j];
        		}
        	}
        	oowp[i]=m==0?0:s/m;
        }
        for (int i=0;i<n;++i) {
        	cout<<(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i])<<"\n";
        }
    }
}

int main() {
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    york();
    return 0;
}
