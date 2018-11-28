#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

long long a[40];

// get to the position such that a[start]<=x<a[end+1] 
int findresult(long long x, int start, int end)
{
	int count = 0;
	int mid;
	while(end-start > 1) {
		mid = (start+end)/2;
		if(a[mid]==x) {
			count ++;
			break;
		}
		else if (a[mid<x]) {
			count ++;
			start = mid;
		}
		else { // a[mid]>x
			end = mid;
			count ++;
		}
	}
	return count;

}

int main()
{
	//freopen("D:\\tmp\\test.txt","r",stdin);freopen("D:\\tmp\\test.out","w",stdout);
	//freopen("D:\\tmp\\B-small.in","r",stdin);freopen("D:\\tmp\\B-small.out","w",stdout);
	freopen("D:\\tmp\\B-large.in","r",stdin);freopen("D:\\tmp\\B-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		long long L, P, C;
		cin >> L >> P >> C;
		int N=0;
		long long tmp=L;
		do {
			a[N] = tmp;
			tmp = tmp*C;
			N++;
		}
		while(tmp<P);
		a[N]=P;
		int result = findresult(a[N-1], 0, N);
		printf("Case #%d: ",caseId);
		printf("%d", result);
		printf("\n");
		fflush(stdout);
	}

	return 0;
}