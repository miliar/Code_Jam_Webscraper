#include<cstdio>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for(int casen = 1; casen <= T; ++casen) {
    int N;
    int A[40];
    scanf("%d", &N);
    for(int i=0; i<N; ++i) {
      char s[64];
      scanf("%s", s);
      A[i] = 0;
      for(int j=0; j<N; ++j)
	if(s[j] == '1')
	  A[i] = j+1;
    }
    int sol=0;
    for(int i=0; i<N; ++i) {
      int j;
      if(A[i] <= i+1) continue;
      for(j=i+1; j<N; ++j)
	if(A[j] <= i+1)
	  break;
      for(int k=j; k>i; --k) {
	int t = A[k-1];
	A[k-1] = A[k];
	A[k] = t;
	sol++;
      }
    }
    printf("Case #%d: %d\n", casen, sol);
  }
  return 0;
}
