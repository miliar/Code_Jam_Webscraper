#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int c,d,n;
char com[3];
char oppo[3];
char str[105];
int j,a,b,w;
int o[100];
int map1[100][100];
int map2[100][100];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("data2.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        memset(map1,-1,sizeof(map1));
        memset(map2,0,sizeof(map2));
        for(j=0; j<=26; j++)
        {
            o[j]=-1;
        }
        scanf("%d",&c);
        for(j=1; j<=c; j++)
        {
            scanf("%s",com);
            a=com[0]-'A';
            b=com[1]-'A';
            w=com[2]-'A';
            map1[a][b]=w;
            map1[b][a]=w;
        }
        scanf("%d",&d);
        for(j=0; j<d; j++)
        {
            scanf("%s",oppo);
            a=oppo[0]-'A';
            b=oppo[1]-'A';
            map2[a][b]=map2[b][a]=1;
        }
        int top=0;
        int str1[105];
        scanf("%d",&n);
        scanf("%s",str);
        for(j=0; j<n; j++)
        {
            str1[top]=str[j]-'A';
            if(!top)
            {
                top++;
                continue;
            }
            if(map1[str1[top]][str1[top-1]]!=-1)
            {
                str1[top-1]=map1[str1[top]][str1[top-1]];
                top--;
            }
            else
            {
                for(int k=0; k<top; k++)
                {
                    if(map2[str1[k]][str1[top]])
                    {
                        top=-1;
                        break;
                    }
                }
            }
            top++;
        }

        printf("Case #%d: [",i);
        for(j=0; j<top; j++)
        {
            if(j!=top-1)
            {
                printf("%c, ",str1[j]+'A');
            }
            else
            {
                printf("%c",str1[j]+'A');
            }

        }
        printf("]\n");
    }
    return 0;
}
