#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <list>
#include <vector>
#include <set>
#include <map>

using namespace std;

int a[1001]; // stores the permutation
int b[1001]; // whether the number has been visited
double f[1001]; // f[n]=average time for a n-cycle

void build_f()
{
  f[1] = 0;
  f[2] = 2;
  double sum = 1;
  for(int n=3; n<=1000; n++) {
    sum += f[n-1]/(n-1);
    f[n] = sum/(1-1.0/n);
  }
}


int main()
{

  build_f();

	//freopen("test.txt","r",stdin);freopen("test.out","w",stdout);
	//freopen("D-small.in","r",stdin);freopen("D-small.out","w",stdout);
	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
    int N;
    cin >> N;
    for(int i=1; i<=N; i++) {
      cin >> a[i];
      b[i] = 0;
    }

    double sum=0;
    int nsorted=0; 
    while(nsorted != N) {
      int k0=-1;
      // find first nonzero b[i], and save pos at k0
      for(int i=1; i<=N; i++) {
        if(b[i]==0) {
          k0 = i;
          break;
        }
      }
      // starting at k0, trace the cycle
      int csize = 1;
      int k=k0;
      b[k0]=1;
      while(a[k] != k0) {
        k = a[k];
        b[k] = 1;
        csize++;
      }
      sum += f[csize];
      nsorted += csize;
    }

		printf("Case #%d: ",caseId);
		printf("%lf", sum);
		printf("\n");
	}

	return 0;
}
