#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))


int main(int argc, char **argv)
{
//	freopen("a.in","r",stdin);
	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

  int testcase, N, min, a, b, j, y;
  int A[1001]={0}, B[1001]={0};
  
  scanf("%d",&testcase);

  for (int caseId=1; caseId<=testcase; caseId++)
  {
	printf("Case #%d: ",caseId);
	y=0, a=0, b=0, min=10001, j=-1;
	
	scanf("%d", &N);
	
	for (int in=0; in<N; in++)
	{
	  scanf("%d %d", &A[in], &B[in]);
	  
	  if(A[in]<min || B[in]<min)
	  {
		min=MIN(A[in],B[in]);
		a=A[in];
		b=B[in];
		j=in;
	  }
	}
	
	for (int in=0; in<N; in++)
	{
	  if(in!=j && (A[in]<a && B[in]>b || A[in]>a && B[in]<b))
	  {
		y++;
	  }
	}
	
	printf("%d\n", y);
	
	fflush(stdout);
  }
  return 0;
}
