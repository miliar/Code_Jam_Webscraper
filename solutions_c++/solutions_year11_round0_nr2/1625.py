#include <stdio.h>
#include <stack>
#include <queue>
using namespace std;

char map[50][50];
char map1[50][50];
char str[500];
char a[500];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,T,n,c,d,up,cnt;
    scanf("%d",&T);
    cnt=1;
    while(T--)
    {
        memset(map,0,sizeof(map));
        memset(map1,0,sizeof(map1));
        scanf("%d",&c);
        for (i=0;i<c;i++)
        {
            scanf("%s",str);    
            map[str[0]-'A'][str[1]-'A']=str[2];
            map[str[1]-'A'][str[0]-'A']=str[2];
        }
        scanf("%d",&d);          
        for (i=0;i<d;i++)
        {
            scanf("%s",str);
            map1[str[0]-'A'][str[1]-'A']=1;
            map1[str[1]-'A'][str[0]-'A']=1;
        }
        scanf("%d",&n);
        scanf("%s",str);
        up=0;
        for (i=0;i<n;i++)
        {
            a[up]=str[i];
            if (up==0) 
            {
                up++;
                continue;
            }
            if (map[a[up]-'A'][a[up-1]-'A']>='A' && map[a[up]-'A'][a[up-1]-'A']<='Z')
            {
                a[up-1]=map[a[up]-'A'][a[up-1]-'A'];
            }
            else 
            {
                 for (j=0;j<up;j++)
                 {
                     if (map1[a[j]-'A'][a[up]-'A']==1) break;    
                 }
                 if (j<up)
                 {
                     up=0;
                     continue;   
                 }
                 up++;
            }
        }
        printf("Case #%d: [",cnt++);
        if (up==0)
        {
            printf("]\n");          
            continue;
        }
        for (i=0;i<up-1;i++)
        {
            printf("%c, ",a[i]);    
        }
        printf("%c]\n",a[i]);
    }
}
