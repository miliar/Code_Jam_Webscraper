#include <iomanip>
#include <stdio.h>
#include <vector>
using namespace std;
int main(){
  FILE *in = fopen("small","r");
  FILE *out = fopen("small.out","w");
  int n;
  fscanf(in,"%d", &n);
  for (int i = 0; i < n; i++){
//    printf("new case\n");
    int o=1, b=1,tmpint,op=0,bp=0,req=0;
    char tmpchar;
    vector<int> seqc[2][2];
    int n1;
    fscanf(in,"%d ",&n1);
    for (int j = 0; j < n1; j++){
      fscanf(in," %c %d ",&tmpchar,&tmpint);
      if (tmpchar=='O') {
        seqc[0][0].push_back(tmpint);
        seqc[0][1].push_back(j);
      }else{
        seqc[1][0].push_back(tmpint);
        seqc[1][1].push_back(j);
      }
    }
    while (op != seqc[0][0].size() && bp != seqc[1][0].size()){
//      printf("o %d b %d \n",o,b);
      bool tst= false;
      if (seqc[0][1][op] < seqc[1][1][bp] && seqc[0][0][op]== o){
        op++;
        tst=true;
      }else{
          o += (seqc[0][0][op]-o > 0) - (seqc[0][0][op]-o < 0); 
        }
      
      if (seqc[0][1][op] > seqc[1][1][bp] && seqc[1][0][bp]== b && !tst){
        bp++;
      }else{
          b += (seqc[1][0][bp]-b > 0) - (seqc[1][0][bp]-b < 0); 
        }
      req++;
    }
    while (op != seqc[0][0].size() ){
      if (seqc[0][0][op]== o){
        op++;
      }else{
          o += (seqc[0][0][op]-o > 0) - (seqc[0][0][op]-o < 0); 
      }
      req++;
    }
    while (bp != seqc[1][0].size() ){
      if (seqc[1][0][bp]== b){
        bp++;
      }else{
          b += (seqc[1][0][bp]-b > 0) - (seqc[1][0][bp]-b < 0); 
      }
      req++;
    }
  printf("Case #%d: %d\n",i+1,req);

  }
}
