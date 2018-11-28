#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int it=0;it<T;it++) {
		int n;
		scanf("%d",&n);
		vector<int> A(n);
		vector<int> B(n);
		for(int i=0;i<n;i++) {
			int x,y;
			scanf("%d %d",&x,&y);
			A[i] = x;
			B[i] = y;
		}
		int total = 0;
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(A[j]>A[i] && B[j]<B[i]) {
					total++;
				}
				if(A[j]<A[i] && B[j]>B[i]) {
					total++;
				}
			}
		}
		printf("Case #%d: %d\n",it+1,total/2);
	}
	return 0;
}
