#include<cstdio>
#include<cstring>
#include<cmath>
#include<map>
#include<string>
using namespace std;
int T, C, D, N, M;
int G1[26+2][26+2], G2[26+2][26+2];
char data[100+3], ans[100+3];

void getin()
{
    char buf[5];
    memset(G1,-1,sizeof(G1));
    memset(G2,-1,sizeof(G2));
    scanf("%d",&C);
    for (int i=1;i<=C;i++)
    {
        scanf("%s",buf);
        int x=buf[0]-'A'+1;
        int y=buf[1]-'A'+1;
        int z=buf[2]-'A'+1;
        G1[x][y]=G1[y][x]=z;
    }
    scanf("%d",&D);
    for (int i=1;i<=D;i++)
    {
        scanf("%s",buf);
        int x=buf[0]-'A'+1;
        int y=buf[1]-'A'+1;
        G2[x][y] = G2[y][x] = 1;
    }
    scanf("%d",&N);
    scanf("%s",data+1);
}

void work()
{
    M=0;
    for (int i=1;i<=N;i++) 
    {
        M++;
        ans[M]=data[i];
        if (M>1 && G1[ans[M]-'A'+1][ans[M-1]-'A'+1] > -1)
        {
            int z=G1[ans[M]-'A'+1][ans[M-1]-'A'+1];
            M--;
            ans[M]=(char)(z+'A'-1);
       //     printf("%d:%d\n",i,M);
            continue;
        }
        else
        {
            for (int j=1;j<=M-1;j++) if (G2[ans[M]-'A'+1][ans[j]-'A'+1] > -1)
            {
                M=0;
                break;
            }
        }
     //   printf("%d:%d\n",i,M);
    }
    if (M==0) { printf("[]\n"); return; }
    printf("[");
    for (int i=1;i<M;i++) printf("%c, ",ans[i]);
    printf("%c]\n",ans[M]);
}

int main()
{
//    freopen("yy.in","r",stdin);
//    freopen("yy.out","w",stdout);
//    freopen("B-small-attempt2.in","r",stdin);
//    freopen("B-small-attempt2.out","w",stdout);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);    
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        printf("Case #%d: ",ii);
        getin();
        work();
    }
    return 0;
}
