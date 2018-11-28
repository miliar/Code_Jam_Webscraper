#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const char* input_file = "C-small-attempt0.in";
const char* output_file = "C-small-attempt0.ou";
#define MAXN  1010
int mark[MAXN][MAXN];

int CheckRecycle ( int b , int e ) {
  memset(mark,0,sizeof(mark));
  int m = (b+e)/2;
  int res=0;
  int t,upper,lower;
  int range,recy;
  for ( int i=b ; i<=e ; i++ ) {
    range=10 ;
    t = i;
    while ( t/10 ) {
      t/=10;
      range*=10;
    }
    t = i;
    for ( int j = 10 ; t>=j ; j*=10 ) {
      upper = t/j;
      lower = t%j;
      recy = lower*range/j+upper;
      if ( recy > i && recy <=e && !mark[i][recy]) {
        //printf("%d,%d\n",i,recy);
        mark[i][recy] = 1;
        res++;
      }
    }
  }
  return res;
}

int main ( ) {
  FILE* fp_in,*fp_out;
  int sum_score;
  int case_number;
  int b,e,res;
  //read file
  fp_in=fopen(input_file,"r");
  fp_out=fopen(output_file,"w");
  fscanf(fp_in,"%d\n",&case_number);
  for ( int k=1 ; k<=case_number ; k++ ) {
    fscanf(fp_in,"%d%d",&b,&e);
    res = CheckRecycle(b,e);
    
    fprintf(fp_out,"Case #%d: ",k);
    fprintf(fp_out," %d\n",res);

  }
  fclose(fp_in);
  fclose(fp_out);
}