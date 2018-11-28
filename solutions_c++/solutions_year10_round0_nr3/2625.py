#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <queue>

using namespace std;

int t,r,k,n,g,x,res;
queue <int> q;

int main () {
  freopen ("input","r",stdin);
  freopen ("output","w",stdout);
  scanf ("%d",&t);
  for (int i=0; i<t; i++) {
    scanf ("%d%d%d",&r,&k,&n);
    for (int j=0; j<n; j++) {
      scanf ("%d",&g);
      q.push(g);
    }
    for (int j=0; j<r; j++) {
      for (int p=0; p<n; p++) {
        x+=q.front();
        if (x>k) {
          x=0;
          break;
        }
        q.push(q.front());
        res+=q.front();
        q.pop();
      }
      x=0;
    }
    cout << "Case #" << i+1 << ": " << res << endl;
    res=0;
    x=0;
    while (!q.empty()) q.pop();
  }
  return 0;
}