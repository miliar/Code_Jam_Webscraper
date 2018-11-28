#include<iostream>
using namespace std;
char a[5010][17];
bool f[17][128];
int L,D,N;
int main(){
      int i,j,k,ans,t,ca;
      char ch;
      bool flag;
      freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);
      scanf("%d%d%d",&L,&D,&N);
      for(i=0;i<D;i++) scanf("%s",a[i]);
      getchar();
      
      for(ca=1;ca<=N;ca++){
            t=-1;k=0;
            memset(f,false,sizeof(f));
            while((ch=getchar())!='\n'){
                  if(ch=='(') {t=0;continue;}
                  if(ch!='(' && ch!=')' && t!=-1) {f[k][ch]=true;continue;}
                  if(ch!='(' && ch!=')'){
                        f[k++][ch]=true;
                        t=-1;
                        continue;
                  }
                  if(ch==')') {t=-1;k++;}
            }
            ans=0;
            for(i=0;i<D;i++){
                  flag=true;
                  for(j=0;j<L;j++)
                        if(f[j][a[i][j]]==false){
                              flag=false;
                              break;
                        }
                  if(flag) ans++;
            }
            printf("Case #%d: %d\n",ca,ans);
      }
	return 0;
}