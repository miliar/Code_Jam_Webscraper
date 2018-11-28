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
string problem_name="b";
void init(){
    freopen( (problem_name+".in").c_str(),"rt",stdin);
    freopen( (problem_name+".out").c_str(),"wt",stdout);
}
string go(string s){
    string ret="";
    int j=0;
    while(sz(s)<20) s="0"+s;
    next_permutation(all(s));
    while(s[j]=='0') j++;
    for(;j<sz(s);j++) ret+=s[j];
    return ret;
}
int main(){
    init();
    string s;
    int T;
    int i;
    cin>>T;
    for(i=1;i<=T;i++){
        cin>>s;
        s=go(s);
        cout<<"Case #"<<i<<": "<<s<<endl;
    }
    return 0;
}
