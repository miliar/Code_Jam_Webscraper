#include <iostream>

using namespace std;

int main()
{
	int t, n, a, b, numo;
	long double totalwp, totalowp;
	int** board;
	long double** wp;
	long double* owp;
	long double* oowp;
	char temp;

	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ":" << endl;
		cin >> n;
		board = new int*[n];
		wp = new long double*[n];
		owp = new long double[n];
		oowp = new long double[n];
		for(int j = 0; j < n; j++)
		{
			board[j] = new int[n];
			wp[j] = new long double[2];
			a = 0;
			b = 0;
			for(int k = 0; k < n; k++)
			{
				cin >> temp;
				if(temp == '0')
				{
					board[j][k] = 0;
					b++;
				}
				else if(temp == '1')
				{
					board[j][k] = 1;
					a++;
					b++;
				}
				else
				{
					board[j][k] = 2;
				}
			}

			wp[j][0] = a;
			wp[j][1] = b;
		}

		for(int j = 0; j < n; j++)
		{
			totalwp = 0.0;
			numo = 0;
			for(int k = 0; k < n; k++)
			{
				if(board[j][k] == 0)
				{
					a = wp[k][0]-1;
					b = wp[k][1]-1;
					//cout << "a: " << a << ", b: " << b << endl;
					totalwp += (long double)a/b;
					numo++;
				}
				else if(board[j][k] == 1)
				{
					a = wp[k][0];
					b = wp[k][1]-1;
					totalwp += (long double)a/b;
					numo++;
				}
			}
			//cout << "DEBUG: " << "a: " << a << ", b: " << b << ", " << totalwp << " " << numo << endl;
			owp[j] = totalwp/numo;
			//cout << "owp[" << j << "] = " << totalwp << "/" << numo << endl;
		}
		for(int j = 0; j < n; j++)
		{
			totalowp = 0;
			numo = 0;
			for(int k = 0; k < n; k++)
			{
				//If you played against them
				if(board[j][k] == 0 || board[j][k] == 1)
				{
					totalowp += owp[k];
					numo++;
				}
			}
			oowp[j] = totalowp/numo;
		}
		for(int j = 0; j < n; j++)
		{
			cout << 0.25 * (long double)(wp[j][0]/wp[j][1]) + 0.5 * owp[j] + 0.25 * oowp[j] << endl;
			//cout << "wpa: " << wp[j][0] << ", wpb: " << wp[j][1] << ", wp: " << (double)(wp[j][0]/wp[j][1]) << endl;
			//cout << "owp: " << owp[j] << endl;
			//cout << "oowp: " << oowp[j] << endl;		
		}
	}
}
