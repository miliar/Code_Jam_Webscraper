// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}


string T;
int tt;
char r[1000];

struct uzol{
   string name;
   int left,right;
   double p;
   uzol(){}
   uzol(string x){ name=x; left=-1; right=-1; }
};

uzol u[10000];
int pu=0;

set<string> mam;

//(weight [feature tree tree])

int nacitaj(){
   char c=' '; while(c!='(') scanf("%c",&c);   
   int cu=pu;
   uzol &uu=u[pu]; pu++;
   uu.name="";
   double p; scanf("%lf",&p); uu.p=p;
   while(1){
      scanf("%c",&c);
      if(c==')'){ uu.left=-1; uu.right=-1; return cu; }
      if(isalpha(c)) { uu.name+=c; break;}
   }
   while(1){
      scanf("%c",&c); 
      if(isalpha(c)) uu.name+=c; else break;
   }

   uu.left=nacitaj();
   uu.right=nacitaj();

   while(1){ scanf("%c",&c); if(c==')') break; }
   return cu; 
}

double prejdi(int cu){   
   uzol uu=u[cu];
//   printf("%d %s %d %d %.5lf\n",cu,uu.name.c_str(),uu.left,uu.right,uu.p);
   if(uu.name=="") return uu.p;
   if(mam.count(uu.name)) 
      return uu.p* prejdi(uu.left); 
      else return uu.p* prejdi(uu.right);
}

void solve(){   
   int L; 
   scanf("%d\n",&L); //printf("%d\n",L);
   pu=0;
   //char c=' '; while(c!='(') scanf("%c",&c);
   nacitaj();
  
   int A; scanf("%d\n",&A); //printf("%d\n",A);
   while(A--){
      char ss[100];
      mam.clear();   
      scanf("%s",ss);
      int K; scanf("%d",&K);
      while(K--){ scanf("%s",ss); mam.insert(ss); }
      printf("%.8lf\n",prejdi(0));
   }
   

}

int main(){
  int pvs; scanf("%d\n",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:\n",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
