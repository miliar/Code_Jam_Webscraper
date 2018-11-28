#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;
char s[55][55];
int n,m;
bool flag[55][55];
bool check(int i,int j)
{
    if(i<n&&j<m&&s[i][j]=='#'&&!flag[i][j]) return true;
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outA.txt","w",stdout);
    int t,k,i,j;
    
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++) scanf("%s",s[i]);
        printf("Case #%d:\n",k);
        memset(flag,0,sizeof(flag));
        for(i=0;i<n;i++) {
            for(j=0;j<m;j++) {
                if(s[i][j]=='#'&&!flag[i][j]) {
                    if(check(i,j+1)&&check(i+1,j)&&check(i+1,j+1)) {
                        s[i][j]=s[i+1][j+1]='/';
                        s[i+1][j]=s[i][j+1]='\\';
                        continue;
                    }
                    break;
                }
            }
            if(j<m) break;
        }
        if(i<n) printf("Impossible\n");
        else {
            for(i=0;i<n;i++) printf("%s\n",s[i]);
        }
    }
    return 0;
}
