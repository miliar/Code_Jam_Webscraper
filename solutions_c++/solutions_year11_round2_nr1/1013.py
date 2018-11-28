#include <iostream>

using namespace std;

int main()
{
	int t;   

	int n, pd, pg;
	string s[101];
	int w[101];
	int m[101];
	double owp[101];
	double oowp[101];
    cin >> t;
    
    for(int tt=1; tt<=t; tt++)
    {
		cin >> n;
		
		for(int i=0; i<n; i++)
		{
			cin >> s[i];
		}
		
		
		
		for(int i=0; i<n; i++)
		{
			w[i] = 0; m[i] = 0;
			for(int j=0; j<n; j++)
			{
				if (s[i][j] == '1') { w[i]++; m[i]++; }
				else if (s[i][j] == '0') m[i]++;
			}
			
		}
		
		for(int i=0; i<n; i++)
		{
			int no = 0;
			owp[i] = 0;
			for(int j=0; j<n; j++)
			{
				if (s[i][j] != '.')
				{
					no++;
					int mm = m[j]-1;
					int ww = w[j];
					if (s[i][j] == '0') ww--;
					if (mm > 0) owp[i] += 1.0*ww/mm;
				}
			}
			if (no > 0)  owp[i] /= no; else owp[i] = 0;
			
		}
		
		for(int i=0; i<n; i++)
		{
			int no = 0;
			oowp[i] = 0;
			for(int j=0; j<n; j++)
			{
				if (s[i][j] != '.')
				{
					no++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= no;
		}
		
		printf("Case #%d:\n", tt);
		for(int i=0; i<n; i++)
		{
			double rpi = 0.25 * w[i] / m[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.8lf\n", rpi);
		}
    }
    
    return 0;
}
