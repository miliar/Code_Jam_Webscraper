#include<cstdio>
#include<cstdio>
#include<cstring>

using namespace std;

char ch[200];
char update[50][4];
char del[50][3];
char st[200];
int p;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,t,n,m,len,k,mm=1;
    bool f;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",update[i]);
        }
        scanf("%d",&m);
        for(i=0;i<m;i++)
        {
            scanf("%s",del[i]);
        }
        scanf("%d",&len);
        scanf("%s",ch);
        p=0;
        for(i=0;i<len;i++)
        {
            st[p++]=ch[i];
            g:if(p>1)
            {
                for(j=0;j<n;j++)
                {
                    if((st[p-1]==update[j][0]&&st[p-2]==update[j][1])||(st[p-1]==update[j][1]&&st[p-2]==update[j][0]))
                    {
                        p-=2;
                        st[p++]=update[j][2];
                        goto g;
                    }
                }
                for(j=0;j<m;j++)
                {
                    for(k=p-2;k>=0;k--)
                    {
                        if((st[p-1]==del[j][0]&&st[k]==del[j][1])||(st[p-1]==del[j][1]&&st[k]==del[j][0]))
                        {
                            p=0;
                            goto g;
                        }
                    }
                }
            }
        }
        f=false;
        printf("Case #%d: [",mm++);
        for(i=0;i<p;i++)
        {
            if(f)
            {
                printf(", ");
            }
            f=true;
            putchar(st[i]);
        }
        printf("]\n");
    }
}
