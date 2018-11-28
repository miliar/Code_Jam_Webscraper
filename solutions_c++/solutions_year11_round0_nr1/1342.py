#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))

int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    int n; scanf("%d",&n);
    int p1=1,p2=1,t1=0,t2=0;
    FOR(i,0,n){
      int x; char s[10]; 
      scanf("%s%d",s,&x);
      if (s[0]=='O'){
        int dd = abs(x-p1)+1;
        p1=x;
        if (t1+dd>t2) t1+=dd;
        else t1=t2+1;
      }else{
        int dd = abs(x-p2)+1;
        p2=x;
        if (t2+dd>t1) t2+=dd;
        else t2=t1+1;
      }
    }
    printf("Case #%d: %d\n",ca,max(t1,t2));
  }
  return 0;
}
