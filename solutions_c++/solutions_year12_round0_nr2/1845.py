#include<stdio.h>
using namespace std;
int main()
{
    freopen("F:\\B-large.in","r",stdin);
    freopen("F:\\file4.txt","w+",stdout);
    int n,T,S,P,a[200],i=0,j=0,sum=0,possible=0;
    char ch;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
                    sum=0;
                    possible=0;
                    scanf("%d %d %d",&T,&S,&P);
                    for(j=0;j<T;j++)
                    {
                                    scanf("%d",&a[j]);
                                    if(a[j]>3*P-3)
                                    {
                                                  sum+=1;
                                    }
                                    if((a[j]>=3*P-4)&&(a[j]<=3*P-3)&&(P!=1))
                                    {
                                                   possible+=1;
                                    }               
                    }
                    if(possible<S){S=possible;}
                    sum=sum+S;
                    printf("Case #");printf("%d",i+1);printf(": ");printf("%d\n",sum);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
    
