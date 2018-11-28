#include<iostream>

#define FOR0(i, n) for(int i=0;i<n;i++)
#define FOR1(i, n) for(int i=1;i<=n;i++)

using namespace std;

int main()
{
	int z, n;
	char r[100][100];
	double c[100], x, y;
	double wp[100], owp[100], oowp[100];
	double wp_[100], owp_[100], oowp_[100];
	
	cout.precision(12);
	cin >> z;

	FOR1(i, z)
	{
		cin >> n;
		FOR0(j, n)
		{
			wp[j] = 0;
			c[j] = 0;
			FOR0(k, n)
			{
				cin >> r[j][k];
				if(r[j][k] != '.')
				{
					if(r[j][k] == '1') wp[j]++;
					c[j]++;
				}
			}
			wp_[j] = c[j];
			if(wp[j] == 0) wp_[j] = 1;
			//cout << j << " " << wp[j] << " " << wp_[j] << " " << wp[j]/wp_[j]<< endl;
		}
		
		FOR0(j, n)
		{
			owp[j] = 0;
			owp_[j] = 1;
			FOR0(k, n)
			{
				if(r[j][k] != '.')
				{
					x = wp[k] - (r[k][j] == '1'? 1:0);
					y = wp_[k] > 1? wp_[k] - 1 : 1;

					owp[j] = owp[j]*y + owp_[j]*x;
					owp_[j] = owp_[j]*y;
				}
			}
			owp_[j] *= c[j];
			if(owp[j] == 0) owp_[j] = 1;
			//cout << j << " " << owp[j] << " " << owp_[j] << " " << owp[j]/owp_[j]<< endl;
		}

		FOR0(j, n)
		{
			oowp[j] = 0;
			oowp_[j] = 1;
			FOR0(k, n)
			{
				if(r[j][k] != '.')
				{
					oowp[j] = oowp[j]*owp_[k] + oowp_[j]*owp[k];
					oowp_[j] = oowp_[j]*owp_[k];
				}
			}
			oowp_[j] *= c[j];
			if(oowp[j] == 0) oowp_[j] = 1;
		}

		cout << "Case #" << i << ":" << endl;
		FOR0(j, n)
			cout << ((wp[j]/wp_[j] + 2*owp[j]/owp_[j] + oowp[j]/oowp_[j])/4) << endl;
	}
	return 0;
}
