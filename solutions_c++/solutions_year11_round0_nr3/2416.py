int T;

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

int msb(int x) {
    int r = -1;
    while (x>0) {
        r++; x>>=1;
    }
    assert(r > -1);
    return r;
}

int maxnocry(int N, int c[1000]) {
    int xx = 0;
    int l = c[0];
    int sum = 0;
    for (int i=0; i<N; i++) {
        //fprintf(stderr,"c[%d]=%x\n", i, c[i]);
        xx ^= c[i];
        l = min(l, c[i]);
        sum += c[i];
    }
    if (xx != 0) return 0;
    return sum - l;
}

int main()
{
  // Input
  scanf("%d\n",&T);
  fprintf(stderr,"T = %d: \n",T);

  // Output
  for (int x=1; x<=T; x++) {
    fprintf(stderr,"Case #%d: \n",x);

    string str;
    int N;
    {
    getline(cin,str);
    stringstream ss(str);
    ss >> N;
    }
    //fprintf(stderr,"N=%d\n", N);
    getline(cin,str);
    stringstream ss(str);
    int c[1000];
    for (int i=0; i<N; i++) {
        ss >> c[i];
        //fprintf(stderr,"c[%d]=%x\n", i, c[i]);
    }

    int v = maxnocry(N,c);
    if (v)
        printf("Case #%d: %d\n",x, v);
    else
        printf("Case #%d: NO\n",x);
  }
  return 0;
}
