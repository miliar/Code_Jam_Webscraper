#include<stdio.h>
#include<string.h>
int ti,tn,i,j,k;
char temp,str[50];
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tn);
    for (ti=1;ti<=tn;ti++)
    {
        scanf("%s",str);
        printf("Case #%d: ",ti);
        for (i=0;str[i+1];i++)
            if (str[i]<str[i+1]) break;
        if (!str[i+1])
        {
            for (j=i;str[j]=='0';j--);
            printf("%c0",str[j]);
            for (k=j+1;k<=i;k++) printf("0");
            for (j--;j>=0;j--) printf("%c",str[j]);
            printf("\n");
        }
        else
        {
            for (i=strlen(str)-2;i>=0;i--)
                if (str[i]<str[i+1]) break;
            for (k=strlen(str)-1;k>i;k--)
                if (str[k]>str[i]) break;
            for (j=k-1;j>i;j--)
                if (str[j]>str[i]&&str[j]<str[k]) k=j;
            temp=str[i];
            str[i]=str[k];
            str[k]=temp;
            for (j=i+1,k=strlen(str)-1;j<k;j++,k--)
            {
                temp=str[j];
                str[j]=str[k];
                str[k]=temp;
            }
            printf("%s\n",str);
        }
    }
    return 0;
}
