#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

double calcWP(char** mat, int N, int team, int col)
{
	int count = 0;
	int win = 0;
	for(int j=0; j<N; j++)
	{
		if(mat[team][j] == '.') continue;
		if(j == col) continue;
		if(mat[team][j] == '1')
		{
			win++;
		}
		count++;
	}
	double res = (double) win / count;
	return res;
}

vector<double> process(char** mat, int N)
{
	double *WP = new double[N];
	for(int i=0; i<N; i++)
	{
		int count = 0;
		int win = 0;
		for(int j=0; j<N; j++)
		{
			if(mat[i][j] == '.') continue;
			if(mat[i][j] == '1')
			{
				win++;
			}
			count++;
		}
		WP[i] = (double) win / count;
	}
	double *OWP = new double[N];
	for(int i=0; i<N; i++)
	{
		double owp = 0;
		int count = 0;
		for(int j=0; j<N; j++)
		{
			if(mat[i][j] == '.') continue;
			owp += calcWP(mat, N, j, i);
			count++;
		}
		owp /= count;
		OWP[i] = owp;
	}
	double *OOWP = new double[N];
	for(int i=0; i<N; i++)
	{
		double oowp = 0;
		int count = 0;
		for(int j=0; j<N; j++)
		{
			if(mat[i][j] == '.') continue;
			oowp += OWP[j];
			count++;
		}
		oowp /= count;
		OOWP[i] = oowp;
	}
	vector<double> res;
	for(int i=0; i<N; i++)
	{
		double rpi = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		res.push_back(rpi);
	}
	return res;
}

void main()
{
	ifstream infile("Input.txt");
	ofstream outfile("Output.txt");
	int T;
	infile >> T;
	for(int i=0; i<T; i++)
	{
		int N;
		infile >> N;
		char** mat= new char*[N];
		for(int j=0; j<N; j++)
		{
			mat[j] = new char[N];
			for(int k=0; k<N; k++)
			{
				char c;
				infile >> c;
				mat[j][k] = c;
			}
		}
		vector<double> res = process(mat, N);
		outfile << "Case #" << i+1 << ":" << endl;
		for(int j=0; j<(int)res.size(); j++)
		{
			outfile << res[j] << endl;
		}
	}
	infile.close();
	outfile.close();
}