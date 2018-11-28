#include<cstdio>
const int N=101,dx[]={-1,0,0,1},dy[]={0,-1,1,0};
int n,m,z,s[N][N],c[N][N];
bool valid(int x,int y){return(x>=0 && x<n && y>=0 && y<m);}
int go(int x,int y)
{
    if(s[x][y])return s[x][y];
    int i,j,k=c[x][y];
    for(i=0;i<4;i++)
        if(valid(x+dx[i],y+dy[i]) && k>c[x+dx[i]][y+dy[i]])
            j=i,k=c[x+dx[i]][y+dy[i]];
    if(k<c[x][y])
        return s[x][y]=go(x+dx[j],y+dy[j]);
    return s[x][y]=z++;
}
main()
{
    int i,j,T,C=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++){
                scanf("%d",&c[i][j]);
                s[i][j]=0;
            }
        z='a';
        printf("Case #%d:\n",C++);
        for(i=0;i<n;i++,puts(""))
            for(j=0;j<m;j++)
                printf("%s%c",j?" ":"",go(i,j));
    }
}
