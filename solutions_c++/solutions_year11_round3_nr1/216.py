#include<stdio.h>
int main(){
    int C,n,m,Case=1;
    char s[55][55];
    scanf("%d",&C);
    while(C--){
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            scanf("%s",s[i]);
        int flag=1;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(i<n-1&&j<m-1&&s[i][j]=='#'&&s[i][j+1]=='#'&&s[i+1][j]=='#'&&s[i+1][j+1]=='#'){
                    s[i][j]=s[i+1][j+1]='/';
                    s[i+1][j]=s[i][j+1]='\\';
                }else if(s[i][j]=='#')
                    flag=0;
        printf("Case #%d:\n",Case++);
        if(flag)
            for(int i=0;i<n;i++)
                puts(s[i]);
        else puts("Impossible");
    }
}
