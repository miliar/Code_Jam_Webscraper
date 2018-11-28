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

ifstream fin("c:\\B-small-attempt0.in");
ofstream fout("c:\\B-small-attempt0.out");

bool check(double t, vector<double>& pos, double d )
{
	double p = pos[0] - t;
	for ( int i = 1; i < pos.size(); i++)
	{
		double req = p + d;
		if ( pos[i] + t < req ) return false;
		if ( pos[i] - t > req ) p = pos[i] - t;
		else
			p = req;
	}
	return true;
	
}

double run()
{
	int n; 
	double	d;
	fin >> n >> d;
	vector<double> pos;
	for ( int i = 0; i < n; i ++)
	{
		double p;
		int v;
		fin >> p >> v;
		for ( int k = 0; k < v; k ++ )
			pos.push_back(p);
	}
		sort(pos.begin(), pos.end());
		if ( check(0,pos,d) ) return 0;
		double minT = 0;
		double maxT = d * pos.size() + (pos.back() - pos[0]);
		//cout<<check(2.5,pos,d);
		//for ( int i = 0; i < pos.size(); i++)
		//	cout<<pos[i]<<' ';
		//cout<<endl;
		while ( maxT - minT > 0.00000001 )
		{
			double mid = (maxT + minT)/2;
			//cout<<mid<<endl;
			if ( check(mid,pos,d) ) maxT = mid;
			else minT = mid;
			//cout<<minT<<' '<<maxT<<endl;
		}
		//cout<<minT<<' '<<maxT<<endl;
		return maxT;			
}
int main() {
  
	int N;
	fin>> N;
	for( int n = 1; n <= N; n++)
	{
		double ret = run();
		//printf("Case #%d: %d\n", n, ret);
		fout<<"Case #"<<n<<": "<<ret<<endl;
   }
   return 0;
}