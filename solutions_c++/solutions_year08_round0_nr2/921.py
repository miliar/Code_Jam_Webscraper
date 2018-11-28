#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin("B-large.in.txt");
ofstream fout("B-large.out.txt");

int n, na, nb, t;
int train_a[200][2], train_b[200][2];

int ans_a, ans_b;
int valid_a[200], valid_b[200];

int main()
{
	int temp;
	int h1, m1, h2, m2;
	char s1[1024], s2[1024];

	fin >> n;
	for (int cases = 1; cases <= n; cases++)
	{
		fin >> t;
		fin >> na >>  nb;

		for (int i = 0; i < na; i++)
		{
			fin >> s1 >> s2;
			sscanf(s1, "%d:%d", &h1, &m1);
			sscanf(s2, "%d:%d", &h2, &m2);

			train_a[i][0] = h1 * 60 + m1;
			train_a[i][1] = h2 * 60 + m2;
		}

		for (int i = 0; i < nb; i++)
		{
			fin >> s1 >> s2;
			
			sscanf(s1, "%d:%d", &h1, &m1);
			sscanf(s2, "%d:%d", &h2, &m2);

			train_b[i][0] = h1 * 60 + m1;
			train_b[i][1] = h2 * 60 + m2;
		}

		for (int i = 0; i < na; i++)
			for (int j = 1; j < na; j++)
				if (train_a[i][1] > train_a[j][1])
				{
					temp = train_a[i][0]; train_a[i][0] = train_a[j][0]; train_a[j][0] = temp;
					temp = train_a[i][1]; train_a[i][1] = train_a[j][1]; train_a[j][1] = temp;
				}

		for (int i = 0; i < nb; i++)
			for (int j = 1; j < nb; j++)
				if (train_b[i][1] > train_b[j][1])
				{
					temp = train_b[i][0]; train_b[i][0] = train_b[j][0]; train_b[j][0] = temp;
					temp = train_b[i][1]; train_b[i][1] = train_b[j][1]; train_b[j][1] = temp;
				}
		
		memset(valid_a, 0, sizeof(valid_a));
		memset(valid_b, 0, sizeof(valid_b));

		ans_a = ans_b = 0;

		for (int i = 0; i < na; i++)
		{
			int best = -1;
			for (int j = 0; j < nb; j++)
				if (valid_b[j] == 0 && train_b[j][1] + t <= train_a[i][0] && (best == -1 || train_b[best][1] < train_b[j][1]))
					best = j;
			
			if (best == -1)
				ans_a++;
			else
				valid_b[best] = 1;
		}

		for (int i = 0; i < nb; i++)
		{
			int best = -1;
			for (int j = 0; j < na; j++)
				if (valid_a[j] == 0 && train_a[j][1] + t <= train_b[i][0] && (best == -1 || train_a[best][1] < train_a[j][1]))
					best = j;

			if (best == -1)
				ans_b++;
			else
				valid_a[best] = 1;
		}

		fout << "Case #" << cases << ": " << ans_a << " " << ans_b << endl;
	}

	return 0;
}