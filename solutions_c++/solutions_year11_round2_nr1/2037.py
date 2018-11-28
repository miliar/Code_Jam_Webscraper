#include <iostream>


using namespace std;

int main()
{
	int t;
	cin >> t;

	for( int z = 0; z < t; z++ )
	{
		int n;
		cin >> n;
		char **results;
		double *wp, *owp, *oowp, *rpi;
		int *win, *loss;

		results = new char*[n];
		for( int i = 0; i < n; i++ )
		{
			results[i] = new char[n];
		}

		for( int i = 0; i < n; i++ )
		{
			for( int j = 0; j < n; j++ )
			{
				cin >> results[i][j];
			}
		}

		wp = new double[n];
		owp = new double[n];
		oowp = new double[n];
		rpi = new double[n];
		win = new int[n];
		loss = new int[n];

		for( int i = 0; i < n; i++ )
		{
			win[i] = 0;
			loss[i] = 0;
			for( int j = 0; j < n; j++ )
			{
				switch(results[i][j])
				{
					case '1':
					       win[i]++;
					       break;
					case '0':
					       loss[i]++;
					       break;
					case '.':
					       break;
				}
			}
			wp[i] = double(win[i])/double(win[i] + loss[i]);
//			cout << "wp=" << wp[i] << endl;
		}

		for( int i = 0; i < n; i++ )
		{
			owp[i] = 0;
			for( int j = 0; j < n; j++ )
			{
				switch(results[i][j])
				{
					case '1':
					       owp[i] += double(win[j])/double(win[j] + loss[j] - 1);
					       break;
					case '0':
					       owp[i] += double(win[j] - 1)/double(win[j] + loss[j] - 1);
					       break;
					case '.':
					       break;
				}

			}
			owp[i] /= double(win[i] + loss[i]);
//			cout << "owp=" << owp[i] << endl;
		}

		for( int i = 0; i < n; i++ )
		{
			oowp[i] = 0;
			for( int j = 0; j < n; j++ )
			{
				switch(results[i][j])
				{
					case '1':
					case '0':
					       oowp[i] += owp[j];
					       break;
					case '.':
					       break;
				}

			}
			oowp[i] /= double(win[i] + loss[i]);
//			cout << "oowp=" << oowp[i] << endl;
			rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		}

		cout << "Case #" << (z + 1) << ":" << endl;
		for( int i = 0; i < n; i++ )
		{
			cout.precision(12);
			cout << rpi[i] << endl;
		}

		delete [] wp;
		delete [] owp;
		delete [] oowp;
		delete [] rpi;
		delete [] win;
		delete [] loss;
		for( int i = 0; i < n; i++ )
		{
			delete [] results[i];
		}
		delete [] results;
	}	

	return 1;
}
