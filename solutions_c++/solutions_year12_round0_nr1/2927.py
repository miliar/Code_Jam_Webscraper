#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const char* input_file = "A-small-attempt1.in";
const char* output_file = "A-small-attempt1.ou";
#define MAXN  200000

char g2e_map[26] = {'y','h','e','s','o','c','v','x','d',\
                    'u','i','g','l','b','k','r','z','t',\
                    'n','w','j','p','f','m','a','q'};
int main ( ) {
  FILE* fp_in,*fp_out;
  char googlerese[MAXN];
  char english[MAXN];
  int case_number;
  int n,a,b;
  //read file
  fp_in=fopen(input_file,"r");
  fp_out=fopen(output_file,"w");
  fscanf(fp_in,"%d\n",&case_number);
  for ( int k=1 ; k<=case_number ; k++ ) {
    fgets(googlerese,MAXN,fp_in);
    n = strlen(googlerese);
    for ( int i=0 ;i<n ; i++ ) {
      if ( googlerese[i] == ' ' ) 
        english[i] = ' ';
      else 
        english[i] = g2e_map[googlerese[i]-'a'];
    }
    english[n] = '\0';

    fprintf(fp_out,"Case #%d: ",k);
    fprintf(fp_out," %s\n",english);

  }
  fclose(fp_in);
  fclose(fp_out);
}