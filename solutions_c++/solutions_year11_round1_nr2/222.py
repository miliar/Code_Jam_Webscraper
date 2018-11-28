#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 128;

string dic[MAXN], ec[MAXN];
int dv[MAXN], ev[MAXN];
int v[26], rv[26];

int check(string &kk, string &l, int n, int dk)
{
	int ans = 0, en = n;
	
	for (int k = 0; k < en; k ++)
	{
		bool bRemove = kk.size() != ec[k].size();
		if (bRemove)
		{
			swap(ec[k], ec[en-1]);
			swap(ev[k], ev[en-1]);
			en --;   k --;
			for (int j = 0; j < 26; j ++)
				if ((1 << j) & ev[en])
					v[j] --;
		}
	}

	for (int i = 0; i < 26 && dk > 0; i ++)
	{
		int z = l[i] - 'a';
		if (v[z] == 0)  continue;
		if (((1 << z) & dk) == 0)
		{
			ans ++;  
			for (int k = 0; k < en; k ++)
			{
				bool bRemove = false;
				bRemove = ((1 << z) & ev[k]) > 0;
				if (bRemove)
				{
					swap(ec[k], ec[en-1]);
					swap(ev[k], ev[en-1]);
					en --;   k --;
					for (int j = 0; j < 26; j ++)
						if ((1 << j) & ev[en])
							v[j] --;
				}
			}
		} else {
			dk -= 1 << z;
			for (int k = 0; k < en; k ++)
			{
				bool bRemove = false;
				for (int j = 0; j < kk.size() && (!bRemove); j ++)
					if ((kk[j] == l[i] && ec[k][j] != l[i])||
						(kk[j] != l[i] && ec[k][j] == l[i]))  bRemove = true;
				if (bRemove)
				{
					swap(ec[k], ec[en-1]);
					swap(ev[k], ev[en-1]);
					en --;   k --;
					for (int j = 0; j < 26; j ++)
						if ((1 << j) & ev[en])
							v[j] --;
				}
			}
		}
	}
	return ans;
}

int work()
{
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i ++)
	{
		cin >> dic[i];
		ec[i] = dic[i];
	}

	memset(rv, 0, sizeof(rv));
	memset(dv, 0, sizeof(dv));
	for (int i = 0; i < n; i ++)
	{	
		memset(v, 0, sizeof(v));
		for (int j = 0; j < dic[i].size(); j ++)
		{
			v[dic[i][j]-'a'] ++;
			dv[i] |= 1 << (dic[i][j] - 'a');
		}
		for (int j = 0; j < 26; j ++)
			if (v[j])  rv[j] ++;
	}

	memcpy(ev, dv, sizeof(ev));

	string lis;
	for (int i = 0; i < m; i ++)
	{
		int mx = -1, mk;
		cin >> lis;
		for (int k = 0; k < n; k ++)
		{
			memcpy(v, rv, sizeof(rv));
			int z = check(dic[k], lis, n, dv[k]);
			if (z > mx)
			{
				mx = z;  mk = k;
			}
		}
		cout << " " << dic[mk];
	}
	cout << endl;
	return 0;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
	{
		cout << "Case #" << k << ":";
		work();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}