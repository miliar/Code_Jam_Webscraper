/*

*/
#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
int Case,r,c;
char g[55][55];
bool change()
{
    for (int i=1;i<=r;i++)
        for (int j=1;j<=c;j++)
            if (g[i][j]=='#') {
                if (g[i][j+1]=='#' && g[i+1][j]=='#' && g[i+1][j+1]=='#') {
                    g[i][j]='/';
                    g[i][j+1]='\\';
                    g[i+1][j]='\\';
                    g[i+1][j+1]='/';
                }
                else return false;
            }
    return true;
}
void display()
{
    scanf("%d",&Case);
    for (int ca=1;ca<=Case;ca++) {
        printf("Case #%d:\n",ca);
        scanf("%d%d",&r,&c);
        for (int i=1;i<=r;i++)
            scanf("%s",g[i]+1);
        if (change()) {
            for (int i=1;i<=r;i++)
                for (int j=1;j<=c;j++) {
                    printf("%c",g[i][j]);
                    if (j==c) printf("\n");
                }
        }
        else printf("Impossible\n");
    }
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    display();
    return 0;
}

