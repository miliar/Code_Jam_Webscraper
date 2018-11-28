#include<stdio.h>
#include<stdlib.h>

int t,n,p,s,a[50],co,s1;

int main(){
    int i,j,k;
    freopen("1.in","r",stdin);
    freopen("1.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&n,&s,&p);
        co=s1=0;
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[j]);
            if(a[j]/3>=p)co++;
            else
            {
                if(a[j]%3==0)
                {
                    if(a[j]/3+1>=p && a[j])s1++;
                }else if(a[j]%3==1){
                    if(a[j]/3+1>=p)co++;
                }else{
                    if(a[j]/3+1>=p)co++;
                    else if(a[j]/3+2>=p)s1++;
                }
            }
//            printf("[%d,%d]",co,s1);
        }
        if(s1>=s)printf("Case #%d: %d\n",i,co+s);
        else printf("Case #%d: %d\n",i,co+s1);
    }
    
    scanf(" ");
    return 0;
    }
