#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;


char mat[20],size;

inline int pw(int pw)
{
       int ans=1;
       for(int i=0;i<pw;i++)
       ans*=10;
       return ans;
}

inline bool convert(int nos)
{
   unsigned int mt[20];
   int j=0;  
   nfill(mt);  
    while(nos!=0)
      {
           mt[j++]=nos%10;           
           nos/=10;       
      }
    sort(mt,mt+j);
    reverse(mt,mt+j);

    int k;
    bool good = true;
    int i;
    
    
    for(k=0;k<strlen(mat);k++)
    {                      
            if((mat[k]-48)!=mt[k])
            {
               good = false;
               break;
            }
    }
    if(j>strlen(mat))
    if(mt[k]!=0)
    good=false;
    return good;
              
}


int main()
{

 int x,t;
 int no;

 S(t);
 FOR(x,t)
 {
      int no=0,i=0,num;

      cin>>mat;
      //cout<<x+1<<" "<<mat<<endl;
      size=0;
      int p = strlen(mat)-1;
      
      for(i=0;i<strlen(mat);i++)
      {
         no+=((mat[i]-48)*pw(p--));
      }        
      num = no;     
      //cout<<no<<endl;                      
      sort(mat,mat+strlen(mat));        
      reverse(mat,mat+strlen(mat));
      
      
      //size=i;   
      for(i=num+1;i<10000000;i++)
      {
          if(convert(i))
          break;                     
      }
     printf("Case #%d: %d\n",x+1,i);    
         
 }
return 0;
}
