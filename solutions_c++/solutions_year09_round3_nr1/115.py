#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf

int main() {
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    int t;
    sf("%d",&t);
    int kase=1;
    while ( t--)
    {
     char num[100];
     sf("%s",num);
     int val[300];
     fill(val,val+300,-1);
     int i;
     int b;
     int dig=0;
     val[ num[0] ] = 1;
     for(i=1; num[i];i++)
      if ( val[ num[i] ] == -1 ) 
       {  
           val[ num[i] ] = dig; 
           dig++; 
           if ( dig == 1 ) 
           dig=2;
       }
      b=0;
      for(i=0;i<300;i++) if ( val[i] != -1 ) b++;
     
      if  ( b==1 ) b=2;
      int len = strlen(num);
      long long prod=1;
      long long ans=0;
      for(i=len-1;i>=0;i--)
       ans = ans + val[ num[i] ]*prod, prod = prod*b;
      pf("Case #%d: ",kase++);
      cout<<ans<<endl;
    }
	return 0;
}
