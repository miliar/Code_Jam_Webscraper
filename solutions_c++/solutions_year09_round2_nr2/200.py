#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int c,o,i,j,k,g[10],len;
    char str[128];
    scanf("%d",&c);
    for(o=1;o<=c;o++)
    {
        printf("Case #%d: ",o);
        scanf("%s",str);
        len=strlen(str);
        for(k=len-1;k>=0;k--)
        {
            memset(g,0,sizeof(g));
            for(i=k;i<len;i++)
                g[str[i]-'0']++;
            for(j=str[k]-'0'+1;j<10;j++)
                if(g[j])
                    break;
            if(j<10)
            {
                str[k]=j+'0';
                g[j]--;
                for(i=k+1;i<len;i++)
                    for(j=0;j<10;j++)
                        if(g[j])
                        {
                            g[j]--;
                            str[i]=j+'0';
                            break;
                        }
                break;
            }
        }
        if(k<0)
        {
            memset(g,0,sizeof(g));
            for(i=0;i<len;i++)
                g[str[i]-'0']++;
            for(j=1;j<10;j++)
                if(g[j])
                    break;
            str[0]=j+'0';
            g[j]--;
            str[1]='0';
            for(i=2;i<=len;i++)
                for(j=0;j<10;j++)
                    if(g[j])
                    {
                        g[j]--;
                        str[i]=j+'0';
                        break;
                    }
            str[len+1]='\0';
            printf("%s\n",str);
        }
        else
            printf("%s\n",str);
    }
    return 0;
}

