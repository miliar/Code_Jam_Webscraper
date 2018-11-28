#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int n;
char a[200][200];
int w[200], l[200];
double WP[200], OP[200], OOP[200];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, TT;

	cin >> T;
	for (TT=1;TT<=T;++TT)
	{
		cin >> n;
		memset(w, 0, sizeof(w));
		memset(l, 0, sizeof(l));

		for (int i=0;i<n;++i) {
			for (int j=0;j<n;++j) {
				scanf(" %c ", &a[i][j]);
				if (a[i][j] == '1')
					++ w[i];
				if (a[i][j] == '0')
					++ l[i];
			}
			
			WP[i] = w[i] / (double)(w[i] + l[i]);
		}

		for (int i=0; i < n; ++ i)
		{
			int count = 0;
			double rating = 0.0;
			for (int j=0;j<n;++j) {
				if (a[i][j] != '.') {
					count ++;
					rating += (w[j] - (a[i][j] == '0' ? 1 : 0)) / (double)(w[j] + l[j] - 1);
				}
			}

			OP[i] = rating / count;
		}
			
		for (int i=0; i < n; ++ i)
		{
			int count = 0;
			double rating = 0.0;
			for (int j=0;j<n;++j) {
				if (a[i][j] != '.')
					count ++,
					rating += OP[j];
			}

			OOP[i] = rating / count;
		}	 

		cout << "Case #" << TT << ":\n";
		for (int i=0;i<n;++i)
		{
			printf("%.12lf\n", (0.25 * WP[i] + 0.5 * OP[i] + 0.25 * OOP[i]));
		}
	}

	return 0;
}