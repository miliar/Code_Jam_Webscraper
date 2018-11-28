#include <iostream>
#include <set>

using namespace std;

int main()
{
	int n;
	cin >> n;
	while (n--)
	{
		int s;
		cin >> s;
		getchar();
		string all[200];
		for (int i=0; i<s; i++)
		{
			char buf[1000];
			cin.getline(buf, sizeof(buf));
			all[i] = buf;
		}
		int q;
		cin >> q;
		getchar();

		static int f[3][2000][2000];
#define ff f[1]

		memset(f, 0, sizeof(f));
		for (int i=0; i<q; i++)
		{
			char buf[1000];
			cin.getline(buf, sizeof(buf));

			for (int j=0; j<s; j++)
			{
				if (all[j] == buf)
				{
					ff[i][j] = 1000000;
				}
				else
				{
					int mm = 1000000;
					for (int k=0; k<s; k++)
						if (ff[i-1][k]+(j!=k) < mm)
							mm = ff[i-1][k]+(j!=k);
					ff[i][j] = mm;
				}
			}
		}
		static int ca = 0;
		int mm = 100000;
		for (int i=0; i<s; i++)
			if (ff[q-1][i] < mm)
				mm = ff[q-1][i];
		cout << "Case #" << ++ca << ": " << mm << endl;
//		system("pause");
	}
}

