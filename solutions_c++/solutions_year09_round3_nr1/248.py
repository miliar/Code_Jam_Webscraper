#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <float.h>

using namespace std;

// prewritten code

#define sz(x) (int)(x).size()
#define all(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define pb push_back

#define GDB 1
#define DBG(x) if(GDB){cerr << #x <<" = "<< x << endl;}
#define DBGA(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cerr<<x[i]<<' '; cerr<<endl;}
#define DBGV(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cerr<<x[i]<<' '; cerr<<endl;}

// real code
string problem_name="a";
void init(){
    freopen( (problem_name+".in").c_str(),"rt",stdin);
    freopen( (problem_name+".out").c_str(),"wt",stdout);
}
long long solve(string s){
    int i;
    int j=0;

    long long base,ret;
    map<char,int> d;
    for(i=0;i<sz(s);i++) d[s[i]]=-1;
    d[s[0]]=1;
    for(i=1;i<sz(s);i++){
        if(d[s[i]]==-1) d[s[i]]=j,j++;
        if(j==1) j++;
    }
    base=Max(2,j);
    ret=0;
    for(i=0;i<sz(s);i++) ret=ret*base+d[s[i]];
  //  for(i=0;i<sz(s);i++) cout<<d[s[i]]<<" ";
    //cout<<endl;
    return ret;
}
int main(){
    init();
    int T,tt;
    long long ret;
    cin>>T;
    string s;
    for(tt=1;tt<=T;tt++){
        cin>>s;
        ret=solve(s);
      //  DBG(ret);
        printf("Case #%d: %lld\n",tt,ret);
    }
    return 0;
}
