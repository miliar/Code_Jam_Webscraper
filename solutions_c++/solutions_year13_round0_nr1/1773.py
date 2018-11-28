#define LOCAL
#include <stdio.h>
int main(){
#ifdef LOCAL
       freopen("data.txt", "r", stdin);
       freopen("data.out", "w", stdout);
#endif
       int t,n;
       scanf("%d",&t);
       for(n=1;n<=t;n++){
       printf("Case #%d: ",n);
       void work();
       work();
       }
       return 0;
}
char a[5][5];
int check(int x,int y,int dx,int dy){
    int i;
    int f=0;
    char c='T';
    for(i=0;i<4;i++){
                     if(c!=a[x][y]){
                                    if(a[x][y]=='.')return 0;
                                    if(c!='T'&&a[x][y]!='T')return 0;
                                    if(c=='T')c=a[x][y];
                                    }
                     x+=dx;
                     y+=dy;
                     }
    printf("%c won\n",c);
    return 1;
}
int find(){
    int i,j;
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)if(a[i][j]=='.')return 1;
    return 0;
}
void work(){
     int i;
     for(i=0;i<4;i++)scanf("%s",a[i]);
     for(i=0;i<4;i++)if(check(i,0,0,1))return ;
     for(i=0;i<4;i++)if(check(0,i,1,0))return ;
     if(check(0,0,1,1))return ;
     if(check(3,0,-1,1))return ;
     if(find()==0)printf("Draw\n");
     else printf("Game has not completed\n");
}
