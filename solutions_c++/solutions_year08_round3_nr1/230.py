
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int cmpGreater(const void* a, const void* b)
{
	int n1 = *((int*) a);
	int n2 = *((int*) b);

	return n1 - n2;
}

int cmpLesser(const void* a, const void* b)
{
	int n1 = *((int*) a);
	int n2 = *((int*) b);

	return -1*(n1 - n2);
}

const int MAX = 100000;

__int64 letterUses[MAX];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int caseCount;
	cin >> caseCount;
	for (int caseNum=1; caseNum<=caseCount; caseNum++)
	{
		int keyCapacity, keyCount, letterCount;
		cin >> keyCapacity >> keyCount >> letterCount;

		for (int i=0; i<letterCount; i++)
			cin >> letterUses[i];

		__int64 pressesNeeded = 1;
		__int64 keyUsed = 0;

		qsort(letterUses, letterCount, sizeof letterUses[0], cmpLesser);

		__int64 cnt = 0;
		for (int i=0; i<letterCount; i++)
		{
			cnt += pressesNeeded * letterUses[i];
			keyUsed++;

			if (keyUsed >= keyCount)
			{
				keyUsed = 0;
				pressesNeeded++;
				keyCapacity--;
			}
		}

		cout << "Case #" << caseNum << ": ";
		if (keyCapacity < 0)
			cout << "Impossible" << endl;
		else
			cout << cnt << endl;
	}

	return 0;
}


