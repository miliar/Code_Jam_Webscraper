#include <cstdio>
#include <cstdlib>
char a[10][10];
bool found[255];
int main(){
   int n, T, empt, sum;
   FILE *fi = fopen("in.in", "r");
   FILE *fo = fopen("out.out", "w");
   fscanf(fi, "%d", &T);
   for (int kl = 1; kl<=T; kl++){
      fscanf(fi, "\n");
      empt = 0;
      found['X'] = false;
      found['O'] = false;
      for (int i = 0; i!=4; i++){
         for (int j = 0; j!=4; j++){
            fscanf(fi, "%c", &a[i][j]);
            if (a[i][j]=='.') empt ++;
         }
         fscanf(fi, "\n");
      }
      for (int i = 0; i!=4; i++){
         for (int j = 0; j!=4; j++){
            sum = -1;
            for (int k = 0; i+k<4 && j+k<4 && (a[i+k][j+k]=='T' || a[i][j]==a[i+k][j+k]); k++) sum++;
            for (int k = 0; i-k>=0 && j-k>=0 && (a[i-k][j-k]=='T' || a[i][j]==a[i-k][j-k]); k++) sum++;
            if (sum>=4) found[a[i][j]] = true;
            sum = -1;
            for (int k = 0; i+k<4 && j-k>=0 && (a[i+k][j-k]=='T' || a[i][j]==a[i+k][j-k]); k++) sum++;
            for (int k = 0; i-k>=0 && j+k<4 && (a[i-k][j+k]=='T' || a[i][j]==a[i-k][j+k]); k++) sum++;
            if (sum>=4) found[a[i][j]] = true;
            sum = -1;
            for (int k = 0; i+k<4 && (a[i+k][j]=='T' || a[i][j]==a[i+k][j]); k++) sum++;
            for (int k = 0; i+k>=0 && (a[i+k][j]=='T' || a[i][j]==a[i+k][j]); k--) sum++;
            if (sum>=4) found[a[i][j]] = true;
            sum = -1;
            for (int k = 0; j+k<4 && (a[i][j+k]=='T' || a[i][j]==a[i][j+k]); k++) sum++;
            for (int k = 0; j+k>=0 && (a[i][j+k] == 'T' || a[i][j]==a[i][j+k]); k--) sum++;
            if (sum>=4) found[a[i][j]] = true;
         }
      }

      if (found['X']) fprintf(fo, "Case #%d: X won\n", kl);
      else if (found['O']) fprintf(fo, "Case #%d: O won\n", kl);
      else if (empt!=0) fprintf(fo, "Case #%d: Game has not completed\n", kl);
      else fprintf(fo, "Case #%d: Draw\n", kl);
   }
   system("pause");
}
            
   
