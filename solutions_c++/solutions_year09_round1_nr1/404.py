#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <hash_map>
#include <hash_set>
#include <exception>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;
using namespace stdext;

int h[11][10000];
char buffer[100000];
hash_set<int> ss;
hash_set<int>::iterator iterS;

int happy(int n, int base)
{
	while (n != 1)
	{
		if (ss.find(n) != ss.end())
		{
			for (iterS = ss.begin(); iterS != ss.end(); iterS++)
			{
				if (*iterS < 10000)
					h[base][*iterS] = 0;
			}
			return 0;
		}
		if (n<1000 && h[base][n] != -1)
		{
			int m = h[base][n];
			for (iterS = ss.begin(); iterS != ss.end(); iterS++)
			{
				if (*iterS < 10000)
					h[base][*iterS] = m;
			}
			return m;
		}

		itoa(n, buffer, base);

		char* cc;
		int sum = 0;
		for (cc = buffer; *cc != 0; cc++)
		{
			int c = *cc - '0';
			sum += c*c;
		}
		ss.insert(n);
		n = sum;
	}

	for (iterS = ss.begin(); iterS != ss.end(); iterS++)
	{
		if (*iterS < 10000)
			h[base][*iterS] = 1;
	}
	return 1;
}

int base[10];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	for (int i=0; i<11; i++)
		for (int j=0; j<10000; j++)
			h[i][j] = -1;

	string s;
	int T;
	int pre=0, pst;
	cin >> T ;
	cin.ignore();
	for (int i=1; i<=T; i++)
	{
		cin.getline(buffer, 1000);
		s.assign(buffer);
		pre = 0;
		pst = s.find(" ", pre);
		int size=0;
		while (pst != -1)
		{
			int ii = atoi(s.substr(pre, pst - pre).c_str());
			base[size++] = ii;
			
			pre = pst + 1;
			pst = s.find(" ", pre);
		}
		
		pst = s.length();
		int ii = atoi(s.substr(pre, pst - pre).c_str());
		base[size++] = ii;

		bool state;
		int k;
		for (k=2; ;k++)
		{
			state = true;
			for (int j=0; j<size; j++)
			{
				ss.clear();
				if (happy(k,base[j]) == false)
				{
					state = false;
					break;
				}
			}
			if (state)
				break;
		}
			
		cout << "Case #" << i << ": " << k << endl;
	}

	return 0;
}