#include<iostream> 
#include<cstdio>
#include<queue>
#include<fstream>
#include<string> 
using namespace std;
//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

char arr[101][101];
double wp[101][101];
double owp[101];
double oowp[101];
double enemy[101];
double score[101]; 


int main()
{
	int n , t , T , N;
	int i = 0;
	double output = 0;
	double p , tmp;
	string a; 

	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");

	//scanf( "%d" , &T );
	fin >> T;
	for( t = 1 ; t <= T ; ++t )
	{
		fin >> N;
		//getchar();
		for( n = 0 ; n < N ; ++n )
		{
			fin >> a;
			enemy[n] = 0;
			score[n] = 0; 
			for( i = 0 ; i < N ; ++i )
			{
				arr[n][i] = a[i];
				if( arr[n][i] == '.' )
					continue;
				++enemy[n]; 
				score[n] += (double)( a[i] - '0' ); 
			}
			wp[n][n] = score[n] / enemy[n];
		}
		for( n = 0 ; n < N ; ++n )
		{
			for( i = 0 ; i < N ; ++i )
			{
				if( i == n )
					continue; 
				if( arr[n][i] == '.' )
					wp[n][i] = 0;
				else //( arr[n][i] != '.' )
				{
					wp[n][i] = (   score[n] - (double)(arr[n][i] - '0')   )    /    (enemy[n]-1.0) ;
				}
			}
		}
		for( n = 0 ; n < N ; ++n )
		{
			tmp = 0;
			for( i = 0 ; i < N ; ++i )
			{
				if( i == n )
					continue;
				tmp += wp[i][n];
			}
			owp[n] = tmp / enemy[n];
		}
		fout << "Case #" << t << ": " << endl;
		for( n = 0 ; n < N ; ++n )
		{
			tmp = 0; 
			for( i = 0 ; i < N ; ++i )
			{
				if(   i == n   ||   arr[n][i] == '.'   )
					continue;
				tmp += owp[i];
			}
			oowp[n] = tmp / enemy[n];
		}
		for( n = 0 ; n < N ; ++n )
		{
			output = 0.25 * wp[n][n] + 0.50 * owp[n] + 0.25 * oowp[n];
			//fout <<  "wp: " << wp[n][n] << "   owp: " << owp[n] << "   oowp: " << oowp[n] << endl; 
			//printf( "%.12f/n" , output );
			fout << output << endl;
		}
	}//end while(fin)
	return 0; 
}
