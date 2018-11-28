#include <iomanip>
#include <algorithm>
#include <map>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

#include <time.h>
#include <sys/time.h>

using namespace std;

double ans[111];
int a1[111];
double a2[111];
double a3[111];
int k1[111];
int k2[111];
int a[111][111];

int main()
{
//	freopen("anarc05b.in","r",stdin);
//	freopen("anarc05b.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int T = 0; T < t; T++)
	{
		int n;
		printf("Case #%d:\n",T+1);
		scanf("%d",&n);
		char ss[111];
		gets(ss);

		for (int i = 0; i < n; i++)
		{
			gets(ss);
			string s = ss;
			for (int j = 0; j < n; j++)
			{
				if (s[j] == '0') a[i][j] = 0;
				else
				if (s[j] == '1') a[i][j] = 1;
				else a[i][j] = -1;
			}
			ans[i] = 0.0;
		}

		for (int i = 0; i < n; i++)
		{	
			a1[i] = 0;
			k1[i] = 0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] == -1) continue;
				k1[i]++; a1[i]+=a[i][j];
			}
			double D = a1[i]; D /= k1[i];
			ans[i] = ans[i] + 0.25 * D;
		}
		for (int i = 0; i < n; i++)
		{
			a2[i] = 0.0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] == -1) continue;
				double D = a1[j] - a[j][i];
//				cout << "   ---- " << D << " " << k1[j] - 1 << endl;
				D /= (k1[j] - 1);
				a2[i] += D;
			}
//			cout << a2[i] << " " << k1[i] << endl;
			a2[i] /= k1[i];
			ans[i] +=(a2[i] * 0.5);
		}

		for (int i = 0; i < n; i++)
		{
			double D = 0.0;
			int k = 0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] == -1) continue;
				D+=a2[j];
				k++;
			}
			D /= k;
			D *= 0.25;
			ans[i] += D;
		}
		
		for (int i = 0; i < n; i++)
			printf("%.9lf\n",ans[i]);
	}

//	in.getline(s);

	return 0;	
}
