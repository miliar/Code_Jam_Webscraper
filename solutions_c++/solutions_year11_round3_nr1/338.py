#include<iostream>
using namespace std;
int T,n,m;
char ch[100][100];
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j,k;
    bool pd=0;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
                      memset(ch,' ',sizeof(ch));
                      pd=1;
                      scanf("%d%d",&n,&m);
                      for(j=1;j<=n;j++)scanf("%s",ch[j]);
                      //printf("yes");
                      for(j=1;j<=n;j++)
                      for(k=0;k<m;k++){
                                        if(ch[j][k]=='#'){
                                                          if(ch[j+1][k]!='#'||ch[j+1][k+1]!='#'||ch[j][k+1]!='#')
                                                          {pd=0;break;}
                                                          else {
                                                               ch[j][k]='/';
                                                               ch[j+1][k]='\\';
                                                               ch[j][k+1]='\\';
                                                               ch[j+1][k+1]='/';
                                                               }
                                                          }
                                        if(pd==0)break;
                                        }
                      if(pd==0){printf("Case #%d:\nImpossible\n",i);}
                      else {
                           printf("Case #%d:\n",i);
                           for(j=1;j<=n;j++){
                           for(k=0;k<m;k++)printf("%c",ch[j][k]);
                           printf("\n");}
                           }
                      }
    //while(1);
}
