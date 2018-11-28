
#include<stdio.h>
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
int arr[3];
int S,P;
void check(int total) {int i;
for(i=P;i<9;i++) { if(P+P+P==total) return;
                   if(P+P+P+1==total) return;
                   if(P+P+1+P+1==total) return;
                   if(P+P+1+P+2==total && S>0) {S--; return;}
                   if(P+P+2+P+2==total && S>0) {S--; return;}
                 }
                  }
int main(){int T,j,N,i,total,ans=0,temp,flag,pop=0;
freopen("B-small-attempt1.in","r",stdin);
freopen("B-small-attempt1.out","w",stdout);
scanf("%d",&T);
while(T--) { ans=temp=0;
scanf("%d%d%d",&N,&S,&P);
for(i=0;i<N;i++)
scanf("%d",&arr[i]);
for(i=0;i<N;i++)
 {total=arr[i];flag=0;
  if(P>=2) {
  if(P-2+P-2+P==total && S>0) {flag=1;S--;ans++; continue;}
  if(P-2+P-1+P==total && S>0) {flag=1;S--;ans++; continue;}
  if(P-1+P-1+P==total) {flag=1;ans++; continue;}
  if(P-1+P+P==total) {flag=1;ans++; continue;}
}
 if(total > 3*(P-1) && flag!=1) {flag=1;ans++; check(total);continue;}
     
      }
 
  printf("Case #%d: %d\n",++pop,ans);
}
  getch();
  return 0;
  }
