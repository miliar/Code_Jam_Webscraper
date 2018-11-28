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


int main()
{
   
    freopen("A-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
   
   string s;
   getline(cin, s);
   int cases; sscanf(s.c_str(),"%d",&cases);
   
   REP(k,cases) {
           getline(cin,s);
           stringstream st; 
           st<<s;
           int n;
           st>>n;
           string type; vector<int> a, oo, bb;
           string tmp;
           REP(i,n) {
               char c; int x;
               st>>c>>x;
               a.PB(x);
               type.PB(c);              
               if(c == 'O') oo.PB(x);
               else if(c == 'B') bb.PB(x);
           }              
           
           int posO=1, posB=1, total = 0, lastO = 0, lastB = 0;
           REP(i,type.size()) {
                 char p = type[i];
                 if(p == 'O') {
                    int v = abs(posO - a[i]);
                    v = max( v-lastB, 0) + 1;
                    lastO += v;
                    total+=v;
                   // printf("v = %d  totalO = %d\n",v,total);
                    posO = a[i];
                    lastB = 0;

                 } else if(p == 'B') {
                    int v = abs(posB - a[i]);
                    v = max( v-lastO, 0) + 1;
                    lastB += v;
                    total+=v;
                   // printf("v = %d  totalB = %d\n",v,total);
                    posB = a[i];
                    lastO = 0;                      
                 }                
           }
           printf("Case #%d: %d\n", k+1,total);
           
   }             
     return 0;
}
