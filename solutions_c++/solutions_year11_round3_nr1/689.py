#include<cstdio>
#include<cstring>


int main() {

  FILE *fin = fopen("D:\\in.txt","r");
  FILE *fout = fopen("D:\\out.txt","w");

  int t;
  fscanf(fin,"%d",&t);

  for ( int l = 0; l < t; l++ ) {
    char in[55][55];
    memset(in,0,sizeof(in));
    int r,c;
    char b;
    int possible = 1;
    fscanf(fin,"%d %d%c",&r,&c,&b);
    for ( int i = 0; i < r; i++ )
      fscanf(fin,"%s",in[i]);

    for ( int i = 0; i < r; i++ )
      for ( int j = 0; j < c; j++ ) {
        if ( in[i][j] == '#' )
          if (i < r-1 && j < c-1)
            if (in[i+1][j] == '#' && in[i][j+1] =='#' && in[i+1][j+1] == '#' ) {
              in[i][j] = '/';
              in[i][j+1] = '\\';
              in[i+1][j] = '\\';
              in[i+1][j+1] = '/';
            }
      }

    for ( int i = 0; i < r; i++ )
      for ( int j = 0; j < c; j++ )
        if (in[i][j] == '#') possible=0;

    fprintf(fout,"Case #%d:\n",l+1);
    if (possible)
      for ( int i = 0; i < r; i++ )
          fprintf(fout,"%s\n",in[i]);
    else
      fprintf(fout,"Impossible\n");

  }

  fclose(fin);
  fclose(fout);

  return 0;

}


