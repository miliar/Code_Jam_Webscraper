#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int maxk = 16;

int perm[maxk];
int k, len;
string s;
string sx;
int mini;
bool used[maxk];

void computerle()
{
	for (int i=0; i<len / k; i++)
	{
		int base = i*k;
		for (int j=0; j<k; j++)
			sx[base+j] = s[base+perm[j]];
	}
	char last = sx[0];
	int count = 1;
	for (int i=1; i<len; i++)
	{
		if (sx[i] != last)
		{
			last = sx[i];
			count++;
		}
	}
	if (count < mini)
		mini = count;
}

void sub(int l)
{
	if (l == k)
	{
		computerle();
	}
	else
	{
		for (int i=0; i<k; i++)
			if (!used[i])
			{
				used[i] = true;
				perm[l] = i;
				sub(l+1);
				used[i] = false;
			}
	}
}

int main()
{
	int N;
	cin >> N;
	for (int tc = 0; tc < N; tc++)
	{
		cin >> k;
		getline(cin,s);
		getline(cin,s);
		len = s.length();
		mini = len + 10;
		sx = s;
		sub(0);
		cout << "Case #" << tc+1 << ": " << mini << endl;
	}
}

