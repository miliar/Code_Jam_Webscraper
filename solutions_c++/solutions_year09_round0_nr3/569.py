#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
vector<int>u[128];
char sen[]="welcome to code jam";
int main(){
      int i,len0,len,tp,j,T,ca,MOD,k,l;
      char a[510];
      int f[510][30];
      freopen("C-large.in","r",stdin);
      freopen("C-large.out","w",stdout);
      scanf("%d",&T);
      
      for(i=0;i<128;i++) u[i].clear();
      len0=strlen(sen);
      for(i=0;i<len0;i++) u[sen[i]].push_back(i);
      getchar();
      for(ca=1;ca<=T;ca++){
            gets(a);
            len=strlen(a);
            memset(f,0,sizeof(f));
            
            MOD=10000;
            for(i=0;i<len;i++){
                  //if(u[a[i]].size()==0) continue;
                  for(j=0;j<u[a[i]].size();j++){
                        l=u[a[i]][j];
                        if(l==0) {f[i][1]=1;continue;}
                        tp=0;
                        bool flag=false;
                        for(k=0;k<i;k++) if(f[k][l]){
                              tp=(tp+f[k][l])%MOD;
                              flag=true;
                        }
                        if(flag) f[i][l+1]=tp;
                  }
            }
            tp=0;
            for(i=0;i<len;i++) tp=(tp+f[i][len0])%MOD;
            printf("Case #%d: %04d\n",ca,tp);
      }
      return 0;
}