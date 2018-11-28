#include <cstdio>
#include <cstring>

int n,m,f[100][100],a[100][100],ansa[100],ansb[100];

int min(int a,int b) {
    if (a<b) return a;
      else return b;
}

void DP(){
     int i,j,k;
     memset(f,0,sizeof(f));
     for (i = 1; i<=m; i++)
       for (j = 1; j<=n; j++) {
         if (a[i][j] == -1) continue;
         if (a[i][j]+a[i][j-1] == 1 && a[i][j]+a[i-1][j]==1 &&a[i][j] == a[i-1][j-1])
            f[i][j] = min(min(f[i-1][j],f[i][j-1]),f[i-1][j-1]); 
         f[i][j]++;   
       }
}

void Fill(int x,int y,int l) {
     int i,j,k;
     //printf("%d %d\n",x,y);
     for (i = x; i<x+l; i++)
       for (j = y; j<y+l; j++)
         a[i][j] = -1;
}

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int tt,test,i,k,ans,j;
    scanf("%d",&test);
    char s[100];
    for (tt = 1; tt<=test; tt++) {
        scanf("%d %d",&m,&n);
      //  memset(f,0,sizeof(f));
      //  if (tt==27) printf("%d %d\n",m,n);
        memset(a,0,sizeof(a));
        for (i = 1; i<=m; i++) {
          scanf("%s",s);
      //    if (tt==27) printf("%s\n",s);
       //   printf("%s\n",s);
          int now = 0;
          for (j = 0; j<n/4; j++) {
            int t = 0;
            if (s[j]>='A') t = s[j]-'A'+10;
               else t = s[j]-'0';
         //   printf("%d  ",t);   
            if (t & 1==1) a[i][now+4] = 1;
            t = t/2;
            if (t & 1==1) a[i][now+3] = 1;
            t = t/2;
            if (t & 1==1) a[i][now+2] = 1;
            t = t/2;            
            if (t & 1==1) a[i][now+1] = 1;
            now += 4;             
          }    
        }
    /* 
       for (i = 1; i<=m; i++) {
          for (j = 1; j<=n; j++)
            printf("%d",a[i][j]); printf("\n");
            }
        printf("--------------\n"); */
        ans = 0;
        int max = 100000;
        memset(ansb,0,sizeof(ansb));
        while (max != 1) {
          DP();    
          max = 0;
       /* 
              for (i = 1; i<=m; i++) {
            for (j = 1; j<=n; j++)
              printf("%2d",a[i][j]); printf("\n");}
          printf("------------------------------------\n");       
          for (i = 1; i<=m; i++) {
            for (j = 1; j<=n; j++)
              printf("%2d",f[i][j]); printf("\n");}  // */
          for (i = 1; i<=m; i++)
            for (j = 1; j<=n; j++)
              if (f[i][j]>max) max = f[i][j];
          if (max == 0) break;    
      //    printf("%d\n",max);    
          ans++;   
          ansa[ans] = max;
          if (max==1) {
             for (i = 1; i<=m; i++)
               for (j = 1; j<=n; j++)
                 if (a[i][j]>=0) ansb[ans]++; 
             break;           
          }    
          for (i = 1; i<=m; i++)
            for (j = 1; j<=n; j++) 
              if (f[i][j] == max) {
                 ansb[ans]++;
                 Fill(i-max+1,j-max+1,max);
                 DP();         
              }
        }
        printf("Case #%d: %d\n",tt,ans);
        for (i = 1; i<=ans; i++)
          printf("%d %d\n",ansa[i],ansb[i]);
    }
    return 0;
}
