#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
int c[30][30],r[30][30];
char que[105];
char idx[10005];
//char use[10005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
		int i;
        memset(c,0,sizeof(c));
        memset(r,0,sizeof(r));
        char o[5];
        int a;
        scanf("%d",&a);
        for(i=0;i<a;i++)
        {
            scanf("%s",o);
            c[o[0]-'A'][o[1]-'A']=o[2]-'A';
            c[o[1]-'A'][o[0]-'A']=o[2]-'A';
        }
        int b;
        scanf("%d",&b);
        for(i=0;i<b;i++)
        {
            scanf("%s",o);
            r[o[0]-'A'][o[1]-'A']=1;
            r[o[1]-'A'][o[0]-'A']=1;
        }
        int h=0,e=0;
        int len;
        scanf("%d",&len);
        scanf("%s",idx);
        for(i=0;i<len;i++)
        {
            que[e++]=idx[i]-'A';
            while(h+1<e&&c[que[e-1]][que[e-2]]!=0)
            {
                char k=c[que[e-1]][que[e-2]];
                que[e-2]=k;
                e--;
            }
            for(int j=h;j<e-1;j++)
            {
                int a=que[j];
                int b=que[e-1];
                if(r[a][b]!=0)
                {
                    h=e=0;
                    break;
                }
            }
        }
        printf("Case #%d: [",++cas);
        for(i=h;i<e-1;i++)
            printf("%c, ",que[i]+'A');
		if(h!=e)
			printf("%c]\n",que[e-1]+'A');
		else
			printf("]\n");
    }
    return 0;
}
