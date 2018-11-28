#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;



void multi(int N[], int J, int& l)
{
	for (int i = 0; i < l; ++i )
	{
		N[i] *= J;
	}

	int ji = 0;
	
	while (ji <= 998)
	{
		N[ji+1] += N[ji]/10;
		N[ji] %= 10;
		++ji;
	}
	l = 1;
	for (ji = 1; ji <= 998; ++ji )
	{
		if (N[ji])
			l = ji + 1;
	}
}

void add(int M[], int&m, int N[], int n)
{
	int l = max(m,n);
	for (int i = l-1; i >=0; --i)
	{
		M[i] += N[i];
	}
	m = l;
}

void print(int N[], int l)
{
	for (int j = l-1; j >=0; --j)
	{
		printf("%d", N[j]);
	}
}

int main()
{

	int T;
	cin >> T;
	for (int tc =	0; tc < T; ++tc)
	{
		char tmp[100] = {0};
		int mm[256] = {0};
		memset(mm, -1, sizeof mm);
		int org[100] = {0};
		cin >> tmp;
		int l = strlen(tmp);
		
		reverse(tmp, tmp+l);

		mm[tmp[l-1]] = 1;
		org[l-1] = 1;

		int tmpLL = l-2;
		while (tmpLL >= 0 && tmp[tmpLL] == tmp[l-1])
		{
			org[tmpLL] = org[l-1];
			--tmpLL;
		}

		if (tmpLL >= 0)
		{
			mm[tmp[tmpLL]] = 0;
			org[tmpLL] = 0;
		}

		int next = 2;
		for (int i = tmpLL-1; i >= 0; --i)
		{
			if (mm[tmp[i]] != -1)
			{
				org[i] = mm[tmp[i]];
			}
			else
			{
				mm[tmp[i]] = next++;
				org[i] = mm[tmp[i]];
			}
		}

		int res[1000] = {0};
		int resL = 1;

		int mer[1000] = {1};
		int merL = 1;

		for (int j = 0; j < l; ++j)
		{
			int tmpR[1000] = {0};
			int tmpRL = 1;
			
			memcpy(tmpR, mer,sizeof tmpR);
			tmpRL = merL;

			multi(tmpR, org[j], tmpRL);

			add(res, resL, tmpR, tmpRL);
			multi(res, 1, resL);
			multi(mer, next, merL);
		}
		
		printf("Case #%d: ", tc+1);
		print(res, resL);
		printf("\n");

	}
	return 1;
}