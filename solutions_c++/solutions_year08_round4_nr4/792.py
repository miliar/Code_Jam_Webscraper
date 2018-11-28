
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int Calc(vector<int> v, int k, char* stOld)
{
	char* stNew = new char[1024];
	strcpy(stNew, stOld);

	int len = strlen(stNew);
	for (int pos=0; pos < len; pos+=k)
	{
		for (int j=0; j<k; j++)
			stNew[pos+v[j]] = stOld[pos+j];
	}

	int res = 1;
	for (int i=1; i<len; i++)
	{
		if (stNew[i] != stNew[i-1])
			res++;
	}

	return res;
}

char st[1024];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int caseCount;
	cin >> caseCount;
	for (int caseNum=1; caseNum<=caseCount; caseNum++)
	{
		vector<int> v;
		v.clear();

		int k;
		cin >> k;
		cin.getline(st, 1024);
		cin.getline(st, 1024);

		for (int i=0; i<k; i++)
		{
			v.push_back(i);
		}

		int min = 2 * strlen(st);

		do 
		{
			int cur = Calc(v, k, st);
			if (cur < min)
				min = cur;
		}
		while (next_permutation(v.begin(), v.end()));
		
		cout << "Case #" << caseNum << ": ";
		cout << min << endl;
	}

	return 0;
}


