#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int caseN;
	int N;
	int A[100], B[100];
	scanf("%d",&caseN);
	for(int cc=0;cc<caseN;cc++){
		int minsum = 2147483647;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%d",&A[i]);
		for(int i=0;i<N;i++)
			scanf("%d",&B[i]);
		sort(B,B+N);
		do{
			int sum=0;
			for(int i=0;i<N;i++)
				sum += A[i] * B[i];
			if(minsum > sum)
				minsum = sum;
		}while(next_permutation(B,B+N));
		printf("Case #%d: %d\n", cc+1, minsum);
	}
	return 0;
}
