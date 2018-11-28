#include<cstdio>

int t,T;
char arr[10][10];
char ch;

int main(){
  int i,j;
  FILE *fin,*fout;
  fin = fopen("A-large.in","r");
  fout = fopen("A-large.out","w");
  fscanf(fin,"%d",&T);
  for(t=1;t<=T;t++){
    for(i=0;i<4;i++){
      fscanf(fin,"%s",arr[i]);
    }
    fprintf(fout,"Case #%d: ",t);
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
        if(arr[i][j]!='O' && arr[i][j]!='T') break;
      }
      if(j==4) break;
    }
    if(i<4){
      fprintf(fout,"O won\n");
      continue;
    }
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
        if(arr[j][i]!='O' && arr[j][i]!='T') break;
      }
      if(j==4) break;
    }
    if(i<4){
      fprintf(fout,"O won\n");
      continue;
    }
    for(j=0;j<4;j++){
      if(arr[j][j]!='O' && arr[j][j]!='T') break;
    }
    if(j==4){
      fprintf(fout,"O won\n");
      continue;
    }
    for(j=0;j<4;j++){
      if(arr[j][3-j]!='O' && arr[j][3-j]!='T') break;
    }
    if(j==4){
      fprintf(fout,"O won\n");
      continue;
    }
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
        if(arr[i][j]!='X' && arr[i][j]!='T') break;
      }
      if(j==4) break;
    }
    if(i<4){
      fprintf(fout,"X won\n");
      continue;
    }
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
        if(arr[j][i]!='X' && arr[j][i]!='T') break;
      }
      if(j==4) break;
    }
    if(i<4){
      fprintf(fout,"X won\n");
      continue;
    }
    for(j=0;j<4;j++){
      if(arr[j][j]!='X' && arr[j][j]!='T') break;
    }
    if(j==4){
      fprintf(fout,"X won\n");
      continue;
    }
    for(j=0;j<4;j++){
      if(arr[j][3-j]!='X' && arr[j][3-j]!='T') break;
    }
    if(j==4){
      fprintf(fout,"X won\n");
      continue;
    }
    for(i=0;i<4;i++){
        for(j=0;j<4;j++)
            if(arr[i][j]=='.') break;
        if(j<4) break;
    }
    if(i<4){
       fprintf(fout,"Game has not completed\n");
       continue;
    }
    fprintf(fout,"Draw\n");

  }

  return 0;
}
