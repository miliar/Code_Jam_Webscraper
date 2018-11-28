#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int n,t,s,p,count1,count2,num1,num2;  //count1 = explicit case, count2 = check-with-S case
    int a;  //a = total point
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d%d%d",&t,&s,&p);
        count1=0;
        count2=0;
        num1=p*3-2;
        if(num1<p) num1=p;
        num2=p*3-4;
        if(num2<p) num2=p;
        for(int j=0;j<t;j++)
        {
            scanf("%d",&a);
            if(a>=num1) count1++;
            else if(a>=num2) count2++;
        }
        if(count2>s) count1+=s;
        else count1+=count2;
        printf("Case #%d: ",i+1);
        printf("%d\n",count1);
    }
    //system("pause");
}
