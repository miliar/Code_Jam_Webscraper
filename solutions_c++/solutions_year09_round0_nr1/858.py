#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int L,D,N;
char Dic[5001][20];
bool U[5001],Set[30];
int main()
{
    //freopen("a.txt","r",stdin);
    //freopen("b.txt","w",stdout);
    scanf("%d%d%d",&L,&D,&N);
    for (int i=1;i<=D;i++)
        scanf("%s",Dic[i]+1);
    for (int i=1;i<=N;i++)
    {
        scanf("%*c");
        memset(U,0,sizeof(U));
        for (int p=1;p<=L;p++)
        {
            char ch;
            scanf("%c",&ch);
            if (ch=='(')
            {
                        for (int j='a';j<='z';j++) Set[j-'a'+1]=false;
                        scanf("%c",&ch);
                        while (ch!=')')
                        {
                              Set[ch-'a'+1]=true;
                              scanf("%c",&ch);
                        }
                        for (int j=1;j<=D;j++)
                            if (!Set[Dic[j][p]-'a'+1])
                               U[j]=true;
            }
            else
                for (int j=1;j<=D;j++)
                    if (Dic[j][p]!=ch)
                       U[j]=true;
        }
        int ans=0;
        for (int j=1;j<=D;j++)
            if (!U[j])
               ans++;
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
