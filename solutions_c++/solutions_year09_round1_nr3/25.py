
//Written by Alex Hamed Ahmadi - alex@hamedahmadi.com

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)
#define FORIT(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define P(x) cerr<<#x<<" = "<<x<<endl;
#define pb push_back

const int ctop=110;
//typedef long long int ll;
double C[ctop][ctop];
void calc() {
    C[0][0]=1;
    for (int m=1;m<ctop;m++) {
      C[m][0]=1;
      for (int i=1;i<=m;i++) C[m][i]=C[m-1][i-1]+C[m-1][i];
    }
}

double d[100];

double getc(int n, int k) {
  if (k>n) return 0;
  if (n<0) return 0;
  if (k<0) return 0;
  if (n==k) return 1;
  if (k==0) return 1;
  return C[n][k];
}

int main() {
  calc();

  int nt;
  cin>>nt;
  for (int T=1;T<=nt;T++) {

    int n, c;
    cin>>c>>n;
    d[0]=0;
    for (int i=1;i<=c;i++) {
      d[i]=1;

      double pbad = getc(i,0)*getc(c-i,n)/getc(c,n);
      double pgood = 1-pbad;

      for (int k=1;k<=i;k++) {//cover k with this pack
	double p=getc(i,k)*getc(c-i,n-k) / getc(c,n);
	p/=pgood;
	d[i]+=p*(d[i-k]);
      }

      d[i] = (d[i]*pgood + pbad) / pgood;

    }

    printf("Case #%d: %.8f\n", T, d[c]);
  }

  return 0;
}
