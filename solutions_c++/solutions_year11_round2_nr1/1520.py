#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

char *m;
int N;
double *wp, *owp, *oowp;

double wp0(int j) {
  int i,w=0,p=0;

  for(i=0;i<N;i++) {
    if (m[j*N+i] != '.') p++;
    if (m[j*N+i] == '1') w++;
  }

  if (p!=0)
    return ((double)w) / ((double)p);
  else
    return 0.0;
}

double wp1(int j, int exc) {
  int i,w=0,p=0;

  for(i=0;i<N;i++) {
    if (i==exc) continue;
    if (m[j*N+i] != '.') p++;
    if (m[j*N+i] == '1') w++;
  }

  if (p!=0)
    return ((double)w) / ((double)p);
  else
    return 0.0;
}



double owp0(int j) {
  int i;
  double sum=0.0, n=0.0;

  for(i=0;i<N;i++)  {
    if (m[j*N+i] != '.') { 
      sum += wp1(i,j);
      n++;
    }
  }
  if (n!=0.0)
    return(sum/n);
  else
    return 0.0;
}

double oowp0(int j) {
  int i;
  double sum=0.0, n=0.0;

  for(i=0;i<N;i++) {
    if (m[j*N+i] != '.') {
      sum += owp[i];
      n++;
    }
  }
  if (n!=0.0)
    return(sum/n);
  else
    return 0.0;
}

int main() {

  int i,T,j,k;
  char c;
  double rpi;

  cin >> T;

  for(i=1;i<=T;i++) {
    cin >> N;
    m = new char[N*N];
    for(j=0;j<N*N;j++) {
      do { cin >> c; } while (c!='.' && c!='1' && c!='0');
      m[j] = c;
    }
    
    wp = new double[N];
    owp = new double[N];
    oowp = new double[N];

    for(j=0;j<N;j++)
      wp[j] = wp0(j);

    for(j=0;j<N;j++)
      owp[j] = owp0(j);

    for(j=0;j<N;j++)
      oowp[j]  = oowp0(j);

    cout << "Case #" << i << ":\n";
    for(j=0;j<N;j++) {
      rpi = wp[j]/4.0 + owp[j]/2.0 + oowp[j]/4.0;
      printf("%.8f\n",rpi);
    }

    delete m;
    delete wp;
    delete owp;
    delete oowp;
  }

  return 0;
}
