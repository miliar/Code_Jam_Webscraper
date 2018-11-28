#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;

int n,t,k;

int pow(int x,int y) {
  int ret=1;
  for (int i=1; i<=y; i++) {
    ret*=x;
  }
  return ret;
}

int main () {
  freopen ("input","r",stdin);
  freopen ("output","w",stdout);
  scanf ("%d",&t);
  for (int i=0; i<t; i++) {
    scanf ("%d%d",&n,&k);
    if (k%pow(2,n)==pow(2,n)-1) cout << "Case #" << i+1 << ": " << "ON" << endl; else cout << "Case #" << i+1 << ": " << "OFF" << endl;
  }
  return 0;
}