#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<char> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int n,tn;
char dub[1000000],pc[1000];
vector<pair<string,double> > tr;
set<int> Q;

double f(int i,set<string> a){
    if(!Q.count(i))return 1;
    double res=tr[i].second;
    if(a.count(tr[i].first))res*=f(2*i,a);
    else res*=f(2*i+1,a);
    return res;
}

int miss_white(int k){
    for(;isspace(dub[k]);k++);
    return k;
}

int parse(int k,int p){
    k=miss_white(k);
    if(dub[k]!='(')return -1;
    k=miss_white(k+1);
    if(!isdigit(dub[k]))return -1;
    double w=0;
    for(;k<n&&isdigit(dub[k]);++k)
        w=w*10+dub[k]-'0';
    if(dub[k]=='.'){
        double q=0,b=10;
        for(k++;k<n&&isdigit(dub[k]);++k,b*=10)
            q+=(dub[k]-'0')/b;
        w+=q;
    }
    k=miss_white(k);
    int l=0;
    for(;k<n&&isalpha(dub[k]);++k)
        pc[l++]=dub[k];
    pc[l]=0;
    string feach=(string)pc;
    if(tr.size()<p+1)tr.resize(p+1);
    tr[p]=make_pair(feach,w);
    Q.insert(p);
    if(dub[k]==')')return miss_white(k+1);
    k=parse(parse(k,2*p),2*p+1);
    if(dub[k]!=')')return -1;
    return miss_white(k+1);
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("x.out","w",stdout);
    int uiu;
    scanf("%d\n",&uiu);
    for(int t=1;t<=uiu;++t){
        cout<<"Case #"<<t<<":"<<endl;
        int l;
        scanf("%d\n",&l);
        string s;
        n=0;
        for(int i=0;i<l;++i){
            getline(cin,s);
            for(int j=0;j<s.size();++j)
                dub[n++]=s[j];
        }
        dub[n]=0;
        tr.clear();
        Q.clear();
        if(parse(0,1)!=n)
            cout<<"oops"<<endl;
        tn=tr.size();
        int k;
        scanf("%d\n",&k);
        string name;
        int c;
        for(int i=0;i<k;++i){
            cin>>name>>c;
            string ss;
            set<string> redf;
            for(int j=0;j<c;++j){
                cin>>ss;
                redf.insert(ss);
            }
            cout<<f(1,redf)<<endl;
        }
    }
    return 0;
}
