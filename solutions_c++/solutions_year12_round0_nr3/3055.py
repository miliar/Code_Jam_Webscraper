#include<stdio.h>
#include<stdlib.h>
#include<string.h>
bool chk(int a,int b)
{
    char a0[8],tmp;
    itoa(a,a0,10);
    for(int i=0;i<strlen(a0);i++)
    {
        tmp=a0[0];
        for(int j=0;j<strlen(a0)-1;j++)
            a0[j]=a0[j+1];
        a0[strlen(a0)-1]=tmp;
        if(atoi(a0)==b)
            return true;
    }
    return false;
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int t,count,i,j,k,tmpnum,a,b;
    char tmp;
    int number[8],cnum,m;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        count=0;
        scanf("%d%d",&a,&b);
        for(int j=a;j<b;j++)
            for(int k=j+1;k<=b;k++)
                if(chk(j,k))
                    count++;
        printf("Case #%d: ",i+1);
        printf("%d\n",count);
    }
    //system("pause");
}
