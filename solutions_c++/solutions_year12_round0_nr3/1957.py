//#pragma comment (linker, "/STACK:64000000")
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
#define mp(a,b) make_pair((a), (b))
#define rall(c) (c).rbegin(), (c).rend()



typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

int in() {
    int a;
    scanf("%d", &a);
    return a;
}

double din() {
    double a;
    scanf("%lf", &a);
    return a;
}

int gcd(int a, int b) {
    while(b){
        a%=b;
        swap(a,b);
    }
    return a;
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}

const double eps = 1e-7;

int logbin(int a){
    int res=1;
    while(a) a>>=1, res<<=1;
    return res;
}
vector<vector<int> > g;
vector<char> u;
vector<int> mt;
const int INF=1<<30;
char kun(int v){
    u[v]=1;
    for(int i=0;i<g[v].size();++i){
        int to=g[v][i];
        if(mt[to]==-1 ||(!u[mt[to]] && kun(mt[to]))){
            mt[to]=v;
            return 1;
        }
    }
    return 0;
}
int getnextnum(int a,int s){
    int b=a%10;
    a/=10;
    a+=b*pow(10,s-1);
    return a;
}

int main(){
    freopen("4.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t=in();
    for(int i=0;i<t;++i){
        int a=in(),b=in();
        int s=0;
        int aa=a;
        while(aa>0){
            ++s;
            aa/=10;
        }
        long long res=0;
        for(int j=a;j<=b;++j){
            int l=j;
            set<int> m;
            for(int k=1;k<s;++k){
                int c=getnextnum (l,s);
                if(c>j && c>=a && c<=b) m.insert (c);
                l=c;
            }
            res+=(int)m.size ();
        }
        printf("Case #%d: ",i+1);
        cout<<res<<endl;
    }


/*
    int t=in();
    for(int i=0;i<t;++i){
        int res=0;
        vector<int> v,w,vv;
        int n=in(),s=in(),p=in();
        for(int j=0;j<n;++j){
            int a=in();
            if(a%3==0){
                if(a/3>=p) ++res; else
                    v.push_back (a/3);
            }
            if(a%3==1){
                if((a/3)+1>=p) ++res; else
                    w.push_back (a/3+1);
            }
            if(a%3==2){                if((a/3)+1>=p) ++res; else vv.push_back (a/3+1);}
        }
        sort(rall(v));
        sort(rall(vv));
        sort(rall(w));
        for(int j=0;j<v.size ();++j){
            if(v[j]>=(p-1) && s>0 && v[j]>0){
                // cout<<v[j]<<" ";
                ++res;
                --s;
            }else break;
        }
        // cout<<res;
        for(int j=0;j<vv.size ();++j){
            if(vv[j]>=(p-1) && s>0 && vv[j]>0){
                ++res;
                --s;
            }else break;
        }
        printf("Case #%d: ",i+1);
        cout<<res<<endl;
    }
    */
    return 0;
}
