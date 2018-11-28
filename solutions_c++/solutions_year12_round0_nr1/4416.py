#include<stdio.h>
int record[30];

void Init(){
record[0]=24;
record[1]=7;
record[2]=4;
record[3]=18;
record[4]=14;
record[5]=2;
record[6]=21;
record[7]=23;
record[8]=3;
record[9]=20;
record[10]=8;
record[11]=6;
record[12]=11;
record[13]=1;
record[14]=10;
record[15]=17;
record[16]=25;
record[17]=19;
record[18]=13;
record[19]=22;
record[20]=9;
record[21]=15;
record[22]=5;
record[23]=12;
record[24]=0;
record[25]=16;
}

int main(){
  int t,i,k;
  char c;
  //freopen("A-small-attempt3.in","r",stdin);
  //freopen("A-small-attempt3.out","w",stdout);

  Init();
  scanf("%d",&t);
  getchar();
  for(i=1;i<=t;i++){

     c=getchar();
     printf("Case #%d: ",i);
     while(c!='\n'){
       if ('a'<=c && c<='z') printf("%c",record[c-'a']+'a');
                        else printf("%c",c);
       c=getchar();
     }
     printf("\n");
  }
  return 0;

}
