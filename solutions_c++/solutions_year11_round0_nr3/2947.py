//Candy Splitting

#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;

int N, sum, count, a, all, ans, number;
int C[1001];
int s[1001];

void search (int i)
{
	if (number > 0 && number < N && count == (count ^ a))
	{
		if (sum > ans)
		{
			ans = sum;
		}
		if (all - sum > ans)
		{
			ans = all - sum;
		}
	}
	if (i >= N)
	{
		return;
	}
	int last_count = count;
	sum += C[i];
	count = (count ^ C[i]);
	s[number] = C[i];
	number++;
	search(i + 1);
	number--;
	sum -= C[i];
	count = last_count;
	search(i + 1);
}

void deal (fstream &ouf)
{
	a = number = ans = sum = count = all = 0;
	int i;
	for (i = 0; i < N; i++)
	{
		all += C[i];
		a = (a ^ C[i]);
	}
	search(0);
	if (!ans)
	{
//		printf("NO\n");
		ouf << "NO" << endl;
	}
	else
	{
//		printf("%d\n", ans);
		ouf << ans << endl;
	}
}

int main()
{
	int num = 1, i, T;
	fstream inf, ouf;
	inf.open("C-small-attempt2.txt", ios::in);
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
	while (T > 0)
	{
//		scanf("%d", &N);
		inf >> N;
		for (i = 0; i < N; i++)
		{
//			scanf("%d", &C[i]);
			inf >> C[i];
		}
//		printf("Case #%d: ", num);
		ouf << "Case #" << num << ": ";
		num++;
		deal(ouf);
		T--;
	}
	inf.close();
	ouf.close();
	return 0;
}