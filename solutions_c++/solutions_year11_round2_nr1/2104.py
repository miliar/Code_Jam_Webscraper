#include <iostream>
#include <string>
#include <cstring>
using namespace std;

string t[100];

int main()
{
	int T;
	cin >> T;
	for (int x=1; x<=T; x++)
	{
		int N;
		cin >> N;

		cout.setf(ios::fixed);
		cout.precision(8);

		for (int i=0; i<N; i++)
		{
			t[i].clear();
			cin >> t[i];
		}

		double wp[N];
		double owp[N][N];
		double oowp[N];
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));

		for (int i=0; i<N; i++)
		{
			int n = 0;
			for (int k=0; k<N; k++)
			{
				if (i==k) continue;
				if (t[i][k]!='.') n++;
				if (t[i][k]=='1') wp[i]++;
			}
			wp[i] /= n;
		}

		for (int i=0; i<N; i++)
		for (int k=0; k<N; k++)
		{
			if (i == k) continue;
			int n = 0;
			for (int l=0; l<N; l++)
			{
				if (i==l || k==l) continue;
				if (t[i][l]!='.') n++;
				if (t[i][l]=='1') owp[i][k]++;
			}
			owp[i][k] /= n;
		}
		
		for (int i=0; i<N; i++)
		{
			int n = 0;
			for (int k=0; k<N; k++)
				if (i!=k && t[i][k]!='.')
				{
					n++;
					owp[i][i] += owp[k][i];
				}

			owp[i][i] /= n;
		}

		for (int i=0; i<N; i++)
		{
			int n = 0;
			for (int k=0; k<N; k++)
				if (t[i][k] != '.')
				{
					n++;
					oowp[i] += owp[k][k];
				}
			oowp[i] /= n;
		}

		cout << "Case #" << x << ':' << endl;
		for (int i=0; i<N; i++)
			cout << 0.25*wp[i]+0.5*owp[i][i]+0.25*oowp[i] << endl;
	}
	return 0;
}
