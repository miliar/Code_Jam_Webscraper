int N;

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <assert.h>

using namespace std;

int main()
{
  // Input
  scanf("%d\n",&N);
  fprintf(stderr,"N = %d: \n",N);

  // Output
  for (int x=1; x<=N; x++) {
    fprintf(stderr,"Case #%d: \n",x);

    string str;
    getline(cin,str);
    stringstream ss(str);
    int N;
    ss >> N;
    fprintf(stderr,"N=%d\n", N);
    char r[100];
    int b[100];
    for (int i=0; i<N; i++) {
        ss >> r[i] >> b[i];
    }
    int bp[2], bt[2];
    bp[0] = bp[1] = 1;
    bt[0] = bt[1] = 0;
    for (int i=0; i<N; i++) {
        int k;
        k = r[i] == 'O' ? 1 :
            r[i] == 'B' ? 0 :
            -1;
        assert(k>-1);
        // move bot
        bt[k] += abs(bp[k] - b[i]);
        bp[k] = b[i];
        // wait for other bot to finish work
        bt[k] = max(bt[0], bt[1]);
        // press button
        bt[k] ++;

        //fprintf(stderr,"%c time = %d, pos = %d\n", r[i], bt[k], bp[k]);
    }
    int t = max(bt[0], bt[1]);

    printf("Case #%d: %d\n",x, t);
  }
  return 0;
}
