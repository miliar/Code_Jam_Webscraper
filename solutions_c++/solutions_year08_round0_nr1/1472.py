/*
/* Author: Giacomo Spigler
/* Contest: Google CODEJam 2008, Qualification Round
/* Date: 27/07/2008
*/

#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
  int n, nsearch, q;
  vector<string> se;
  vector<string> qe;

  char s[100];


  scanf("%d", &n);  //test cases

  for(int ccc=0; ccc<n; ccc++) {
    scanf("%d", &nsearch);

    se.clear();
    qe.clear();

    char c;
    scanf("%c", &c);


    for(int i=0; i<nsearch; i++) {
      gets(s);

//if(ccc==0) cout<<s<<endl;
      se.push_back(s);
    }


    scanf("%d", &q);


    scanf("%c", &c);

    for(int i=0; i<q; i++) {
      gets(s);

//cout<<s<<endl;
      qe.push_back(s);
    }

//printf("%d %d %d  [%d]\n", ccc, se.size(), qe.size(), q);



    int maxindex=0;
    int count=0;
    while(maxindex<q) {
      int mmax=0;

      for(int i=0; i<se.size(); i++) {
        int index=-2;
//if(ccc==6) cout<<se[i]<<endl;
        for(int j=maxindex; j<qe.size(); j++) {
          if(qe[j]==se[i]) {
            index=j;
            break;
          }
        }
if(ccc==6) {
// cout<<maxindex<<" "<<index<<endl;
}
        if(index==-2) {
          maxindex=q;
          goto end;
        }


        if(index>mmax) {
          mmax=index;
        }
      }

      maxindex=mmax;
      if(maxindex<q) count++;
    }


    end:
    printf("Case #%d: %d\n", ccc+1, count);

  }


  return 0;
}

