#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

long long w[1000][1000];
long long g[1000];

// build the matrix w
// such that w[i][j] = g[i]+...g[(i+j)%N]
// notice that for each i, w[i,:] is an strictly increasing array
void buildw(int N)
{
	for(int i=0; i<N; i++) {
		w[i][0]=g[i];
		for(int j=1; j<N; j++) {
			w[i][j] = w[i][j-1]+g[(i+j)%N];
		}
	}
}

// binary search in the array a[start]...a[end], 
// for the biggest integer i such that a[start]+...+a[i] <=k 
int bsearch(long long* a, long long k, int start, int end)
{
	if(start==end) {
		if(a[start]<=k)
			return start;
		else
			return -1;
	}
	if(start+1==end) {
		if(a[end]<=k)
			return end;
		else if(a[start]>k)
			return -1;
		else // a[start] <=k <a[end]
			return start;
	}
	int mid = int((start+end)/2);
	if(a[mid]==k)
		return mid;
	else if (a[mid]>k)
		return bsearch(a, k, start, mid);
	else
		return bsearch(a, k, mid, end);
}

long long getmoney(int R, long long k, int N)
{
	buildw(N);
	long long t=0;
	int start=0;
	int end;
	for(int r=0; r<R; r++) {
		end = bsearch(w[start], k, 0, N-1);
		t += w[start][end];
		start = (start+end+1)%N;
	}
	return t;
}

int main()
{
	//freopen("D:\\tmp\\test.txt","r",stdin);freopen("D:\\tmp\\test.out","w",stdout);
	//freopen("D:\\tmp\\C-small.in","r",stdin);freopen("D:\\tmp\\C-small.out","w",stdout);
	freopen("D:\\tmp\\C-large.in","r",stdin);freopen("D:\\tmp\\C-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int R, N;
		long long k;
		cin >> R;
		cin >> k;
		cin >> N;
		for(int i=0; i<N; i++)
			cin >> g[i];
		long long result = getmoney(R, k, N);
		printf("Case #%d: ",caseId);
		printf("%lld", result);
		printf("\n");
	}

	return 0;
}