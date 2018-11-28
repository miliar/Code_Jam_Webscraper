#include <stdio.h>

int A[101][101];
char res[101][101];
int H,W;
int T;

int in_range(int x, int y) {
    return (x >= 0 && y >= 0 && x < H && y < W);
}

int flows_to(int j, int k) {
     int dir = 0;
     int best = A[j][k];
     if (in_range(j-1,k) && A[j-1][k] < best) {
        dir=1;
        best=A[j-1][k];
        }
     if (in_range(j,k-1) && A[j][k-1] < best) {
        dir=2;
        best=A[j][k-1];
        }
     if (in_range(j,k+1) && A[j][k+1] < best) {
        dir=3;
        best=A[j][k+1];
        }
     if (in_range(j+1,k) && A[j+1][k] < best) {
        dir=4;
        best=A[j+1][k];
        }
     return dir;
}

void put_levels(int j, int k, int levels) {
     if (in_range(j-1,k) && flows_to(j-1,k) == 4) {
        res[j-1][k] = levels;
        put_levels(j-1,k,levels);
        }
     if (in_range(j,k-1) && flows_to(j,k-1) == 3) {
        res[j][k-1] = levels;
        put_levels(j,k-1,levels);
        }
     if (in_range(j,k+1) && flows_to(j,k+1) == 2) {
        res[j][k+1] = levels;
        put_levels(j,k+1,levels);
        }
     if (in_range(j+1,k) && flows_to(j+1,k) == 1) {
        res[j+1][k] = levels;
        put_levels(j+1,k,levels);
        }
}

void swap_levels(char l1, char l2) {
     for (int i=0;i<H;++i)
         for (int j=0;j<W;++j)
             if (res[i][j] == l1) res[i][j] = l2;
             else if (res[i][j] == l2) res[i][j] = l1;
}

void update_levels(char max) {
     char cur_lev = 'a';
     int i=0;
     int j=0;
     while (cur_lev < max) {
           if (res[i][j] != cur_lev) 
              swap_levels(cur_lev,cur_lev+1);
           while (res[i][j] == cur_lev) {
                 ++j;
                 if (j == W) {j=0;++i;}
                 if (i==H) return;
           }
           ++cur_lev;
     }
}

int main() {
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;++i) {
        scanf("%d %d",&H,&W);
        for (int j=0;j<H;++j)
            for (int k=0;k<W;++k) {
                res[j][k] = 0;
                scanf("%d",&A[j][k]);
            }
        
        char levels='a';
        for (int j=0;j<H;++j)
            for (int k=0;k<W;++k) {
                if (!flows_to(j,k)) {
                   res[j][k]=levels;
                   put_levels(j,k,levels);
                   ++levels;
                   }
            }
        update_levels(levels-1);
        printf("Case #%d:\n",i);
        for (int j=0;j<H;++j) {
            for (int k=0;k<W-1;++k)
                printf("%c ",res[j][k]);
            printf("%c\n",res[j][W-1]);
            }
    }    
    return 0;   
}
