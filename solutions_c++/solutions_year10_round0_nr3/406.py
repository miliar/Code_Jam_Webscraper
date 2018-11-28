#include <iostream>
#include <vector>
#include <string>
#include <regex.h>
#include <queue>
using namespace std;


int main() {
  int t;
  scanf("%d", &t);

  for(int iii=1; iii<=t; iii++) {
    int r, k, n;
    scanf("%d %d %d", &r, &k, &n);

//    queue<int> g;
    vector<int> g;
    for(int i=0; i<n; i++) {
      int aa;
      scanf("%d", &aa);
      g.push_back(aa);
    }

    vector<int> s; //s[i][j] is earnings starting at position i
    vector<int> numgroups;

    for(int i=0; i<n; i++) {
      int j=i;
      int num=0;
      int sum=0;
      while(num<n && sum+g[j]<=k) {
        sum+=g[j];
        j=(j+1)%n;
        num++;
      }

      s.push_back(sum);
      numgroups.push_back(j);
    }


    long long cost=0;
    int cur=0;
    for(int j=0; j<r; j++) {
      cost+=s[cur];
      //cur=(cur+numgroups[cur])%n;
      cur=numgroups[cur];
    }


    printf("Case #%d: %lld\n", iii, cost);



  }

  return 0;
}




