#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;


int N;

int g(char c) { return (c - '0'); }
int m(int a)
{
	return (a < 0)?-a:a;
}
void solve(int iii)
{
	int t, na, nb;
	cin >> t >> na >> nb;
	int ai[100], ao[100], bo[100], bi[100], as[100], ae[100], bs[100], be[100];
	
	for (int i = 0; i < na; i++)
	{
		string str1, str2;
		cin >> str1;
		as[i] = (g(str1[0]) * 10 + g(str1[1])) * 60 + g(str1[3]) * 10 + g(str1[4]);
		cin >> str2;
		ae[i] = (g(str2[0]) * 10 + g(str2[1])) * 60 + g(str2[3]) * 10 + g(str2[4]);
	}
	for (int i = 0; i < nb; i++)
	{
		string str1, str2;
		cin >> str1;
		bs[i] = (g(str1[0]) * 10 + g(str1[1])) * 60 + g(str1[3]) * 10 + g(str1[4]);
		cin >> str2;
		be[i] = (g(str2[0]) * 10 + g(str2[1])) * 60 + g(str2[3]) * 10 + g(str2[4]);
	}
	int cnt = 0, ra = 0, rb = 0;
	bool aa[100], bb[100];
	memset(aa, false, sizeof(aa));
	memset(bb, false, sizeof(bb));
	
	while (cnt != na + nb)
	{
		int turn = -1, mn = 100000000, ind = -1;
		for (int i = 0; i < na; i++)
		{
			if (!aa[i] && as[i] < mn)
			{
				turn = 0;
				mn = as[i];
				ind = i;
			}
		}
		for (int i = 0; i < nb; i++)
		{
			if (! bb[i] && bs[i] < mn)
			{
				turn = 1;
				mn = bs[i];
				ind = i;
			}
		}
		cnt++;
		if (turn == 0)
		{
			ra++;
			aa[ind] = true;
		}
		else 
		{
			rb++;
			bb[ind] = true;
		}
		while (true)
		{
			if (turn == 0)
			{
				int mm = 1000000, mi = -1;
				for (int j = 0; j < nb; j++)
				{
					if (!bb[j] && bs[j] < mm && bs[j] >= ae[ind] + t)
					{
						mm = bs[j];
						mi = j;
						turn = 1;
					}
				}
				if (mi == -1)
					break;
				cnt++;
				ind = mi;
				bb[ind] = true;
			}

			if (turn == 1)
			{
				int mm = 1000000, mi = -1;
				for (int j = 0; j < na; j++)
				{
					if (!aa[j] && as[j] < mm && as[j] >= be[ind] + t)
					{
						mm = as[j];
						mi = j;
						turn = 0;
					}
				}
				if (mi == -1)
					break;
				cnt++;
				ind = mi;
				aa[ind] = true;
			}

		}
	}

	cout << "Case #" << iii + 1 << ": " << ra << ' ' << rb << endl;

}


int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> N;
	for (int i = 0; i < N; i++)
		solve(i);
	fclose(stdin);
	fclose(stdout);
	return 0;
}