#include <iostream>
#include <cstdio>
using namespace std;

#define gout case_number++, printf("Case #%d: ", case_number), cout
#define REP(i,n) for(i=0;i<n;i++)

int case_number;

long long int a[101], b[101];
int A[101], B[101];

long long int assemble (int x, int y, long long int ax, long long int by);
int main()
{
	int test_case, m, n, i, j, k;
	scanf ("%d", &test_case);

	while (test_case--)
	{
		REP(i,101) a[i] = b[i] = A[i] = B[i] = 0;//
		
		scanf ("%d %d", &n, &m);
		
		REP(i,n) cin >> a[i] >> A[i];
		REP(i,m) cin >> b[i] >> B[i];
		
		gout << assemble (n-1, m-1, a[n-1], b[m-1]) << endl;
	}	
		
	return 0;
}

long long int assemble (int x, int y, long long int ax, long long int by)
{
	if (x == -1) return 0LL;
	if (y == -1) return 0LL;
	
	if (A[x] != B[y]){
		
		long long int t1, t2;
		t1 = assemble (x-1, y, a[x-1], by);
		t2 = assemble (x, y-1, ax, b[y-1]);
		
		return max (t1, t2);
	}
	else
	{
		if (ax == by){
			return (ax + assemble (x-1, y-1, a[x-1], b[y-1]));
		}
		
		else
		{
			if (ax > by) return (by + assemble (x, y-1, ax-by, b[y-1]));
			else return (ax + assemble (x-1, y, a[x-1], by-ax));
		}
	}
	
}
