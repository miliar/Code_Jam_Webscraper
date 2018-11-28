
//Written by Alex Hamed Ahmadi - alex@hamedahmadi.com

#include <iostream>
#include <cstring>
#include <string>
#include <cassert>
#include <algorithm>
#include <cstdio>

using namespace std;

const int maxlen=1000;

char a[maxlen];
char b[]="welcome to code jam";

int m,n;

int d[maxlen][maxlen];

const int mod = 10000;

int main() {

  n=strlen(b);

  cin.getline(a, maxlen);
  int nt=atoi(a);
  for (int T=1;T<=nt;T++) {
    cin.getline(a, maxlen);
    m=strlen(a);

    memset(d, 0, sizeof d);

    for (int i=0;i<=m;i++)
      d[i][n]=1;

    for (int i=m-1;i>=0;i--) {
      for (int j=0;j<n;j++) {
	d[i][j] = d[i+1][j];
	if (a[i]==b[j]) {
	  d[i][j] += d[i+1][j+1];
	  if (d[i][j]>=mod) d[i][j]-=mod;
	}
      }
    }
    cerr<<d[0][0]<<endl;

    printf("Case #%d: %04d\n", T,  d[0][0]);
  }

  return 0;
}
