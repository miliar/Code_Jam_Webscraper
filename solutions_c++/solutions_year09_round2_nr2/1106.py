#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char dig[25];
int T;

int main()
{
    int i,j,k,t,s;
    freopen("B-large(1).in","r",stdin);
    freopen("B.small.out","w",stdout);
    scanf("%d",&T);
    
    for(t=1;t<=T;t++)
    {
                     scanf("%s",dig);
                     printf("Case #%d: ",t);
                     int l=strlen(dig);
                       for(s=l-1;s>=0;s--)
                             if(dig[s]!='0') break;
                     for(i=s;i>0;i--)
                     if(dig[i]>dig[i-1])
                     break;
                     if(i==0)
                     {
                           
                            // printf("%d\n",s);
                             
                             printf("%c0",dig[s]);
                             for(j=l-1;j>s;j--)
                             printf("0");
                             for(j=s-1;j>=0;j--)
                             printf("%c",dig[j]);
                             printf("\n");
                     }
                     else
                     {
                         int o=1;
                        // printf("%d\n",s);
                         for(k=s-1;k>=0&&o;k--)
                           for(j=l-1;j>k;j--)
                           if(dig[j]>dig[k])
                           {
                                              o=0;                       
                                            break;
                                          
                           }
                           k++;
                          // printf("%d %d\n",j,k);
                           char c;
                           {
                                c=dig[j];
                                dig[j]=dig[k];
                                dig[k]=c;
                           }
                           sort(dig+k+1,dig+l);
                           printf("%s\n",dig);
                           
                         
                         
                        
                     }
    }
    return 0;
}
                         
