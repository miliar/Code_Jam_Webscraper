#include<iostream>
using namespace std;
const char p[21]=" welcome to code jam";
char s[1000];
int f[1000][30];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d\n",&t);
    int i,j;
    for(int ii=1;ii<=t;ii++){
        gets(s);
        memset(f,0,sizeof(f));
        f[0][0]=1;
        for(i=1;i<=strlen(s);i++){
            f[i][0]=f[i-1][0];
            for(j=1;j<=19;j++){
                f[i][j]=f[i-1][j];
                if(s[i-1]==p[j])
                    f[i][j]+=f[i-1][j-1];
                f[i][j]%=10000;
            }
        }
        int a=f[strlen(s)][19];
        printf("Case #%d: %d%d%d%d\n",ii,a/1000,(a/100)%10,(a/10)%10,a%10);
    }
    return(0);
}

