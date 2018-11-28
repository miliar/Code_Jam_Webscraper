#include <fstream>
#include <cstdio>
#include <vector>
using namespace std;
 
#define abs(X) X >= 0 ? X : -X
 
double norm(vector<double>& a)
{
        int n = a.size();
        double sum = 0;
        for (int i = 0; i < n; i++)
        {
                sum += abs(a[i]);
        }
        return sum;
}
 
double norm(vector<vector<double> >& a)
{
        int n = a.size();
        double r = 1 << 31;
        for (int i = 0; i < n; i++)
        {
                r = max(r, norm(a[i]));
        }
        return r;
}
 
bool isNextStepRequired(vector<double>& previous, vector<double>& current, double delta)
{
        int n = current.size();
        vector<double> difference(n);
        for (int i = 0; i < n; i++)
        {
                difference[i] = current[i] - previous[i];
        }
        return norm(difference) >= delta;
}
 
int main()
{
		freopen("output.txt", "w", stdout);
        ifstream cin("input.txt");
		ofstream cout("output.txt");

		int T;
		cin >> T;
		for (int tc = 0; tc < T; tc++)
		{ 
			int n;
			cin >> n;

			double sum = 0;
			vector<double> J(n);
			for (int i = 0; i < n; i++)
			{
				cin >> J[i];
				sum += J[i];
			}

			vector<double> y(n);
			double l = 0, r = sum, middle;
			while (fabs(l - r) > 1e-8)
			{
				double p = 0.0;
				middle = (l + r) / 2.0;
				for (int i = 0; i < n; i++)
				{
					y[i] = (middle - J[i]) / sum;
					if (y[i] < 0) continue;
					p += y[i];
				}
				((p < 1.0) ? l : r) = middle;
			}

			printf("Case #%d: ", tc + 1);
			//cout << "Case #" << tc + 1 << ": ";
			for (int i = 0; i < n; i++)
			{
				printf("%.6lf ", fabs(y[i] * 100.0));
				//cout << fabs(y[i] * 100.0) << " ";
			}
			putchar('\n');
			//cout << endl;
		}
 
        return 0;
}
