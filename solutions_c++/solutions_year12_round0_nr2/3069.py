#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const char* input_file = "B-large.in";
const char* output_file = "B-large.ou";
#define MAXN  200

int simple_max_score ( int sum ) {
  int res = 0 ;
  int t;
  if ( sum % 3 == 0) {
    t = sum/3;
    if ( t> res ) 
      res = t;
  }
  if ( (sum-1)%3 == 0 && sum>=1) {
    t = (sum-1)/3+1;
    if ( t>res ) 
      res = t;
  }
  if ( (sum-2)%3 == 0 && sum>=2) {
    t = (sum-2)/3+1;
    if ( t>res ) 
      res = t;
  }
  return res;
}

int suprising_max_score ( int sum ) {
  int res = 0; 
  int t;
  if ( (sum-2)%3 == 0 && sum>=2 ) {
    t = (sum-2)/3 +2;
    if ( t>res ) res = t;
  }
  if ( (sum-3)%3 == 0 && sum>=3 ) {
    t = (sum-3)/3+2;
    if ( t>res ) res = t;
  }
  if ( (sum-4)%3 == 0 && sum>=4 ) {
    t = (sum-4)/3+2;
    if ( t>res ) res = t;
  }
  return res;
}

int main ( ) {
  FILE* fp_in,*fp_out;
  int sum_score;
  int case_number;
  int n,a,b,p,s,cnt;
  //read file
  fp_in=fopen(input_file,"r");
  fp_out=fopen(output_file,"w");
  fscanf(fp_in,"%d\n",&case_number);
  for ( int k=1 ; k<=case_number ; k++ ) {
    cnt = 0;
    fscanf(fp_in,"%d%d%d",&n,&s,&p);
    for ( int i =0 ; i<n ; i++ ) {
      fscanf(fp_in,"%d",&sum_score);
      if ( simple_max_score(sum_score)>=p ) 
        cnt++;
      else if ( s>0 && suprising_max_score(sum_score)>=p ) {
        s--;
        cnt++;
      }
    }
    
    fprintf(fp_out,"Case #%d: ",k);
    fprintf(fp_out," %d\n",cnt);

  }
  fclose(fp_in);
  fclose(fp_out);
}