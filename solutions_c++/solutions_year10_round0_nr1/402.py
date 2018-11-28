#include <iostream>
#include <vector>
#include <string>
#include <regex.h>
using namespace std;


int main() {
  int t;
  scanf("%d", &t);

  for(int iii=1; iii<=t; iii++) {
    int n, k;
    scanf("%d %d", &n, &k);

    int n2=1;
    for(int i=0; i<n; i++) n2*=2;

    printf("Case #%d: ", iii);
/*
    if(n==1) {
      if( (k%2)==1 ) {
        printf("ON\n");
      } else {
        printf("OFF\n");
      }      
    } else {*/
      if( (k%n2)==(n2-1) ) {
        printf("ON\n");
      } else {
        printf("OFF\n");
      }
//    }

  }


  return 0;
}




