#include <iostream>

using namespace std;

const int size=500;
char mm[size][size];
char xx[size][size];


void init()
{
    memset(mm,-1,sizeof(mm));
    memset(xx,0,sizeof(xx));
    char ss[10];
    int n;
    scanf("%d",&n);
    while(n--)
    {
        scanf(" %s",ss);
        int a=ss[0]-'A';
        int b=ss[1]-'A';
        int c=ss[2]-'A';
        mm[a][b]=mm[b][a]=c;
    }
    scanf("%d",&n);
    while(n--)
    {
        scanf(" %s",ss);
        int a=ss[0]-'A';
        int b=ss[1]-'A';
        int c=ss[2]-'A';
        xx[a][b]=xx[b][a]=1;
    }
}
char ans[size];
int ansnum;
char ss[size];
int  len;
void getans()
{
    ansnum=0;
    scanf("%d",&len);
    scanf(" %s",ss);

    for(int i=0;i<len;i++)
    ss[i]-='A';

    ans[ansnum++]=ss[0];

    for(int i=1;i<len;i++)
    {
        ans[ansnum]=ss[i];
        if(ansnum==0)
        {
            ansnum++;
            continue;
        }



        int a=ans[ansnum];
        int b=ans[ansnum-1];

        if(mm[a][b]!=-1)
        {
            ans[ansnum-1]=mm[a][b];
            continue;
        }
        ansnum++;

        for(int j=0;j<29;j++)
        if(xx[j][a]==1)
        {
            bool flag=false;
            for(int k=0;k<ansnum-1;k++)
            if(ans[k]==j)
            {
                flag=true;
                break;
            }
            if(flag)
            {
                ansnum=0;
                break;
            }
        }

    }
}
void print(int ttt)
{
    printf("Case #%d: [",ttt);
    if(ansnum>0)
    printf("%c",ans[0]+'A');
    for(int i=1;i<ansnum;i++)
    printf(", %c",ans[i]+'A');
    printf("]\n");
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        init();
        getans();
        print(i);
    }
    return 0;
}
