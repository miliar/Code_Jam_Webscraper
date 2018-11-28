#include<iostream>
#include<fstream>
using namespace std;

fstream inf, ouf;
int main()
{
	inf.open("f:\\C-large.in", ios::in);
	ouf.open("f:\\res.txt", ios::out);

	char *stt = "welcome to code jam";
	char st[501];
	int n;

	inf>>n;
	int total[502][20];
	inf.getline(st,1);
	for (int ti = 1; ti <= n; ++ti)
	{
		inf.getline(st,501);
		int len;
		len = strlen(st);
		int i;
		for (i = 0; i <= 18; ++i)
			total[len][i] = 0;
		total[len][19] = 1;
		int j;
		for (i = len - 1; i >= 0; --i)
		{
			total[i][19] = 1;
			for (j = 18; j >= 0; --j)
			{
				total[i][j] = total[i + 1][j];
				if (st[i] == stt[j])
					total[i][j] = (__int64(total[i + 1][j + 1]) + total[i][j]) % 10000;
			}
		}

		ouf << "Case #" << ti <<": ";
		int res;
		res = total[0][0] % 10000;
		ouf << res / 1000;
	//	cout << res / 1000;
		res %= 1000;
		ouf << res / 100;
	//	cout << res / 100;
		res %= 100;
		ouf << res /10;
	//	cout << res /10;
		res %= 10;
		ouf << res << endl;
	//	cout << res << endl;

	}

	inf.close();
	ouf.close();
	return 1;
}