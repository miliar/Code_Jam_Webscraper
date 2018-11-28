#include<stdio.h>

int main() {
  int total,i,j,m,P,K,L,pom,zbir,rez,br;
  int let[1000];
  bool dali;
  FILE *fi,*fo;
  char c;
  fi = fopen("input.txt","r+");
  fo = fopen("output.txt","w+");
  fscanf(fi,"%d",&total);
  
  
  
  for (m=0;m<total;m++) {
      
    fscanf(fi,"%d%d%d",&P,&K,&L);
    zbir=0;
    rez=0;
    for (j=0;j<L;j++) {
      fscanf(fi,"%d",&let[j]);
      zbir=zbir+let[j];
    }
    // this is the main part
    for (i=0;i<L;i++) {
      for (j=i;j<L;j++) {
        if (let[i]<let[j]) {
          pom=let[i];
          let[i]=let[j];
          let[j]=pom;
        }
      }
    }
    
    // checks if it is impossible
    if (L>P*K) {
      // there are more letters than available spaces
      fprintf(fo,"Case #%d: Impossible\n",m+1);
    } else {
      pom=0;
      br=-1;
      dali=true;
      while (dali==true) {
        pom++;
        for (j=1;j<=K;j++) {
          br++;
          if (br<L) {
            rez=rez+let[br]*pom;
          } else {
            dali=false;
          }
        }
      }
        
    }
    
    fprintf(fo,"Case #%d: %d\n",m+1,rez);
  }
  
  
  fclose(fi);
  scanf("%d",&i);
  return 0;
}
