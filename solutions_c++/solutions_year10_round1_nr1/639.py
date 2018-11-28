/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#define maxv(a,b) (a>=b ? a : b)
#define minv(a,b) (a<=b ? a : b)
using namespace std;
char g[55][55];
int n,k,Case;
void down()
{
    for (int i=n;i>=1;i--) 
        for (int j=1;j<=n;j++) {
            if (g[i][j]=='.') continue;
            int di=i;
            while (1) {
                if (g[di+1][j]=='.') di++;
                else break;
                }
            if (di!=i) {
                g[di][j]=g[i][j];
                g[i][j]='.';
                }
            }
}
void check()
{
    int flag[55][55];
    bool a=false,b=false;
    memset(flag,0,sizeof(flag));
    for (int i=1;i<=n;i++) 
        for (int j=1;j<=n;j++) {
            if (g[i][j]=='.') continue;
            int di=i,dj=j,k=1;
            while (1) {
                if (g[di+1][j]==g[i][j] && di+1<=n) {
                    k++;
                    di++;
                    }
                else break;
                }
            flag[i][j]=maxv(flag[i][j],k);
            k=1;
            while (1) {
                if (g[i][dj+1]==g[i][j] && dj+1<=n) {
                    k++;
                    dj++;
                    }
                else break;
                }
            flag[i][j]=maxv(flag[i][j],k);
            k=1;
            di=i;dj=j;
            while (1) {
                if (g[di+1][dj+1]==g[i][j] && dj+1<=n && di+1<=n) {
                    k++;
                    dj++;di++;
                    }
                else break;
                }
            flag[i][j]=maxv(flag[i][j],k);
            k=1;
            di=i;dj=j;
            while (1) {
                if (g[di+1][dj-1]==g[i][j] && dj-1>=1 && di+1<=n) {
                    k++;
                    dj--;di++;
                    }
                else break;
                }
            flag[i][j]=maxv(flag[i][j],k);
            }
    for (int i=1;i<=n;i++) {
        for (int j=1;j<=n;j++) {
            //cout<<flag[i][j];
            if (flag[i][j]>=k) {
                if (g[i][j]=='R') a=true;
                if (g[i][j]=='B') b=true;
                }
            }
        //cout<<endl;
        }
    if (!a && !b) printf("Neither\n");
    if (a && b) printf("Both\n");
    if (a && !b) printf("Red\n");
    if (!a && b) printf("Blue\n");
}
void display()
{
    scanf("%d",&Case);
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ",ca);
        scanf("%d%d",&n,&k);
        for (int j=1;j<=n;j++) {
            getchar();
            for (int i=1;i<=n;i++)
                g[i][j]=getchar();
            }
        for (int i=1;i<=n;i++) 
            g[0][i]=g[i][0]=g[n+1][i]=g[i][n+1]='#';
        down();
        //for (int i=1;i<=n;i++) { 
            //for (int j=1;j<=n;j++) 
                //cout<<g[i][j];
            //cout<<endl;
            //}
        check();
        }
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    display();
    return 0;
}

