#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int GetAnswer(string ptn, string sz)
{
	int arr[500];
	int nsz = sz.size();
	int nptn = ptn.size();
	if (sz[0] == ptn[0]) arr[0] = 1;
	else arr[0] = 0;
	for (int i = 1; i < nsz; i ++)
	{
		if (sz[i] == ptn[0]) arr[i] = (arr[i -1] + 1) % 10000;
		else arr[i] = arr[i - 1];
	}
	for (int i = 1; i < nptn; i ++)
	{
		for (int j = 0; j < nsz; j ++)
		{
			if (j < i) arr[j] = 0;
			else
			{
				if (sz[j] == ptn[i]) arr[j] = (arr[j - 1] + arr[j]) % 10000;
				else arr[j] = arr[j - 1];
			}
		}
	}
	return arr[nsz - 1];
}
int main()
{
	string sz;
	string ptn = "welcome to code jam";
	int N;
	cin >> N;
	getline(cin, sz);
	for (int i = 0; i < N; i ++)
	{
		getline(cin, sz);
		int cnt = GetAnswer(ptn, sz);
		cout << "Case #" << i + 1 << ": ";
		cout << cnt / 1000;
		cnt = cnt % 1000;
		cout << cnt / 100;
		cnt = cnt % 100;
		cout << cnt / 10;
		cnt = cnt % 10;
		cout << cnt << endl;
	}
	return 0;
}