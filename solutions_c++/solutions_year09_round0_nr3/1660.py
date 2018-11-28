#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <Map>
#include <hash_set>
#include <exception>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

long long Count(char* s, int L1, int l1, char* t, int L2, int l2)
{
	if (l1 >= L1 && l2 < L2)
		return 0;

	long long count = 0;
	long long sum;
	char c1 = t[l2];
	int from = l1, end;

	if (l2 == L2 - 1)
	{
		for (int i=l1; i<L1; i++)
			if (s[i] == c1)
				count++;
		return count;
	}

	char c2 = t[l2+1];
	for (end = l1; end < L1; end++)
	{
		if (s[end] == c2)
		{
			sum = 0;
			for (int i= from; i<end; i++)
				if (s[i] == c1)
					sum++;

			if (sum > 0)
				count += sum * Count(s, L1, end, t, L2, l2+1) %10000;

			from = end;
		}
	}

	return count;
}

using namespace std;
using namespace stdext;


int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int N;
	char c[1000];
	string s;
	cin >> N ;
	cin.getline(c,1000);
	long long count;
	for (int i=0; i<N; i++)
	{
		cin.getline(c, 1000);
		s = c;
		
		string t = "welcome to code jam";
		count = Count((char*)s.data(),s.length(),0,(char*)t.data(),t.length(),0);

		cout << "Case #" << i+1 << ": ";
		count = count % 10000;
		if (count < 10)
			cout << "000";
		else if (count < 100)
			cout << "00";
		else if (count < 1000)
			cout << "0";
		cout << count << '\n';
	}


	return 0;
}