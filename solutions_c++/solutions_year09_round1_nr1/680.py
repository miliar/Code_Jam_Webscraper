#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;

bool f[1000000];
char ts[100];

inline bool test(char *ts,int &base){
      int tp,i;
      memset(f,false,sizeof(f));
      while(1){
            tp=0;i=0;
            while(ts[i]){
                  tp+=(ts[i]-'0')*(ts[i]-'0');
                  i++;
            }
            if(tp==1) return true;
            if(f[tp]) return false;
            else f[tp]=true;
            itoa(tp,ts,base);
      }
}
int main(){
      int  cases,it,n,a[10],p,i;
      bool flag;
      freopen("A-small-attempt0.in","r",stdin);
      freopen("A-small.out","w",stdout);
      scanf("%d",&cases);
      getchar();
      for(it=1;it<=cases;it++){
            n=0;
            while(1){
                  scanf("%d",&a[n++]);
                  char ch;
                  ch=getchar();
                  if(ch=='\n' || ch==EOF) break;
            }
            p=2;
            while(1){
                  bool flag=true;
                  //sprintf(ts,"%d",p);
                  for(i=0;i<n;i++){
                        itoa(p,ts,a[i]);
                        if(!test(ts,a[i])){
                              flag=false;
                              break;
                        }
                  }
                  if(flag) break;
                  p++;
            }
            printf("Case #%d: %d\n",it,p);
      }

      return 0;
}
