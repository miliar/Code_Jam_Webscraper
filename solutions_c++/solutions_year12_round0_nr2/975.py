#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int main()
{
    freopen("B-large.in.","r",stdin);
    freopen("out.txt","w",stdout);
    int amm;
    scanf("%d",&amm);
    for (int i=1;i<=amm;i++)
    {
        int num,sur,qu;
        int str[105];
        scanf("%d%d%d",&num,&sur,&qu);
        qu*=3;
        for (int j=0;j<num;j++)
            scanf("%d",&str[j]);
        sort(str,str+num);
        printf("Case #%d: ",i);
        int ptr=0;
        int ans=0;
        if (qu==0)
        {
           printf("%d\n",num);
           continue;
        }
        if (qu==3)
        {
           for (int j=0;j<num;j++)
               if (str[j])ans++;
           printf("%d\n",ans);
           continue;       
        }
        while (ptr<num)
        {
              if (str[ptr]==0){ptr++;continue;}
              if (str[ptr]==1){ptr++;continue;}
              if (str[ptr]<qu-4){ptr++;continue;}
              if (str[ptr]==qu-4||str[ptr]==qu-3)
              {
                 if(sur){sur--;ans++;}
                 ptr++;
                 continue;
              }              
              else {ans++;ptr++;}          
        }
        printf("%d\n",ans);
    
    }
    return 0;   
}
