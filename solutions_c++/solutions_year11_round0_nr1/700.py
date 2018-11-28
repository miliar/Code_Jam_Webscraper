#include <iostream>

using namespace std;

const int size=110;;
int n;
int orange[size];
int oranum;
int blue[size];
int bluenum;
char op[size];
int opnum;
void init()
{
    oranum=bluenum=opnum=1;
    orange[0]=blue[0]=1;

    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        char c;
        int a;
        scanf(" %c %d",&c,&a);
        op[opnum++]=c;

        if(c=='O')
        orange[oranum++]=a;
        else
        blue[bluenum++]=a;
    }

    for(int i=bluenum-1;i>=1;i--)
    {
        blue[i]-=blue[i-1];
        if(blue[i]<0)
        blue[i]=-blue[i];
    }
    for(int i=oranum-1;i>=1;i--)
    {
        orange[i]-=orange[i-1];
        if(orange[i]<0)
        orange[i]=-orange[i];
    }
}
int ans;
void getans()
{
    ans=0;
    oranum=bluenum=1;
    for(int i=1;i<opnum;i++)
    {
        ans++;
        if(op[i]=='B')
        {
            orange[oranum]=orange[oranum]-1-blue[bluenum];
            ans+=blue[bluenum++];
        }
        if(op[i]=='O')
        {
            blue[bluenum]=blue[bluenum]-1-orange[oranum];
            ans+=orange[oranum++];
        }

        if(orange[oranum]<0)
        orange[oranum]=0;

        if(blue[bluenum]<0)
        blue[bluenum]=0;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        init();
        getans();
        printf("Case #%d: %d\n",i,ans);

    }
    //system("pause");
    return 0;
}
