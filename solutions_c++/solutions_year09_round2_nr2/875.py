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
    
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
    
    int t;
    sf("%d",&t);
    char num[25];
    int kase=1;
    while ( t--)
    {
    pf("Case #%d: " , kase++);
     sf("%s",num);
     char mc[25];
     strcpy(mc,num);
     int len = strlen(num);
     if ( next_permutation(num,num+len) )
        pf("%s\n",num);
     else {
          sort(num,num+len);
          //reverse(num,num+len);
          int i;
          for(i=0;num[i];i++)
           if ( num[i] != '0' ) br;
          pf("%c",num[i]);
          num[i] = '-';
          pf("0");
          for(i=0;num[i];i++)
           if( num[i] != '-' ) pf("%c",num[i]);
          pf("\n");
     }
     
    }
	return 0;
}
