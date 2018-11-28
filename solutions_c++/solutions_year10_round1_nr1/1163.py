#include <cstdio>
#include <cstring>
int n,l;
char a[100][100];
int dx[4] = {1,1,0,-1},
    dy[4] = {1,0,1,1};
void Rotate() {
     int i,j;
     char b[100][100];
     memset(b,0,sizeof(b));
     for (i = 1; i<=n; i++)
       for (j = 1; j<=n; j++)
         b[j][n-i+1] = a[i][j];
     for (i = 0; i<=n+1; i++)
       for (j = 0; j<=n+1; j++)
         a[i][j] = '.';    
     for (j = 1; j<=n; j++) {
       int now = n+1;   
       for (i = n; i>=1; i--) 
         if (b[i][j] != '.') a[--now][j] = b[i][j];   
     }
  /*   
      for (i = 1; i<=n; i++) {
       for (j = 1; j<=n; j++)
         printf("%c",a[i][j]);
       printf("\n");  
     }  //  */
}

int Go(int x,int y,char ch,int k,int len) {
    if (a[x][y] != ch) return 0;
    len++;
 //   printf("%c %d %d %d\n",ch,x,y,len);
    if (len>=l) return 1;
    if (Go(x+dx[k],y+dy[k],ch,k,len)) return 1;
    return 0;
}

int Can(char ch) {
    int i,j,k;
    for (i = 1; i<=n; i++)
      for (j = 1; j<=n; j++)
        if (a[i][j] == ch) {
           for (k = 0; k<4; k++)
             if (Go(i,j,ch,k,0)==1) return 1;         
        } 
    return 0;    
}

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout); 
    int test,tt,i,j,k;
    scanf("%d",&test);
    for (tt = 1; tt<=test; tt++) {
        scanf("%d %d\n",&n,&l);
        for (i = 1; i<=n; i++) {
          for (j = 1; j<=n; j++)
            scanf("%c",&a[i][j]);
          scanf("\n");  
        }
        Rotate(); 
        printf("Case #%d: ",tt);
        int flag1 = Can('B'),flag2 = Can('R'); 
       // printf("%d %d\n",flag1,flag2);
        if (flag1 && flag2) printf("Both\n");
           else if (flag1) printf("Blue\n");
                    else if (flag2) printf("Red\n");
                             else printf("Neither\n"); 
    }
    return 0;
}
