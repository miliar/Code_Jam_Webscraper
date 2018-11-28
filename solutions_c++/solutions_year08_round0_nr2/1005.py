#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)


int n,m,limit;

struct tp{
       int x,y;
} a[300],b[300];
int c1[24*60+100],c2[24*60+100];

bool compareab(tp a,tp b){
     if (a.x<b.x) return true;
     else return false;
}

int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,test,cases,t;
    cin>>test;
    cases=0;
    while (test){
         test--; cases++;
         scanf("%d\n",&limit);
         scanf("%d%d",&n,&m);
         foru(i,1,n) {
                     scanf("%d:%d",&j,&k);
                     a[i].x=j*60 + k;
                     scanf("%d:%d",&j,&k);
                     a[i].y=j*60 + k;
         }
         foru(i,1,m) {
                     scanf("%d:%d",&j,&k);
                     b[i].x=j*60+k;
                     scanf("%d:%d",&j,&k);
                     b[i].y=j*60 + k;
         }
         int na=0,nb=0;
         sort(a+1,a+n+1,compareab);
         sort(b+1,b+m+1,compareab);
         i=1; j=1;
         
         memset(c1,0,sizeof(c1));
         memset(c2,0,sizeof(c2));
         a[n+1].x=24*60+100;
         b[m+1].x=24*60+100;
         int can1=0,can2=0;
         foru(t,0,24*60){
            can1+=c1[t];
            can2+=c2[t];
            while (a[i].x==t){
               if (can1>0) can1--; 
               else na++; 
               c2[a[i].y + limit]++;
               i++;
            }           
            while (b[j].x==t){
               if (can2>0) can2--;
               else nb++;
               c1[b[j].y + limit]++;
               j++;
            }
         }
         printf("Case #%d: %d %d\n",cases,na,nb);
    }
    return 0;
}
