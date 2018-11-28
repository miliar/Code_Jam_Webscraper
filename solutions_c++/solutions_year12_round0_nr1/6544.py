#include <stdio.h>

int main(int argc, char **argv) {

  int letter[26];
  
  char c;
  
  letter[0]=121;letter[1]=104;letter[2]=101;letter[3]=115;letter[4]=111;letter[5]=99;letter[6]=118;letter[7]=120;
  letter[8]=100;letter[9]=117;letter[10]=105;letter[11]=103;letter[12]=108;letter[13]=98;letter[14]=107;letter[15]=114;
  letter[16]=122;letter[17]=116;letter[18]=110;letter[19]=119;letter[20]=106;letter[21]=112;letter[22]=102;letter[23]=109;
  letter[24]=97;letter[25]=113;
  
  int i,nCases;
  scanf("%d",&nCases);
  getchar();
  i=0;
  while(i<nCases){
    printf("Case #%d: ",i+1);
    while((c=getchar())!='\n'){
      (c != ' ') ? printf("%c",letter[c-97]):printf(" "); 
    }   
    printf("\n"); 
    i++;
  }
  
  return 0;
}
