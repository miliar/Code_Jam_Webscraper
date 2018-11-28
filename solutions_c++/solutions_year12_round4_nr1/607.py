#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <typeinfo>
#include <set>
#include <cctype>
#include <locale>
#include <utility>
#include <map>
#include <iterator>
#include <valarray>
#include <complex>
#include <sstream>
#include <bitset>
#include <ctime>
#include <list>
#include <numeric>
#include <cstring>
using namespace std;

/*
#include <unordered_map>
#include <unordered_set>
#include <regex>
*/
#define sz size()
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sqr(a) (a)*(a)
#define mp make_pair
#define rall(c) (c).rbegin(), (c).rend()
#define rmp reverse_make_pair



typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<vector<int> > vvint;
typedef vector<char> vchar;
typedef vector<vector<int> > graph;
const int INF=1<<30;

inline int in() {
    int a;
    scanf("%d", &a);
    return a;
}
template<class T1, class T2>
inline pair<T1, T2> reverse_make_pair(T1 x, T2 y){
    return pair<T1, T2>(y, x);
}
template<class T>
ostream& operator<<(ostream& out, const vector<T> a){
    // out << "{";
    if(!a.empty()) out << a[0];
    for(int i = 1; i < (int)a.size(); i++)   out << " " << a[i];
    //out << "}";
    return out;
}
double din() {
    double a;
    scanf("%lf", &a);
    return a;
}

ll gcd(ll a, ll b) {
    while(b){
        a%=b;
        swap(a,b);
    }
    return a;
}

ll lcm(ll a, ll b) {
    return a / gcd(a, b) * b;
}

const double eps = 1e-6;

int logbin(int a){
    a--;
    int res=1;
    while(a) a>>=1, res<<=1;
    return res;
}
int binpow (int a, int n) {
    int res = 1;
    while (n) {
        if (n & 1)
            res *= a;
        a *= a;
        n >>= 1;
    }
    return res;
}
struct treap{
    treap *l,*r;
    int c,y,i,ii;
    int size;
    ll s;
    int mi,ma;
    treap(){
        l=r=NULL;
        size=1;
    }
};
void recalc(treap* &a){
    if(a==NULL) return;
    a->size=1;
    a->mi=a->c;
    a->ma=a->c;
    if(a->l!=NULL){
        a->size+=a->l->size;
        a->ma=max(a->ma,a->l->ma);
        a->mi=min(a->mi, a->l->mi);
    }
    if(a->r!=NULL){
        a->size+=a->r->size;
        a->ma=max(a->ma,a->r->ma);
        a->mi=min(a->mi,a->r->mi);
    }
}


void merge(treap* &t,treap* l, treap* r){
    if(l==NULL) return (void)(t=r);
    if(r==NULL) return (void)(t=l);
    if(r->y > l->y){
        merge(r->l, l, r->l);
        t=r;
    }else{
        merge(l->r, l->r, r);
        t=l;
    }
    recalc (t);
}
void split(treap* v,int x, treap* &l, treap* &r){
    if(v==NULL){
        r=l=NULL;
        return ;
    }
    int cur = 1;
    if(v->l != NULL) cur+=v->l->size;
    if(cur <= x){
        split(v->r, x-cur, v->r, r);
        l=v;
    }else{
        split(v->l, x, l, v->l );
        r=v;
    }
    recalc(v);
}

void dfs(treap *v){
    if(v->l != NULL) dfs(v->l);
    cout<<v->c<<' ';
    if(v->r != NULL) dfs(v->r);
}

/*int t[1002][1002];
int get (int x, int y){
    int r = 0;
    for(int i=x;i>0;i-=i&-i)
        for(int j=y;j>0;j-=j&-j)
            r+=t[i][j];
    return r;
}

void inc (int x, int y, int d){
    for(int i=x;i<=n;i+=i&-i)
        for(int j=y;j<=n;j+=j&-j)
            t[i][j]+=d;
}
vector<int> h;
int s_d(int i){
    if(h[i]>= h[i*2] && h[i]>=h[i*2+1]) return i;
    if(h[i*2]>=h[i*2+1]){
        swap(h[i],h[i*2]);
        return s_d(2*i);
    }else{
        swap(h[i],h[i*2+1]);
        return s_d(2*i+1);
    }
}
int s_u(int i){
    if(h[i]<=h[i/2] || i==1) return i;
    swap(h[i],h[i/2]);
    return s_u(i/2);
}
vector<int> a;
int square(pii a, pii b, pii c){
    return abs((b.first-a.first)*(c.second-a.second)-(c.first-a.first)*(b.second-a.second));
}*/
vector<vector<pair<char,char> > > com;

int main(){
    freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    srand(time(NULL));
    for(int k=0;k<1000000;++k){
        vector<pair<char,char> > a;
        int ii=rand()%10;
        for(int i=0;i<ii;++i){
            int mmm=rand()%20+1;
            int m=(rand()%mmm);
            for(int j=0;j<m;++j){
                int rr=rand()%3;
                if(rr==2) continue;
                if(rr) a.push_back (mp(0,1));
                else a.push_back (mp(0,-1));
            }
            if(rand()%3>0) a.push_back (mp(1,0));
        }
        com.push_back (a);
    }
    int T=in();
    for(int t=1;t<=T;++t){
        int r=in(),c=in();
        int mm=-1;
        vector<string> g;
        for(int i=0;i<r;++i){
            string s;
            cin>>s;
            g.push_back (s);
        }
        vector<set<pair<int,int> > > ee(10,set<pair<int,int> >());
        vector<vector<vector<pair<int,int> > > >e(10,vector<vector<pair<int,int> > > ((int)com.size (),vector<pair<int,int> >()));
        for(int i=0;i<g.size ();++i){
            for(int j=0;j<g[0].size();++j){
                if(g[i][j]!='#'){
                    for(int k=0;k<com.size ();++k){
                        int ii=i;
                        int jj=j;
                        for(int h=0;h<com[k].size();++h){
                            if(ii+com[k][h].first<g.size () && jj+com[k][h].second>=0 && jj+com[k][h].second<g[0].size() && g[ii+com[k][h].first][jj+com[k][h].second]!='#'){
                                ii+=com[k][h].first;
                                jj+=com[k][h].second;
                            }
                        }
                        if(g[ii][jj]!='#' && g[ii][jj]!='.'){
                            int aa=g[ii][jj]-'0';
                            e[aa][k].pb(mp(i,j));
                            mm=max(mm,aa);
                            ee[aa].insert(mp(i,j));
                            //cout<<aa<<endl;
                        }
                    }
                }
            }
        }

        printf("Case #%d:\n",t);
        for(int i=0;i<=mm;++i){
            bool o=1;
            cout<<i<<": ";
            int nn=0;
            bool cc=;
            for(int j=0;j<e[i].size();++j){
                if(e[i][j].size()!=(int)ee[i].size() && e[i][j].size()!=0) o=0;
            }
            cout<<ee[i].size();
            if(o) cout<<" Lucky\n";
            else cout<<" Unlucky\n";
        }


    }


    return 0;
}



