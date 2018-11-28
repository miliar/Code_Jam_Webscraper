//#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)


int n,m;

struct tp{
       int x,y;
       } ask[200];

bool compareab(tp a, tp b){
     if (a.x<b.x) return true;
     else return false;
}

int ans[200];

int main(){
    freopen("cinput2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k;//,test,cases;
    
 //   cases=0;
//    scanf("%d",&test);
//    while (test){
  //        test--;
    //      cases++;
          scanf("%d",&n);
          int a,b,c;
          foru(i,1,n) {scanf("%d",&ask[i].x);
            ask[i].y=i;
          }
          sort(ask+1,ask+n+1,compareab);
          
          i=1;
          
//          6  -4
          
          a=2; b=6; j=1;
          ask[n+1].x=-1;
          while (1){
             j++;   
             c=(b*6 - 4*a) % 1000;
             if (c<0) c+=1000;   
             a=b; b=c;
             while (j==ask[i].x) {
                 k=ask[i].y;
                 ans[k]=(c-1+1000) % 1000;
                 i++;
                 if (i>n) break;
             }    
             if (i>n) break;
          }        
          foru(i,1,n){
             printf("Case #%d: ",i);
             if (ans[i]<100 && ans[i]>=10) printf("0");else
             if (ans[i]<10) printf("00");
             printf("%d\n",ans[i]);
          }
    //}
    return 0;
}
