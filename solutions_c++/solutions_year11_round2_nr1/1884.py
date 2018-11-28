// CodeJam 2011 - Round 1B-A - 
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   int T, N;
   char **matrix;
   long double *WP, *OWP, *OOWP;
   ifstream infile("A-large.in");
   ofstream outfile("A-large.out");
   char ch;
   
   infile >> T;
   for(int i=1; i<=T; i++)
   {
	infile >> N;
	WP = new long double[N]; OWP = new long double[N]; OOWP = new long double[N];
	matrix = new char*[N];
	for(int j=0; j<N; j++)
	{
		matrix[j] = new char[N];
		for(int k=0; k<N; k++)
		{
			infile >> ch; matrix[j][k] = ch; cout << ch << " ";
		}
		cout<<endl;
	}

	int win=0, total=0;	
	for(int j=0; j<N; j++)
	{
		win = total = 0;
		for(int k=0; k<N; k++)
		{
			if(matrix[j][k] == '.') continue;
			if(matrix[j][k] == '1') win++;
			total++;
		}
		WP[j] = (long double)win / total;
	}
	for(int j=0; j<N; j++)
	{
		long double gwin = 0; int gtotal = 0;
		for(int k=0; k<N; k++)
		{
			if(matrix[j][k] == '.') continue;
			win = total = 0; gtotal++;
			for(int l=0; l<N; l++)
			{
				if(l == j) continue;
				if(matrix[k][l] == '.') continue;
				if(matrix[k][l] == '1') win++;
				total++;
			}
			gwin += ((long double)win/total);
		}
		OWP[j] = gwin / (long double)gtotal;
	}
	for(int j=0; j<N; j++)
	{
		long double gowp = 0; int gtotal = 0;
		for(int k=0; k<N; k++)
		{
			if(matrix[j][k] == '.') continue;
			gowp += OWP[k]; gtotal++;
		}
		OOWP[j] = gowp / (long double)gtotal;
	}

	long double RPI;
	outfile << "Case #" << i << ":" << endl;
	for(int j=0; j<N; j++)
	{
		RPI = 0.25*WP[j] + 0.5*OWP[j] + 0.25*OOWP[j];
		cout<< WP[j] << "    " << OWP[j] << "    " << OOWP[j] << endl;
		outfile << RPI << endl;
	}

	for(int j=0;j<N;j++) delete[] matrix[j];
	delete[] matrix;
	delete[] WP; delete[] OWP; delete[] OOWP;
   }
   infile.close();
   outfile.close();
   return 0;
}

