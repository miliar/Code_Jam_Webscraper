#include<stdio.h>
#include<stdlib.h>

char a[300]={"y zqeeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"}
,b[300]={"a qzooour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"}
,c1[32][105],c2[32][105];
int n;

int main(){
    int i,j,k;
    freopen("1.in","r",stdin);
    freopen("1.txt","w",stdout);
    scanf("%d",&n);
    getchar();
    for(i=1;i<=n;i++)
    {
        gets(c1[i]);
        for(j=0;c1[i][j]!=0;j++)
        {
            for(k=0;a[k]!=c1[i][j];k++);
            c2[i][j]=b[k];
        }
        printf("Case #%d: %s\n",i,c2[i]);
    }
    
    scanf(" ");
    return 0;
    }
