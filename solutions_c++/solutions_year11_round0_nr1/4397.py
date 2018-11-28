#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
  int n;


  FILE *fout = fopen("D:\\botTrust.txt","w");
  FILE *fin = fopen("D:\\in.txt","r");


  fscanf(fin,"%d",&n);

  for (int i = 0; i < n; i++ ) {
    int nn;
    fscanf(fin,"%d ",&nn);
    int t = 0;
    char temp;
    int orange=0,blue=0;
    int o=1,b=1;
    for (int j = 0; j < nn; j++ ) {
      char c;
      int a;
      fscanf(fin,"%c %d%c",&c,&a,&temp);
      if (c == 'O')  {
        int potrebnoVrijeme = abs(a - o) + 1;
        if (potrebnoVrijeme > ( t - orange ) )
          t += potrebnoVrijeme -(t - orange);
        else t++;
        orange = t;
        o = a;
      }
      else {
        int potrebnoVrijeme = abs(a - b) + 1;
        if (potrebnoVrijeme > ( t - blue ) )
          t += potrebnoVrijeme -(t - blue);
        else t++;
        blue = t;
        b = a;
      }
    }
    fprintf(fout,"Case #%d: %d\n",i+1,max(orange,blue));
  }



  fclose(fout);
  fclose(fin);
  return 0;

}
