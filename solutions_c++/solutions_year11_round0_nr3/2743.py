#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
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
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int i=(a);(int)i<(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}

string tobase(int a,int b)
{
 string s;
 do
 {
   int t;
   char c;
   t =  a%b;
   if(t>=10) c='A'+t-10;
   else c=t+'0';
   s.PB(c);
   a/=b;
   if(a==0)break;     
 }while(true);   
 reverse(ALL(s));
 return s;    
       
}

string tobin(int a) {
       return tobase(a, 2);       
}

void norm(string& a, string& b) {
    int x = max(a.size(), b.size());
    while (a.size() < x) a = "0" + a;
    while(b.size() < x) b = "0" + b;
}


string add(string a, string b) {
         
       string ret;
       REP(i,a.size()) {
             if(a[i] == b[i]) ret.PB('0');
             else ret.PB('1');                          
       }
       return ret;       
}

void noz(string& a, string& b) {
       while(a[0] == '0') a.erase(a.begin());
       if(a.size() == 0) a = "0";
       while(b[0] == '0') b.erase(b.begin());
       if(b.size() == 0) b = "0";       
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("c-att1.out","w",stdout);
    
    vector<string> bins;
    
    REP(i,1000001) bins.PB(tobin(i));

    int cases; scanf("%d",&cases); 
    REP(k,cases) {
                 int n; scanf("%d",&n);
                 vector<int> a;
                 
                 REP(i,n) {
                          int tmp; scanf("%d",&tmp); a.PB(tmp);
                 }             
                 
                 string res=""; int r = -1;
                 
                 for(int i = 0; i < 1<<a.size(); i++) {
                       vector<int> x, y;
                       for(int j = 0; j < a.size(); j++) if(i & 1<<j) x.PB(a[j]); else y.PB(a[j]);
                       if(x.size() == 0 || y.size() == 0) continue;
                       string addx="0", addy="0"; int ax=0, ay=0;
                       REP(j,x.size()) norm(addx, bins[x[j]]),addx = add(addx, bins[x[j]]), ax+=x[j];
                       REP(j,y.size()) norm(addy, bins[y[j]]),addy = add(addy, bins[y[j]]), ay+=y[j];
                       norm(addx, addy);
                       noz(addx, addy);
                       if(addx == addy) { r = max(r, max(ax, ay)); }  
                 }
                 
                 printf("Case #%d: ", k + 1);
                 if(r == -1) printf("NO\n");
                 else printf("%d\n",r);
                 
    }
     
     return 0;
}
