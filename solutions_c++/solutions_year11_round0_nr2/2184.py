#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int kol_test;
int n;
char a[1000];
char norm[1000][3];
char rem[1000][2];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	scanf("%d", &kol_test);

	for (int nom_test = 0; nom_test < kol_test; ++nom_test)
	{
		int kol_n, kol_r;
		scanf("%d ", &kol_n);
		for (int i = 0; i < kol_n; ++i)
		{
			char temp1, temp2, temp3;
			scanf("%c%c%c ", &temp1, &temp2, &temp3);
			norm[i * 2][0] = temp1;
			norm[i * 2][1] = temp2;
			norm[i * 2][2] = temp3;
			norm[i * 2 + 1][0] = temp2;
			norm[i * 2 + 1][1] = temp1;
			norm[i * 2 + 1][2] = temp3;
		}
		kol_n *= 2;
		scanf("%d ", &kol_r);
		for (int i = 0; i < kol_r; ++i)
		{
			char temp1, temp2;
			scanf("%c%c ", &temp1, &temp2);
			rem[i * 2][0] = temp1;
			rem[i * 2][1] = temp2;
			rem[i * 2 + 1][0] = temp2;
			rem[i * 2 + 1][1] = temp1;
		}
		kol_r *= 2;
		scanf("%d ", &n);
		int kol = 0;
		for (int i = 0; i < n; ++i)
		{
			char temp;
			scanf("%c", &temp);
			a[kol] = temp;
			++kol;
			if (kol < 2)
				continue;
			bool err = true;
			while (err)
			{
				err = false;
				char c;
				for (int j = 0; j < kol_n; ++j)
				{
					if (norm[j][0] == a[kol - 2] && norm[j][1] == a[kol - 1])
					{
						err = true;
						c = norm[j][2];
						break;
					}
				}
				if (err)
				{
					--kol;
					a[kol - 1] = c;
				}
			}
			if (kol < 2)
				continue;

			int error_kol = 0;
			for (int j = 0; j < kol_r; ++j)
			{
				int error_cur = 0;
				for (int k = 0; k < kol; ++k)
				{
					if (a[k] == rem[j][0])
					{
						error_cur |= 1;
					}
					if (a[k] == rem[j][1])
					{
						error_cur |= 2;
					}
				}
				if (error_cur == 3)
				{
					error_kol = 2;
					break;
				}
			}
			if (error_kol == 2)
			{
				kol = 0;
			}
		}

		printf("Case #%d: [", nom_test + 1);
		for (int i = 0; i < kol; ++i)
		{
			if (i == kol - 1)
			{
				printf("%c", a[i]);
			}
			else
			{
				printf("%c, ", a[i]);
			}
		}
		printf("]\n");
	}

	return 0;
}