#include <iostream>
#include <sstream>
#include <memory>
#include <iostream>
using namespace std;

int mul[2][2], tmp[2][2], ans[2][2];

void calc(int p)
{
	if (p < 1) return;
	if (p == 1)
	{
		memmove(ans, mul, sizeof(ans));
	}
	else
	{
	//	cout << "$" << p << endl;
		calc(p / 2);
		memset(tmp, 0, sizeof(tmp));
		for (int k = 0; k < 2; k ++)
			for (int i = 0; i < 2; i ++)
				for (int j = 0; j < 2; j ++)
					tmp[i][j] = (tmp[i][j] + ans[i][k] * ans[k][j]) % 1000;
		memmove(ans, tmp, sizeof(ans));
		if (p % 2)
		{
			memset(tmp, 0, sizeof(tmp));
			for (int k = 0; k < 2; k ++)
				for (int i = 0; i < 2; i ++)
					for (int j = 0; j < 2; j ++)
						tmp[i][j] = (tmp[i][j] + mul[i][k] * ans[k][j]) % 1000;
			memmove(ans, tmp, sizeof(ans));
		}
		/*
		for (int i = 0; i < 2; i ++)
		{
			for (int j = 0; j < 2; j ++)
				cout << ans[i][j] << " ";
			cout << endl;
		}
		*/
	}
}

int main()
{
	mul[0][0] = 0; mul[0][1] = 996;
	mul[1][0] = 1; mul[1][1] = 6;
	int _T;
	cin >> _T;
	for (int T = 1; T <= _T; T ++)
	{
		int N;
		cin >> N;
		calc(N - 1);
		stringstream tmp; tmp.clear(); tmp << (2 * ans[0][1] + 6 * ans[1][1] + 999) % 1000;
		string ss = tmp.str(); while (ss.size() < 3) ss = "0" + ss;
		cout << "Case #" << T << ": " << ss << endl;
	}	
}
