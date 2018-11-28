// gcg_B.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T,N,S,p;
	int t[200];

	cin >> T;
	int i,j;

	int num[200];

	for (i = 0;i < T;i++)
	{
		num[i] = 0;
		cin >> N >> S >> p;
		for (j = 0;j < N;j++)
		{
			cin >> t[j];
			if (t[j] < p)
			{
				continue;
			}
			if (t[j] > 3*(p-1))
			{
				num[i]++;
				continue;
			}
			if (S && t[j] >= p+2*(p-2))
			{
				S--;
				num[i]++;
			}
		}
	}

	for (i = 0;i < T;i++)
	{
		cout << "Case #" << i+1 << ": " << num[i] << endl;
	}
		
	return 0;
}

