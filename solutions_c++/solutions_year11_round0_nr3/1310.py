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
#define fo(i,n) for(int i=0;i<(n);++i)
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
ll cross(const pii&a,const pii&b) {return (ll)a.first*b.second-(ll)b.first*a.second;}
ll dot(const pii&a,const pii&b) {return (ll)a.first*b.first+(ll)a.second*b.second;}

void york()
{
    int case_num;
    cin>>case_num;
    for(int cur_case=1;cur_case<=case_num;++cur_case)
    {
        string ans;
        int n;
        int value=0;
        cin>>n;
        vector<int> a(n);
        for(auto&x:a)
        {
            cin>>x;
            value^=x;
        }
        if(value!=0)
        {
            ans="NO";
        }
        else
        {
        	int t=accumulate(a.begin(),a.end(),0)-*min_element(a.begin(),a.end());
        	ans=conv<int,string>(t);
        }
        cout<<"Case #"<<cur_case<<": "<<ans<<'\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    
    york();
    return 0;
}
