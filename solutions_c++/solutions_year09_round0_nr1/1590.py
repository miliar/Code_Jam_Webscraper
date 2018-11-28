#include<stdio.h>
#include<string.h>

int l,d,n;
char s[5000][20],ss[1000];

int main()
{
    int i,j,k,kk;
    freopen("A-large.in","r",stdin);
    freopen("A.large.out","w",stdout);
    scanf("%d%d%d",&l,&d,&n);
    for(i=0;i<d;i++)
    scanf("%s",s[i]);
    for(i=1;i<=n;i++)
    {
                     scanf("%s",ss);
                     int h,l1,l2;
                     l1=strlen(ss);
                     h=0;
                     printf("Case #%d: ",i);
                     int ans=0;
                     int sss;
                     for(j=0;j<d;j++)
                     {
                                     h=0;
                                     sss=0;
                                     int o;
                                     for(k=0;k<l;k++)
                                     if(ss[h]!='(')
                                     {
                                                     if(ss[h]==s[j][k])
                                                     {
                                                                      sss++;
                                                                      h++;
                                                     }
                                                     else break;
                                     }
                                     else
                                     {
                                         o=0;
                                         for(h=h+1;ss[h]!=')';h++)
                                         {
                                                                 if(ss[h]==s[j][k]&&o==0)
                                                                 {
                                                                                        o=1;
                                                                                        sss++;
                                                                 }
                                         }
                                         if(o==0) break;
                                         h++;
                                     }
                                     if(sss==l) ans++;
                     }
                     printf("%d\n",ans);
    }
    return 0;
}
                                              
                                                                                       
                                                                                  
                                         
                                                                          
