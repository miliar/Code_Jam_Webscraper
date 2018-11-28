#include <iostream>
#include <fstream>

using namespace std;
double calc_wp(int[][100], int, int);
double calc_owp(int[][100], int, int);
double calc_oowp(int[][100], int, int, double*);

int main()
{
	string filename;
	cin >> filename;
	ifstream infile(filename.c_str());
	ofstream outfile("output.txt");

	int test_cases;
	infile >> test_cases;

	for (int round = 1; round <= test_cases; round++) {
		int n;
		double wp[100];
		double owp[100];
		double oowp[100];

		infile >> n;
		int matrix[100][100];
		for (int i = 0; i < n; i++) {
			string str;
			infile >> str;
			for (int j= 0; j < n; j++)
				matrix[i][j] = str.at(j);
		}

		for (int i= 0; i < n; i++)
			wp[i] = calc_wp(matrix, n, i);

		for (int i = 0; i < n; i++)
			owp[i] = calc_owp(matrix, n, i);

		for (int i = 0; i < n; i++)
			oowp[i] = calc_oowp(matrix, n, i, owp);

		outfile << "Case #" << round << ":" << endl;
		for (int i = 0; i < n; i++)
			outfile <<  0.25*wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;

	}
	infile.close();
	outfile.close();
	return 0;
}

double calc_wp(int matrix[][100], int n, int i)
{

	double c = 0;
	double win = 0;
	for (int k = 0; k < n; k++) {
		if (matrix[i][k] == '0')
			c++;
		else if (matrix[i][k] == '1') {
			c++;
			win++;
		}
	}
	return win/c;
}

double calc_owp(int matrix[][100], int n, int i)
{
	int newm[100][100];
	for (int r = 0; r < n; r++)
		for (int c = 0; c < n; c++) {
			if (c == i)
				newm[r][c] = '.';
			else
				newm[r][c] = matrix[r][c];
		}

	double sum = 0;
	int target  = 0;
	for (int k = 0; k < n; k++) {
		if (newm[i][k] != '.') {
			target ++;
			sum += calc_wp(newm, n, k);
		}
	}
	
	return sum / target;
}

double calc_oowp(int matrix[][100], int n, int i, double* owp)
{
	double sum = 0;
	int target = 0;
	for (int k = 0; k < n; k++)
		if (matrix[i][k] != '.') {
			target ++;
			sum += owp[k];
		}

	return sum / target;
}
