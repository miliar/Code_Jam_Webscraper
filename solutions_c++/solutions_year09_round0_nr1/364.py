#include<stdio.h>
#include<string.h>

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

bool vis[16][27];
char t[5005][17];
char x[20000];

int main()
{
    int i , a , l , n , m , j , ret = 0 , flag;
    fscanf(in,"%d %d %d",&l,&n,&m);
    for(i=0;i<n;i++)
        fscanf(in,"%s",t[i]);
    for(i=0;i<m;i++)
    {
        fscanf(in,"%s",x);
        memset(vis,0,sizeof vis);
        ret = 0;
        for(a=0,flag=0;x[a] != '\0';a++,flag++)
        {
            if(x[a] == '(')
            {
                for(j=a+1;x[j] != ')';j++)
                    vis[flag][x[j]-'a'] = 1;
                a = j;
            }
            else
                vis[flag][x[a]-'a'] = 1;
        }
        for(a=0;a<n;a++)
        {
            flag = 1;
            for(j=0;t[a][j] != '\0';j++)
                if(vis[j][t[a][j]-'a'] == 0) flag = 0;
            if(flag) ret++;
        }
        fprintf(out,"Case #%d: %d\n",i+1,ret);
    }
    //getchar();getchar();
    return 0;
}
