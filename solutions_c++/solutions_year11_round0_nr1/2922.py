//Bot Trust

#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int o_s[101];
int b_s[101];
int o[101];
int b[101];
int o_solve[101];
int b_solve[101];
int N, o_num, b_num;

void deal (fstream &ouf)
{
	int i = 0, j = 0, ans = 0, lock_o = 0, lock_b = 0, o_p = 1, b_p = 1;
	if (o_s[i] != -1)
	{
		lock_o = 1;
	}
	if (b_s[j] != -1)
	{
		lock_b = 1;
	}
	while (i < o_num || j < b_num)
	{
		if (i < o_num && o_p < o[i])
		{
			o_p++;
		}
		else if (i < o_num && o_p > o[i])
		{
			o_p--;
		}
		else if (i < o_num)
		{
			if (lock_o == 0)
			{
				i++;
			}
		}
		if (j < b_num && b_p < b[j])
		{
			b_p++;
		}
		else if (j < b_num && b_p > b[j])
		{
			b_p--;
		}
		else if (j < b_num)
		{
			if (lock_b == 0)
			{
				j++;
			}
		}
		if (i < o_num && o_s[i] >= j)
		{
			lock_o = 1;
		}
		else if (i < o_num)
		{
			lock_o = 0;
		}
		if (j < b_num && b_s[j] >= i)
		{
			lock_b = 1;
		}
		else if (j < b_num)
		{
			lock_b = 0;
		}
		if (i == o_num)
		{
			lock_b = 0;
		}
		if (j == b_num)
		{
			lock_o = 0;
		}
		ans++;
	}
//	printf("%d\n", ans);
	ouf << ans << endl;
}

int main()
{
	int T, i, pos, num = 1;
	fstream inf, ouf;
	inf.open("A-large.txt", ios::in);
	if (!inf)
	{
		exit(0);
	}
	ouf.open("result.txt", ios::out);
	if (!ouf)
	{
		exit(0);
	}
//	scanf("%d", &T);
	inf >> T;
	char ch;
	while (T > 0)
	{
//		scanf("%d", &N);
		inf >> N;
		o_num = b_num = 0;
//		memset(o_solve, -1, sizeof(o_solve));
//		memset(b_solve, -1, sizeof(b_solve));
		for (i = 0; i < N; i++)
		{
//			while (scanf("%c", &ch) && !isalpha(ch));
			while (inf >> ch && !isalpha(ch));
//			scanf("%d", &pos);
			inf >> pos;
			if (ch == 'O')
			{
				o_s[o_num] = b_num - 1;
				o[o_num++] = pos;
				o_solve[pos] = 0;
			}
			else
			{
				b_s[b_num] = o_num - 1;
				b[b_num++] = pos;
				b_solve[pos] = 0;
			}
		}
//		printf("Case #%d: ", num);
		ouf << "Case #" << num << ": ";
		deal(ouf);
		T--;
		num++;
	}
	inf.close();
	ouf.close();
	return 0;
}

/*
void deal()
{
	sort(o, o + o_num);
	sort(b, b + b_num);
	int ans = 0, i = 0, j = 0, flag = 0, o_p = 1, b_p = 1;
	while (i < o_num || j < b_num)
	{
		if (i < o_num && o_p == o[i])
		{
			i++;
			o_p++;
		}
		else if (j < b_num && b_p == b[j])
		{
			j++;
			b_p++;
		}
		else if (!flag && i < o_num)
		{
			o_p++;
		}
		else if (flag && j < b_num)
		{
			b_p++;
		}
		ans++;
		flag = 1 - flag;
	}
	printf("%d\n", ans);
}
*/

/*
void deal()
{
	int ans = 0, i = 0, j = 0, o_p = 1, b_p = 1, lock_o = 0, lock_b = 0, add, temp;
	bool o_move = false, b_move = false;
	if (o_s[0] != -1)
	{
		lock_o = 1;
	}
	else if (b_s[0] != -1)
	{
		lock_b = 1;
	}
	while (i < o_num || j < b_num)
	{
		add = -1;
		if (i < o_num)
		{
			add = (int)abs(o_p - o[i]);
			o_move = true;
			o_p = o[i];
			if (o_s[i] >= j)
			{
				lock_o = 1;
			}
			else
			{
				add++;
				o_move = false;
			    i++;
			}
		}
		if (j < b_num)
		{
			temp = (int)abs(b_p - b[j]);
			b_move = true;
			b_p = b[j];
			if (b_s[j] >= i)
			{
				lock_b = 1;
			}
			else
			{
				temp++;
				b_move = false;
			    j++;
			}
		}
		if (i < o_num && lock_o == 1 && o_s[i] < j)
		{
			lock_o = 0;
			if (o_move)
			{
				ans++;
				i++;
				o_move = false;
			}
		}
		if (j < b_num && lock_b == 1 && b_s[j] < i)
		{
			lock_b = 0;
			if (b_move)
			{
				ans++;
				j++;
				b_move = false;
			}
		}
		if (i < o_num && lock_o == 0 && o_s[i] >= j)
		{
			lock_o = 1;
		}
		if (j < b_num && lock_b == 0 && b_s[j] >= i)
		{
			lock_b = 1;
		}
		if (add == -1)
		{
			add = temp;
		}
		else if (temp > add)
		{
			add = temp;
		}
		if (add != -1)
		{
		    ans += add;
		}
	}
	printf("%d\n", ans);
}
*/