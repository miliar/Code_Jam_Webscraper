#include <iostream>
#include <vector>
#include <string>
using namespace std;
char wd[5002][20];
char x[10000];
char fit[20][50];
int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int l, d, n;
	while (cin >> l >> d >> n)
	{
		for (int i = 0; i < d; i++)
			scanf ("%s", &wd[i]);
		for (int i = 0; i < n; i++)
		{
			scanf ("%s",&x);
			int len = strlen(x);
			int flag = 0;
			char temp[50];
			int mark = 0;
			int k = 0;
			for (int j = 0; j < len; j++)
			{
				if (x[j] == '(')
					flag = 1;
				else if (x[j] == ')')
				{
					strcpy (fit[k++], temp);
					flag = 0;
					mark = 0;
				}
				else
				{
					if (!flag)
					{
						flag = 0;
						fit[k][0] = x[j];
						fit[k][1] = 0;
						k++;
					}
					else 
					{
						temp[mark++] = x[j];
						temp[mark] = 0;
					}
				}
			}
			int ans = 0;
			for (int j = 0; j < d; j++)
			{
				int kk;
				for (kk = 0; kk < l; kk++)
				{
					int s;
					int lenx = strlen(fit[kk]);
					for (s = 0; s < lenx; s++)
						if (wd[j][kk] == fit[kk][s])
							break;
					if (s == lenx)break;
				}
				if (kk == l)ans++;
			}
			printf ("Case #%d: %d\n", i+1, ans);
			//for (int j = 0; j < l; j++)
			//	cout << fit[j] << endl;
		}
	}
}