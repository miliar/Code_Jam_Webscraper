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
   
    freopen("C-small-attempt0.in","r",stdin);
   freopen("c.out","w",stdout);
   
     int t;
     scanf("%d",&t);
     REP(v,t) {           
        int r,k,n;
        scanf("%d %d %d",&r,&k,&n);

        vector<int> ns;
        REP(i,n) {
                 int tmp;
                 scanf("%d",&tmp); ns.PB(tmp);         
        }               
       //REP(i,ns.size()) printf("%d ",ns[i]);
        
        int count = 0;
        for(int i = 0; i < r; i++) {
             int sum = 0;
             vector<int> fill;
             for(int j = 0; j < ns.size(); j++) {
                    int cur = ns[j];
                    if(sum + cur <= k) {
                        ns.erase(ns.begin() + j);
                        fill.PB(cur);
                        j--;         
                        sum+=cur; 
                        count+=cur;
                        if(ns.size() == 0)break;
                        //printf("sum=%d\n",sum); getchar();
                    }       
                    else {  sum = 0; REP(e,fill.size()) ns.PB(fill[e]); fill.clear(); break; }
             }             
            if(fill.size() != 0) REP(e,fill.size()) ns.PB(fill[e]);
        }
        printf("Case #%d: %d\n",v+1, count);
     }

     return 0;
}
