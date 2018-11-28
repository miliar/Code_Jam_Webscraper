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

int n;
int m;
int lim;
int conn[8][8];
int ans;
int color[8];

int path[16];
bool mk[16];

vector<vector<int>> cir;
set<vector<int>> hs;

void find_circle(int u, int st, int pn) {
    path[pn++] = u;

    if (conn[u][st] == 1 && pn >= 3) {
        //cout<<"[";
        //for (int i = 0; i < pn; ++i) cout<<path[i]<<' ';
        //cout<<"]\n";
        
        bool flag = true;
        for (int i = 0; i < pn; ++i) {
            for (int j = i + 2; j < pn; ++j) {
                if (i + pn - j <= 1) continue;
                if (conn[path[i]][path[j]]) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag) {
            vector<int> q(path, path + n);
            sort(q.begin(), q.end());
            if (hs.find(q) == hs.end()) {
                cir.push_back(vector<int>(path, path + pn));
                hs.insert(q);
            }
            return;
        }
    }
    mk[u] = true;
    for (int v = st + 1; v < n; ++v) {
        if (conn[u][v] && !mk[v]) {
            find_circle(v, st, pn);
        }
    }
    mk[u] = false;
}

int co[16];

bool dfs(int p,int cn) {
    if(p==n){
        for (int i=0;i<cir.size();i++) {
            set<int> s;
            for(int j=0;j<cir[i].size();++j){
                s.insert(co[cir[i][j]]);
            }
            if(s.size()<cn)return false;
        }
        return true;
    }
    for(int i=0;i<cn;++i){
        co[p]=i;
        if(dfs(p+1,cn))return true;
    }
    return false;
}

bool test(int cn) {
    co[0]=0;
    bool flag=dfs(1,cn);
    
    if(flag){
        for(int i=0;i<n;++i)color[i]=co[i];
        return true;
    }else {
        return false;
    }
}

void york() {
    int ts;
    cin>>ts;
    for (int cs=1; cs<=ts; ++cs) {
        cout<<"Case #"<<cs<<": ";
        cin>>n>>m;
        if(m==0){
            cout<<n<<"\n";
            for(int i=1;i<=n;++i){
                if(i>1)cout<<' ';
                cout<<i;
            }
            cout<<"\n";
            continue;
        }
        
        cir.clear();
        hs.clear();
        int t[8][2];
        for(int i=0;i<m;++i){cin>>t[i][0];--t[i][0];}
        for(int i=0;i<m;++i){cin>>t[i][1];--t[i][1];}
        memset(conn,0,sizeof conn);
        for(int i=0;i<n;++i)conn[i][(i+1)%n]=1;
        for(int i=0;i<n;++i)conn[(i+1)%n][i]=1;
        for(int i=0;i<m;++i){
            //printf("%d %d\n",t[i][0],t[i][1]);
            conn[t[i][0]][t[i][1]]=1;
            conn[t[i][1]][t[i][0]]=1;
        }
        for(int i=0;i<n;++i){
            memset(mk,0,sizeof mk);
            find_circle(i,i,0);
        }
        
        
        /*
        for(int i=0;i<cir.size();++i){
            for(int j=0;j<cir[i].size();++j){
                cout<<cir[i][j]<<' ';
            }
            cout<<endl;
        }
        */
        
        ans=1;
        for(int i=0;i<n;++i)color[i]=0;
        
        int mx=n-1;
        for(int i=0;i<cir.size();++i)mil(mx,(int)cir[i].size());
        for(int i=2;i<=mx;++i){
            if(test(i))ans=i;
        }
        cout<<ans<<"\n";
        for(int i=0;i<n;++i){
            if(i>0)cout<<' ';
            cout<<color[i]+1;
        }
        cout<<'\n';
    }
}

int main() {
    //freopen("c.in","r",stdin);
    //freopen("c.out","w",stdout);
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    york();
    return 0;
}
