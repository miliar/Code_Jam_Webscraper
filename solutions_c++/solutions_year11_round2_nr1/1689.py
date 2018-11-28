#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

int T;
int N;
std::vector<string> Table;
std::vector<double> WP;
std::vector<double> OWP;
std::vector<double> OOWP;

void calculateWP()
{
	double total = 0; 
	double winNum = 0;
	for(int i = 0; i < N; i++)
	{
		total = 0;
		winNum = 0;
		for(int j = 0; j < N; j++)
		{
			if(Table[i][j] == '1')
			{
				total++;
				winNum++;
			}
			else if(Table[i][j] == '0')
			{
				total++;
			}
		}
		WP[i] = winNum/total;
	}
	return;
}

double singleWP(int i, int j)
{
	double total = 0;
	double winNum = 0;
	for(int k = 0; k < N; k++)
	{
		if(k == i)
			continue;
		if(Table[j][k] == '1')
		{
			total++;
			winNum++;
		}
		else if(Table[j][k] == '0')
		{
			total++;
		}
	}
	return winNum/total;
}

void calculateOWP()
{
	double sum = 0;
	int Count = 0;
	for(int i = 0; i < N; i++)
	{
		OWP[i] = 0;
		Count = 0;
		for(int j = 0; j < N; j++)
		{
			if(Table[i][j] == '1' || Table[i][j] == '0')
			{
				Count++;
				OWP[i] += singleWP(i,j);
			}
		}
		OWP[i] /= Count;
		sum += OWP[i];
	}
	return;
}

void calculateOOWP()
{
	int Count = 0;
	for(int i = 0; i < N; i++)
	{
		OOWP[i] = 0;
		Count = 0;
		for(int j = 0; j < N ; j++)
		{
			if(Table[i][j] == '1' || Table[i][j] == '0')
			{
				OOWP[i] += OWP[j];
				Count++;
			}
		}
		OOWP[i] = OOWP[i]/Count;
	}
}

void calculateRPI()
{
	calculateWP();
	calculateOWP();
	calculateOOWP();
	return;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large-ans.out");
	fin>>T;
	double RPI;
	for(int i = 0; i < T; i++)
	{
		fin>>N;
		Table.clear();
		Table.resize(N);
		WP.clear();
		WP.resize(N);
		OWP.clear();
		OWP.resize(N);
		OOWP.clear();
		OOWP.resize(N);
		for(int r = 0; r < N; r++)
		{
			fin>>Table[r];
		}
		calculateRPI();
		fout<<"Case #"<<i+1<<":\n";
		for(int j = 0; j < N; j++)
		{
			RPI = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
			fout<<RPI<<"\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}
