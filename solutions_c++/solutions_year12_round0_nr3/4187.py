

#include<cstdio>
#include<vector>
#include<math.h>
#include<conio.h>
#include<queue>
#include<algorithm>
#include<cstring>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>
#include<stack>
#include<list>
#include<iostream>
#include<utility>

using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

int main(){int test,a,b,i,x,y,z,temp1,temp2,temp3,d,e,f,ans,pop=0;
freopen("C-small-attempt1.in","r",stdin);
freopen("C-small-attempt1.out","w",stdout);
scanf("%d",&test);
while(test--) {ans=0;
                 	
                 scanf("%d%d",&a,&b);
                 if(b<=9) ans=0; 
                 else { for(i=a;i<=b;i++)
                  { x=i;temp1=temp2=temp3=0;
                          if(x<=99)
                        { temp1=x%10;x/=10;
                          temp1=temp1*10+x;
                         if(temp1>i && temp1<=b) ans++;
                         }
                     x=i;
                     if(x>=100) {
                     d=x%10;x/=10;
                     e=x%10;x/=10;
                     f=x;
                     temp2=100*e+10*d+f;
                     temp3=100*d+10*f+e; 
                     
                     if(temp2>i && temp2<=b)  ans++;
                     if(temp3>i && temp3<=b)  ans++;
                     }   
                    }
                    }
              
                 printf("Case #%d: %d\n",++pop,ans);
              }

  getch();
  return 0;
  }
