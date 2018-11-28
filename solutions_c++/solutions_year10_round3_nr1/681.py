int N;
int WIRES; // wires

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;




int main()
{
  // Input
  scanf("%d\n",&N);
  fprintf(stderr,"N = %d: \n",N);

  // Output
  for (int x=1; x<=N; x++) {
    fprintf(stderr,"Case #%d: \n",x);

    scanf("%d\n",&WIRES);
    fprintf(stderr,"ropes %d\n",WIRES);
    vector< pair<int,int> > w;
    for (int i=1; i<=WIRES; i++) {
      int A,B;
      scanf("%d %d\n",&A,&B);
      w.push_back(make_pair(A,B));
    }
    sort(w.begin(),w.end());
    
    int isec = 0;
    for (int i=0; i<WIRES; i++) {
      // since all prev A are < me, find all B that are > me
      for (int j=0; j<i; j++) {
        if (w[j].second > w[i].second) isec++;
      }
    }
    
    printf("Case #%d: %d\n",x,isec);
  }
  return 0;
}
