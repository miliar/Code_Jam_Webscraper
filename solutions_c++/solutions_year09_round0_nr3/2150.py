#include<cstdio>
#include<cstring>

using namespace std;

const char mo[]=" welcome to code jam";

int test,T;
char s[1000];
int n,m,i,j,k,sum;
int f[1000][20];
int ans[10];

int main(){
    scanf("%d\n",&T);

    for(test=1;test<=T;++test){
        gets(s);
        n=strlen(s);
        memset(f,0,sizeof(f));
        f[0][0]=1;
        sum=0;
        for(i=1;i<=n;++i){
            for(j=1;j<=19;++j)
                if(s[i-1]==mo[j])
                    for(k=0;k<i;++k){
                        f[i][j]+=f[k][j-1];
                        if(f[i][j]>=10000) f[i][j]-=10000;
                    }
//            for(j=1;j<=19;++j) printf("%d  ",f[i][j]);printf("\n");
            sum+=f[i][19];
            if(sum>=10000) sum-=10000;
        }
        printf("Case #%d: ",test);
        for(i=0;i<4;++i){
            ans[i]=sum%10;
            sum/=10;
        }
        for(i=3;i>=0;--i) printf("%d",ans[i]);
        printf("\n");
    }
} 
