#include<cstdio>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for(int C=1; C<=T; ++C) {
    int A[1000], B[1000];
    int N;
    scanf("%d", &N);
    for(int i=0; i<N; ++i)
      scanf("%d%d", &A[i], &B[i]);
    int sol = 0;
    for(int i=0; i<N; ++i)
      for(int j=i+1; j<N; ++j)
	if((A[i]<A[j] && B[i]>B[j]) || (A[i]>A[j] && B[i]<B[j]))
	  sol++;
    printf("Case #%d: %d\n", C, sol);
  }
  return 0;
}
