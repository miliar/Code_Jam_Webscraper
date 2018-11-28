#include<cstdio>
#include<cstring>
using namespace std;


int main() {
  FILE *fin = fopen("D:\\in.txt","r");
  FILE *fout = fopen("D:\\magicka.txt","w");

  int n;

  fscanf(fin,"%d",&n);

  for (int i = 0; i < n; i++ ) {
    int element[1000];
    int trans[100][100];
    int anti[100][100];
    memset(element,0,sizeof(element));
    memset(trans,0,sizeof(trans));
    memset(anti,0,sizeof(anti));
    int nComb;
    fscanf(fin,"%d ",&nComb);
    for (int j = 0; j < nComb; j++ ) {
      char b1,b2,c;
      fscanf(fin,"%c%c%c",&b1,&b2,&c);
      element[b1] = b2;
      element[b2] = b1;
      trans[b1][b2] = c;
      trans[b2][b1] = c;
    }
    fscanf(fin,"%d ",&nComb);
    for (int j = 0; j < nComb; j++ ) {
      char b1,b2;
      fscanf(fin,"%c%c",&b1,&b2);
      anti[b1][b2] = 1;
      anti[b2][b1] = 1;
    }

    int nChar;
    fscanf(fin,"%d " ,&nChar);


    char in[1000];
    memset(in,0,sizeof(in));

    for (int j = 0; j < nChar;j++)
      fscanf(fin,"%c",&in[j]);

    int l = strlen(in);
    char out[1000];
    int p = 0;
    memset(out,0,sizeof(out));

    int num[1000];
    memset(num,0,sizeof(num));
    for (int j = 0; j < l; j++ ) {
      out[p++] = in[j];
      num[in[j]]++;
      if (j == 0) continue;
        char temp = out[p-1];
        char temp2 = out[p-2];
        if (trans[temp][temp2] != 0) {
          out[p-1] = 0;
          out[p-2] = trans[temp][temp2];
          num[temp2]--;
          num[temp]--;
          num[trans[temp][temp2]]++;
          p--;
        }
        else {
          for (int k = 0; k < strlen(out); k++ )
            if (anti[temp][out[k]]) {
              memset(out,0,sizeof(out));
              p = 0;
              memset(num,0,sizeof(num));
              break;
            }
        }
    }

    fprintf(fout,"Case #%d: [",i+1);
    for ( int j = 0; j < strlen(out); j++ ) {
      if (j == strlen(out) - 1) fprintf(fout,"%c",out[j]);
      else fprintf(fout,"%c, ",out[j]);
    }
    fprintf(fout,"]\n");
  }

  return 0;

}





