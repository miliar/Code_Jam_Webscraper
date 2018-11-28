#include<cstdio>
#include<algorithm>
using namespace std;

int main() {
  FILE *fout = fopen("D:\\out.txt","w");
  FILE *fin = fopen("D:\\in.txt","r");

  int t;

  fscanf(fin,"%d",&t);

  for (int ll = 0; ll < t; ll++ ) {
    int n,l,h;
    int result = 0;
    int ostali[110];
    fscanf(fin,"%d %d %d",&n,&l,&h);
    for (int i = 0; i < n; i++ )
      fscanf(fin,"%d",&ostali[i]);

    for (int i = l; i <= h; i++ ) {
      int possible = 1;
      for (int j = 0; j < n; j++) {
        if (i % ostali[j] == 0 || ostali[j] % i == 0) continue;
        else possible=0;
      }
      if (possible) { result = i; break; }
    }

    fprintf(fout,"Case #%d: ",ll+1);
    if (result)
      fprintf(fout,"%d\n",result);
    else fprintf(fout,"NO\n");
  }

  fclose(fin);
  fclose(fout);

  return 0;

}
