#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <stack>
#define maxn 1000000007
#define VI vector<int>
#define VS vector<string>
#define MSI map<string,int>
#define N 2100
  using namespace std;
  int len,s,r,tim,n,tot;
  struct edge{
     int x,y,w;
  }t[N];
void ins(int x,int y,int k){
  t[++tot].w=k;
  t[tot].x=x;
  t[tot].y=y;
}
int cmp(const void *x, const void *y){
  return ((edge *)x)->w -((edge *)y)->w;
}
int main(){
  freopen("a.in","r",stdin);freopen("a.out","w",stdout);
  int i,j,k,x,y,yy;
  int tt,tc;
  double rem,tem,runt,walkt,sum,intlen;
  scanf("%d",&tc);
  for(tt=1;tt<=tc;tt++){
     printf("Case #%d: ",tt);
     scanf("%d%d%d%d%d",&len,&s,&r,&tim,&n);
     tot=0;
     yy=0;
     for(i=1;i<=n;i++){
        scanf("%d%d%d",&x,&y,&k);
        ins(yy,x,0);
        ins(x,y,k);
        yy=y;
     }
     ins(yy,len,0);
     qsort(t+1,tot,sizeof(edge),cmp);   
     rem=1.0*tim;
     sum=0.0;
     for(i=1;i<=tot;i++){
        intlen=1.0*(t[i].y-t[i].x);
        runt=intlen/(t[i].w+r);
        if(runt<=rem){
           rem-=runt;
           sum+=runt;
        }
        else{
           sum=sum+rem+(intlen-rem*(t[i].w+r))/(t[i].w+s);
           rem-=rem;
        }
        //if(tt==1)cout<<intlen<<' '<<t[i].w<<' '<<rem<<' '<<sum<<endl;
     }
    
     printf("%0.8f\n",sum);
  }     
     
  
  return 0;
}
