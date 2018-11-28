#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

int indices[19][500];
int sum[19][500];
int totalC[19];
int cur[19];

////////////////////////////////////
// WELCOME TO CODE JAM
// 0123456789012345678
// W = 0
// L = 2
// T = 8
// D = 13
// J = 16
// A = 17
// C = 3, 11
// M = 5, 18
// E = 1, 6, 14,
// O = 4, 9, 12
// ' '= 7, 10, 15
inline int getIndex(char c)
{
	switch(c)
	{
	case 'w': return 0;
	case 'e': return 1;
	case 'l': return 2;
	case 'c': return 3;
	case 'o': return 4;
	case 'm': return 5;
	case ' ': return 7;
	case 't': return 8;
	case 'd': return 13;
	case 'j': return 16;
	case 'a': return 17;
	}
	return -1;
}

void copyButFirst(int s, int d)
{
	if (totalC[s] <= 1) return;

	totalC[d] = totalC[s]-1;
	for (int i=1; i < totalC[s]; ++i)
		indices[d][i-1] = indices[s][i];
}

bool buildIndices(const std::string &str)
{
	memset(indices, 0, sizeof(indices));
	memset(sum, -1, sizeof(sum) );
	memset(cur, -1, sizeof(cur));
	memset(totalC, 0, sizeof(totalC));


	for (size_t i=0; i < str.length(); ++i)
	{
		int index = getIndex( str[i]);
		if (index == -1) continue;
		indices[ index][totalC[index]++ ] = i;
	}
	copyButFirst(3, 11);
	copyButFirst(5, 18);
	copyButFirst(1, 6);
	copyButFirst(6, 14);
	copyButFirst(4, 9);
	copyButFirst(9, 12);
	copyButFirst(7, 10);
	copyButFirst(10, 15);

	bool allSet = true;
	for (int i=0; i < 19; ++i)
		allSet = allSet && totalC[i] > 0;
	return allSet;
}

int countVals(int pos=0, int latestPos=-1)
{
	if (pos > 18) return 1;

	int i = 0;
	for (; i < totalC[pos] && (indices[pos][i] <= latestPos); ++i);
	if ( i >= totalC[pos]) return 0;

	int cv = 0;
	if (sum[pos][i] > -1)
	{
		for (; i < totalC[pos] ; ++i)
			cv = (cv + sum[pos][i])%10000;
	}
	else
	{
		for (; i < totalC[pos] ; ++i)
		{
			sum[pos][i] = countVals(pos+1, indices[pos][i]);
			cv = (cv + sum[pos][i])%10000;
		}
	}
	
	return cv;
}

int main()
{
	int c = 0;
	std::cin >> c;
	string str;
	std::getline( std::cin, str);
	for (int i=1; i <= c; ++i)
	{
		std::getline( std::cin, str);
		int count = 0;
		if (buildIndices(str))
			count = countVals();
		printf("Case #%d: %04d\n", i, count%10000);
	}
}