
#pragma comment(linker, "/STACK:268435456")

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

const int MAX = 128;

int length;
char m[MAX];

__int64 uglyCount;

int IsUgly(__int64 num)
{
	if (num < 0)
		return IsUgly(-1 * num);

	if (num % 2 == 0)
		return 1;

	if (num % 3 == 0)
		return 1;

	if (num % 5 == 0)
		return 1;

	if (num % 7 == 0)
		return 1;

	return 0;
}

__int64 Calc(__int64 prev, char op, __int64 cur)
{
	if (op == '+')
		return prev + cur;

	return prev - cur;
}

void ProcessNext(__int64 prev, char op, __int64 cur, int pos);

void GoSpace(__int64 prev, char op, __int64 cur, int pos)
{
	// ' '	
	cur *= 10;
	cur += (__int64) (m[pos] - '0');
	ProcessNext(prev, op, cur, pos+1);
}

void GoPlus(__int64 prev, char op, __int64 cur, int pos)
{
	// '+'	
	prev = Calc(prev, op, cur);
	cur = (__int64) (m[pos] - '0');
	op = '+';
	ProcessNext(prev, op, cur, pos+1);
}

void GoMinus(__int64 prev, char op, __int64 cur, int pos)
{
	// '-'	
	prev = Calc(prev, op, cur);
	cur = (__int64) (m[pos] - '0');
	op = '-';
	ProcessNext(prev, op, cur, pos+1);
}

void ProcessNext(__int64 prev, char op, __int64 cur, int pos)
{
	if (pos >= length)
	{
		if (IsUgly(Calc(prev, op, cur)))
			uglyCount++;
		return;
	}

	if (pos > 0)
	{
		GoSpace(prev, op, cur, pos);
		GoMinus(prev, op, cur, pos);
	}

	GoPlus(prev, op, cur, pos);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int caseCount;
	cin >> caseCount;
	cin.getline(m, MAX);
	for (int caseNum=1; caseNum<=caseCount; caseNum++)
	{
		cin.getline(m, MAX);
		length = strlen(m);
		uglyCount = 0;
		
		ProcessNext(0, '+', 0, 0);

		cout << "Case #" << caseNum << ": ";
		cout << uglyCount << endl;
	}

	return 0;
}


