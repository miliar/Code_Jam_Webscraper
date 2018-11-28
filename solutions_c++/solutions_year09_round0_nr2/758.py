#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

struct DATA
{
	int a;
	int p;
	char l;
};

DATA mp[10000];
int H, W;

void ReadMap()
{
	cin >> H >> W;
	for (int i = 0; i < H; i ++)
		for (int j = 0; j < W; j ++)
		{
			cin >> mp[i * W + j].a;
			mp[i * W + j].p = i * W + j;
			mp[i * W + j].l = 0;
		}
	return;
}
int Nbr(int i, int j)
{
	int n, w, e, s;
	int dn, dw, de, ds;
	int d = mp[i * W + j].a;
	if (i - 1 < 0)
	{
		n = -1;
		dn = 999999;
	}
	else
	{
		n = (i - 1) * W + j;
		dn = mp[n].a;
	}
	if (j - 1 < 0)
	{
		w = -1;
		dw = 999999;
	}
	else
	{
		w = i * W + j - 1;
		dw = mp[w].a;
	}
	if (j + 1 >= W)
	{
		e = -1;
		de = 999999;
	}
	else
	{
		e = i * W + j + 1;
		de = mp[e].a;
	}
	if (i + 1 >= H)
	{
		s = -1;
		ds = 999999;
	}
	else
	{
		s = (i + 1) * W + j;
		ds = mp[s].a;
	}
	if (dn < d && dn <= de && dn <= ds && dn <= dw) return n;
	if (dw < d && dw < dn && dw <= de && dw <= ds) return w;
	if (de < d && de < dn && de < dw && de <= ds) return e;
	if (ds < d && ds < dn && ds < dw && ds < de) return s;
	return -1;
}
void Ufs()
{
	for (int i = 0; i < H; i ++)
		for (int j = 0; j < W; j ++)
		{
			int pos = i * W + j;
			int nbr = Nbr(i, j);
			if (nbr != -1)
			{
				mp[pos].p = mp[nbr].p;
			}
		}
	return;
}
void Label()
{
	char l = 'a';
	for (int i = 0; i < H; i ++)
		for (int j = 0; j < W; j ++)
		{
			int pos = i * W + j;
			int root = pos;
			int cur = pos;
			while (mp[root].p != root) root = mp[root].p;
			while (mp[cur].p != cur)
			{
				mp[cur].p = root;
				cur = mp[cur].p;
			}
			if (mp[root].l == 0)
			{
				mp[root].l = l;
				mp[pos].l = l;
				l ++;
			}
			else
			{
				mp[pos].l = mp[root].l;
			}
		}
	return;
}
void WriteLabel()
{

	for (int i = 0; i < H; i ++)
	{
		for (int j = 0; j < W; j ++)
		{
			int pos = i * W + j;
			cout << mp[pos].l << " ";
		}
		cout << endl;
	}
}
int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i ++)
	{
		ReadMap();
		Ufs();
		Label();
		cout << "Case #" << i + 1 << ":" << endl;
		WriteLabel();
	}
	return 0;
}
