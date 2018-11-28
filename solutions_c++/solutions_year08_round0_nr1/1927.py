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

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define ALL(i) i.begin(),i.end()
#define PB push_back

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int isin(string s, vector<string> ss)
{
 REP(i, ss.size()) if(ss[i] == s) return i;
 return -1;    
}

void printvec(vi a)
{
  printf("vecteur : ");
  REP(i,a.size()) printf("%d ",a[i]);
  printf("\n\n");     
}

int main()
{

freopen("A-large.in","r",stdin);
freopen("output.out","w",stdout);


   int n,s,q;
   string ss;
   getline(cin,ss);
   sscanf(ss.c_str(),"%d",&n);
   
   REP(k,n)
   {
    getline(cin,ss);
    vector<string> moteur,req;
    sscanf(ss.c_str(),"%d",&s);
    REP(v,s)
    {
      getline(cin,ss);
      moteur.PB(ss);        
    }
    getline(cin,ss);
    sscanf(ss.c_str(),"%d",&q);
    REP(v,q)
    {
      getline(cin,ss);
      req.PB(ss);      
    }
    
    /*
    printf("moteurs : ");
    REP(i,moteur.size()) cout<<moteur[i]<<" ";
    printf("\n");
    printf("Req = ");
    REP(i,req.size()) cout<<req[i]<<" ";
    cout<<endl;
    */
    if(req.size() == 0) {printf("Case #%d: 0\n",k+1);continue;}
    int max=-10,maxi=0;
    int c = 0;
    int curj = 0;
    string curm;
    while(true)
    {
   // printf("curj = %d\n",curj);
    vi dist(moteur.size(),-1);
    vi occ(moteur.size(),0);
    REP(i,moteur.size())
    {
     FOR(j,curj,req.size())
     {
       if(moteur[i] == req[j]) { occ[i]++; dist[i] = j; break; }                 
     }                    
    }
    //printvec(dist);
    max=-1;maxi=0;
    
    bool isok = false;
    REP(i,occ.size()) if(occ[i] == 0) { isok = true; break;}
    if(isok) {printf("Case #%d: %d\n",k+1,c);break;}
    
    REP(i,dist.size()) if(max<dist[i] && moteur[i]!=curm) { max = dist[i]; maxi = i; }
    curm = moteur[maxi];
   // cout<<curm<<" "<<c<<endl;
    if(max == req.size()-1) {
           if(curm==req[req.size()-1])c++;
           printf("Case #%d: %d\n",k+1,c);break;
           
           }
    curj = max;
    
    c++;
    }
    
    
    
    
   }
   
   
   //getchar();
   return 0;
}
