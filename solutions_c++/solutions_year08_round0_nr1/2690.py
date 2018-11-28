#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int inf = 10000000;

int n , k , i , j , s , q , m , e ;
int a[300][3000];
string ser[300];
string que[300];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> n;
	for (k = 1;k <= n;k ++)
	{
		cin >> s;
		getline(cin,ser[0]);
		for (i = 1;i <= s;i ++)
			getline(cin,ser[i]);
		cin >> q;
		getline(cin,que[0]);
		for (i = 1;i <= q;i ++)
			getline(cin,que[i]);
		for (i = 0;i <= 200;i ++)
			for (j = 0; j <= 2000;j ++)
			{
				a[i][j] = inf;
			}
		for (i = 0;i <= 200;i ++)
			a[i][0] = 0;
		for (i = 0;i < q;i ++)
			for (j = 1; j <= s; j ++)
			{
				if (a[j][i]  != inf)
				{
				if (ser[j] != que[i + 1])
				{
					a[j][i + 1] = min(a[j][i + 1],a[j][i]);
				}
				else
				{
					for (e = 1;e <= s;e ++)
						if (e != j)
						{
							a[e][i + 1] = min(a[e][i + 1],a[j][i] + 1);
						}
				}
				}
			}
		m = a[1][q];
		for (i = 1; i <= s;i ++)
			if (a[i][q] < m)
			{
				m = a[i][q];
			}
		cout << "Case #" << k << ": " << m << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}