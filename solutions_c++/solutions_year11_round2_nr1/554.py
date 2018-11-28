#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cmath>
#include <iostream>
#include <fstream>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define ok(a, b) ((a) >= 0 && (a) < N && (b) >= 0 && (b) < M && mat[a][b] == '.')

ifstream fin("c:\\A-large.in");
ofstream fout("c:\\A-large.out");

double WP[101];
double WP1[101];
double OWP[101];
double OOWP[101];

void run()
{
	int n;
	fin >> n;
	vector<string> cmp;
	for ( int i = 0; i < n; i++)
	{
		string tmp;
		fin >> tmp;
		cmp.push_back(tmp);
	}
	
	for (int i = 0; i < n; i ++ )
	{
		int tot = 0;
		int nW = 0;
		for ( int j = 0; j < n; j ++)
		{
			if ( cmp[i][j] !='.') tot++;
			if ( cmp[i][j] =='1') nW++;
		}
		WP[i] = (double)nW / tot;
		
		for ( int j = 0; j < n; j ++ )
		{
			tot = 0;
			nW = 0;
			for ( int k = 0; k < n; k ++)
			{
				if ( k == i ) continue;
				if ( cmp[j][k] !='.') tot++;
				if ( cmp[j][k] =='1') nW++;
			}
			WP1[j] = (double) nW / tot;
		}
		
		OWP[i] = 0;
		int num = 0;
		double sum = 0.0;
		for ( int j = 0; j < n; j ++ )
		{
			if ( cmp[i][j] != '.' )
			{
				num ++;
				sum += WP1[j];
			}
		}			
		OWP[i] = sum / num;
	}
	
	for (int i = 0; i < n; i ++ )
	{
		int num = 0;
		double sum = 0.0;
		for ( int j = 0; j < n; j ++ )
			if ( cmp[i][j] !='.' )
			{
				num ++;
				sum += OWP[j];
			}
		OOWP[i] = sum / num;
	}
	
	for ( int i = 0; i < n; i ++)
	{
		double res = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		fout<<res<<endl;
	}
	
}
int main() {
  
	int N;
	fin>> N;
	for( int n = 1; n <= N; n++)
	{
		fout<<"Case #"<<n<<":"<<endl;
		run();
		//printf("Case #%d: %d\n", n, ret);
		
   }
   return 0;
}