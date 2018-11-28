#include<iostream>
char a[100][100];
int i,j,k,l,m,n,xys,ysc;
bool work(int x,int y)
{
     if (a[x+1][y]!='#'||a[x][y+1]!='#'||a[x+1][y+1]!='#') return false;
     a[x][y]='/';
     a[x][y+1]='\\';
     a[x+1][y]='\\';
     a[x+1][y+1]='/';
     return true;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&ysc);
    for (xys=1;xys<=ysc;++xys){
        scanf("%d%d",&n,&m);
        l=1;
        for (i=0;i<n;++i) scanf("%s",a[i]);
        for (i=0;i<n;++i){
            for (j=0;j<m;++j)
                if (a[i][j]=='#')
                   if (!work(i,j)){
                      l=0;
                      break;
                   }
            if (l==0) break;
        }
        printf("Case #%d:\n",xys);
        if (l==0) printf("Impossible\n");
        else for (i=0;i<n;++i) printf("%s\n",a[i]);
    }
    return 0;
}
