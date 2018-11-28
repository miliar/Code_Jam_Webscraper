#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
#define FS first
#define SD second

/*
tree ::= (weight [feature tree tree])
weight is a real number between 0 and 1, inclusive
feature is a string of 1 or more lower case English letters
*/
struct tree{
   double w;
   string f;
   tree *L;
   tree *R;
};

char line[102400];

tree * parseT(stringstream &s,bool naw){
   tree * T = new tree();
   if(naw){
      while(true){
         char c;
         s>>c;
         if(c=='(') break;
      }
   }
   s>> (T->w);

   char c;
   while(true){
      s>>c;
      if(c==')' || (c>='a' && c<='z') ) break; 
   }
   if(c==')') return T;
   T->f+=c;
   
   while(true){
      s>>c;
      if(c=='(') break;
      if(c<'a' || c>'z') break;
      T->f+=c;
   }
   if(c=='(') T->L =parseT(s,false);
   else T->L =parseT(s,true);
   T->R = parseT(s,true);
   return T;
}
double go(tree * T,  vector<string> f){
   if(T->f==""){
      return T->w;
   }
   else{
      FOR(i,0,SZ(f)){
         if(f[i]==T->f) return go(T->L,f)*(T->w);
      }
      return go(T->R,f)*(T->w);
   }

}
int main(){
   int T;scanf("%d",&T);
   FORE(test,1,T){
      int k;
      scanf("%d\n",&k);
      string ss;
      FOR(i,0,k){
         fgets(line,102400,stdin);
         ss += string(line);
      }
      
      stringstream s(ss);
      string sk;

      tree * T = parseT(s,true); 
      
      int n;scanf("%d\n",&n);
      printf("Case #%d:\n",test);
      FOR(i,0,n){
         fgets(line,102400,stdin);
         ss = string(line);
         stringstream in(ss);
         in>>ss;
         int k;
         in>>k;
         vector<string> c;
         FOR(j,0,k){
            string f;
            in>>f;
            c.push_back(f);
         }
         printf("%lf\n",go(T,c));
      }
   }
   
}
