#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <stack>
#define mp make_pair
#define pb push_back   
#define setval(a,v) memset(a,v,sizeof(a))
using namespace std;

typedef long long int64;
typedef long double ld;

const string TASKNAME = "C";
const string TASKMOD = "small";
const string INFILE = TASKNAME+"-"+TASKMOD+".in";
const string OUTFILE = TASKNAME+"-"+TASKMOD+".out";


struct polygon{
    vector<int> v;

    polygon split(int l,int r){
        assert(in(l,r));
        int x = lower_bound(v.begin(),v.end(),l) - v.begin();
        int y = lower_bound(v.begin(),v.end(),r) - v.begin();
        polygon p;
        p.v = vector<int>(v.begin()+x,v.begin()+y+1);
        v.erase(v.begin()+x+1,v.begin()+y);
        return p;
    }
    bool in(int l,int r){
        return binary_search(v.begin(),v.end(),l) && binary_search(v.begin(),v.end(),r);
    }
    int& operator[](int a){
        assert(a < (int)v.size() && a>=0);
        return v[a];        
    }
    int operator[](int a)const{
        assert(a < (int)v.size() && a>=0);
        return v[a];        
    }
    int size()const{
        return (int)v.size();
    }
    polygon(){
    }
    void push_back(int x){
        v.pb(x);
    }
    void print(){
        cerr<<"POLY! ";
        copy(v.begin(),v.end(),ostream_iterator<int>(cerr," "));
        cerr<<endl;
    }
};

vector<polygon> p;



void PreCalc(){
}

const int MAXN = 2222;

int u[MAXN];
int v[MAXN];
int n;

int col[MAXN];
bool used[MAXN];
int cnt;
int m;

bool check(){
   // copy(col,col+n,ostream_iterator<int>(cerr," "));
    for (int i=0;i<(int)p.size();i++){
        for (int j=0;j<cnt;j++)
            used[j] = 0;
        for (int j=0;j<p[i].size();j++)
            used[col[p[i][j]]] = true;
        for (int j=0;j<cnt;j++)
            if (!used[j]){
     //           cerr<<" :BAD"<<endl;
                return false;
            }
    }
    //cerr<<" :GOOD"<<endl;
    return true;        
}


bool perebor(int pos,int cur){
    if (pos == n){
        return cur == cnt && check();
    }
    for (int i=0;i<cur;i++){
        col[pos] = i;
        if (perebor(pos+1,cur))
            return true;
    }
    if (cur < cnt){
        col[pos] = cur;
        if (perebor(pos+1,cur+1))
            return true;
    }
    return false;
}

void splitpolygons(){
   for (int i=0;i<m;i++){
       --v[i],--u[i];
       for (int j=0;j<(int)p.size();j++)
         if (p[j].in(u[i],v[i])){    
            polygon tmp =p[j].split(u[i],v[i]);
            p.pb(tmp);
            break;
         }
       //for (int j=0;j<p.size();j++)
        //    p[j].print();    
       //cerr<<endl;
   }                          
}


void solve(){
    scanf("%d %d",&n,&m);
    p.clear();
    p.pb(polygon());
    for (int i=0;i<n;i++)
        p[0].pb(i);
    for (int i=0;i<m;i++)
        scanf("%d",&u[i]);
    for (int i=0;i<m;i++)
        scanf("%d",&v[i]);
    splitpolygons();
    for (cnt=1;;cnt++){
        if (!perebor(0,0))
            break;
        //cerr<<endl;
    }
    --cnt;
    perebor(0,0);
    cout << cnt << endl;
    for (int i=0;i<n;i++)
        cout << col[i]+1 << " \n"[i==n-1];
}

int main(){
    freopen(INFILE.data(),"r",stdin);
    freopen(OUTFILE.data(),"w",stdout);
    PreCalc();
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
        {
            printf("Case #%d: ",i);
            solve();
            if (i>t-20 || i%10==0)
                cerr<<"SOLVED:"<<i<<endl;
        }
  return 0;
}
