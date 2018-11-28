#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) forn(i, v.size())

int n, k, R;
int a[10000];

long long earn[10000];
int len[10000];
bool used[10000];
long long currentEarn[10000];
int currentLength[10000];

int startCycleIndex;

int cycleLength;
int preCycleLength;

long long cycleEarn;
long long preCycleEarn;

long long answer;

bool findCycle()
{
	int index = 0;
	memset(used, 0, sizeof(used));
	
	long long totalEarn = 0;
	int totalLength = 0;
	int i = 0;
	while (!used[index] && i < R)
	{
		currentEarn[index] = totalEarn;
		currentLength[index] = totalLength;
		
		totalEarn += earn[index];
		totalLength++;

		used[index] = true;
		index = (index + len[index]) % n;
		i++;
	}

	if (i == R)
	{
		answer = totalEarn;
		return false;
	}

	cycleEarn = totalEarn - currentEarn[index];
	preCycleEarn = currentEarn[index];

	if (i == 1)
	{
		cycleLength = 1;
		preCycleLength = 0;
	} 
	else
	{
		cycleLength = totalLength - currentLength[index];
		preCycleLength = i - cycleLength;//currentLength[index];
	}
	startCycleIndex = index;
	return true;
}

long long getEarn(int startIndex)
{
	long long result = 0;
	for (int i = startIndex; i < startIndex + n; ++i)
	{
		if (result + a[i] > k)
			break;

		result += a[i];
	}

	return result;
}

int getLen(int startIndex)
{
	int result = 0;
	long long sum = 0;
	for (int i = startIndex; i < startIndex + n; ++i)
	{
		if (sum + a[i] > k)
			break;

		sum += a[i];
		result++;
	}

	return result;
}

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	forn(test, tests)
	{
		cin >> R >> k >> n;
		forn(i, n)
		{
			scanf("%d", &a[i]);
			a[n + i] = a[i];
		}

		forn(i, n)
		{
			earn[i] = getEarn(i);
			len[i] = getLen(i);
		}

		if (!findCycle())
		{
			printf("Case #%d: %I64d\n", test + 1, answer);
			continue;
		}
		
		answer = preCycleEarn + ((R - preCycleLength) / cycleLength) * cycleEarn;

		R = (R - preCycleLength) % cycleLength;
		int index = startCycleIndex;
		forn(i, R)
		{
			answer += earn[index];
			index = (index + len[index]) % n;
		}

		printf("Case #%d: %I64d\n", test + 1, answer);
	}

	return 0;
}