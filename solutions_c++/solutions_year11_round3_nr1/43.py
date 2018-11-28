#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

int T;
int r,c;
char a[100][100];
int p;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=1;k<=T;k++){
        scanf("%d%d ",&r,&c);
        memset(a,'.',sizeof(a));
        for (int i=0;i<r;i++)
            for (int j=0;j<c;j++) scanf("%c ",&a[i][j]);
        p=0;
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++)
                if (a[i][j]=='#'){
                    if (a[i+1][j]!='#') p=1;
                    if (a[i][j+1]!='#') p=1;
                    if (a[i+1][j+1]!='#') p=1;
                    if (p==1) break;
                    a[i][j]='/';a[i][j+1]='\\';
                    a[i+1][j]='\\';a[i+1][j+1]='/';
                }
            if (p==1) break;
        }
        printf("Case #%d:\n",k);
        if (p==1) printf("Impossible\n");
        else{
            for (int i=0;i<r;i++){
                for (int j=0;j<c;j++) printf("%c",a[i][j]);
                printf("\n");
            }
        }
    }
    return 0;
}
