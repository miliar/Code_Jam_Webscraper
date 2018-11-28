#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");
#define cin fin
#define cout fout

char s[30] = "welcome to code jam";
char data[1000];
int sum[600][30];

int M, N, L;

int ans;

int main()
{
	M = strlen(s);

	cin >> N;
	cin.getline(data, 1000);
	for (int i = 0; i < N; i++)
	{
		cin.getline(data, 1000);
		int L = strlen(data);

		memset(sum, 0, sizeof(sum));
		for (int j = 0; j < L; j++)
			for (int k = 0; k < M; k++)
			{
				if (j > 0) sum[j][k] = sum[j-1][k];
				
				if (data[j] == s[k])
				{
					if (k == 0) sum[j][k]++;
					else
						if (j > 0)	sum[j][k] += sum[j-1][k-1];
				}

				sum[j][k] %= 10000;
			}

		if (L > 0)
			ans = sum[L-1][M-1];
		else 
			ans = 0;

		cout << "Case #" << i+1 << ": ";
		if (ans < 10) cout << "0";
		if (ans < 100) cout << "0";
		if (ans < 1000) cout << "0";
		cout << ans << endl;
	}
	

	return 0;
}