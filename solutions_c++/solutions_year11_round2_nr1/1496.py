#include<cstdio>
#include<cstring>
using namespace std;

int main() {
  int t;
  FILE *fin = fopen("D:\\in.txt","r");
  FILE *fout = fopen("D:\\out.txt","w");

  fscanf(fin,"%d",&t);

  for ( int i = 0; i < t; i++ ) {
    double result[101][3];
    int n;
    char c;
    fscanf(fin,"%d%c",&n,&c);
    char table[101][101];
    memset(table,0,sizeof(table));

    for ( int j = 0; j < n; j++) {
      for ( int k = 0; k < n; k++ )
        fscanf(fin,"%c",&table[j][k]);
      fscanf(fin,"%c",&c);
    }

    for ( int j = 0; j < n; j++ ) {
      double wp,owp;
      owp  = 0;
      int win = 0;
      int lose = 0;

      for ( int k = 0; k < n; k++ ) {
        if ( table[j][k] == '1') win++;
        else if ( table[j][k] == '0') lose++;
      }

      wp = (double)win / (win + lose);

      int num = 0;

      for ( int k = 0; k < n; k++ ) {
        if ( table[k][j] != '.' ) {
          win = 0;
          lose = 0;
          for ( int l = 0; l < n; l++ ) {
            if (l == j) continue;
            if ( table[k][l] == '1') win++;
            else if ( table[k][l] == '0') lose++;
          }
          num++;
          owp += (double)win / (win + lose);
        }
      }

      owp /= num;

      result[j][0] = wp;
      result[j][1] = owp;

    }

    for ( int j = 0; j < n; j++ ) {
      int num = 0;
      double oowp = 0;
      for ( int k = 0; k < n; k++ ) {
        if ( table[j][k] != '.' ) {
          oowp += result[k][1];
          num++;
        }
      }
      oowp /= num;

      result[j][2] = oowp;
    }

    fprintf(fout,"Case #%d:\n",i+1);
    for ( int j = 0; j < n; j++ ) {
      fprintf(fout,"%lf\n",0.25*result[j][0] + 0.5*result[j][1] + 0.25*result[j][2]);
    }
  }

  fclose(fin);
  fclose(fout);

  return 0;

}






