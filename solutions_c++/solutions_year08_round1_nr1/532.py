#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <ctime>
#include <algorithm>
#include <iostream>

using namespace std;


int main()
{

//////////////////////////////////////////////////////////////////////////


int T;
scanf("%d", &T);

for (int i = 1; i <= T; ++i)
{
	vector<__int64> va, vb;

	int n;
	scanf("%d", &n);
	for (int j = 1;j <= n; ++j)
	{
		__int64 a;
		scanf("%I64d", &a);
		va.push_back(a);
	}

	for (int j = 1;j <= n; ++j)
	{
		__int64 a;
		scanf("%I64d", &a);
		vb.push_back(a);
	}

	sort(va.begin(), va.end());
	sort(vb.begin(), vb.end());


	__int64 sum = 0;
	for(int j = 0;j<= n-1; ++j)
	{
		sum += va[j] * vb[n-j-1];
	}

	printf("Case #%d: %I64d\n", i, sum);

}



//////////////////////////////////////////////////////////////////////////
	long ti2 = clock();
	//cout << ti2 - ti1 << endl;
	return 0;
}