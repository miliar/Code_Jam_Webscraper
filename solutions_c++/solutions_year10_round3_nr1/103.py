#include <cstdio>
#include <vector>
using namespace std;

int main()
{
  int cases;
  scanf("%d", &cases);
  for(int T=1; T<=cases; T++){
    printf("Case #%d: ", T);
    int ret=0;
    int N;
    scanf("%d", &N);

    vector <pair <int,int> > A(N);

    for(int i=0; i<N; i++) scanf("%d %d", &A[i].first, &A[i].second);

    for(int i=0; i<N; i++) 
      for(int j=0; j<i; j++){
	if( (A[i].first<A[j].first and A[i].second>A[j].second) or
	    (A[i].first>A[j].first and A[i].second<A[j].second) )
	  ret ++;
	    
      }

    printf("%d\n", ret);
  }
  return 0;
}
