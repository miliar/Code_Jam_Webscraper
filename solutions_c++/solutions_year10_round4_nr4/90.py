#include <iostream>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <cstdio>
#include <iomanip>

using namespace std;

#define PI (long double)2.0*acos((long double)0.0)

int dx[] = {0,1,1,1};
int dy[] = {1,-1,0,1};

int main()
{	
 	ifstream fin("D-small-attempt1.in");
 	ofstream fout("D-small1.out");
//	ofstream fout("D-test.out");
//	ifstream fin("D-test.in");
	
		
	int T;
	fin >> T;
	
	for(int t = 0; t < T; t++)
	{
		int N, M;
		fin >> N >> M;
		long double x1, y1, x2, y2;
		fin >> x1 >> y1 >> x2 >> y2;
		
		fout << "Case #" << t+1 << ": ";
		
		long double d = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
		
		for(int m = 0; m < M; m++)
		{
			long double x,y;
			fin >> x >> y;
			
			long double r = sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y));
			long double R = sqrt((x2-x)*(x2-x) + (y2-y)*(y2-y));
			
			if(r > R)
				swap(r,R);
			
			if(d-r >= R) fout << setprecision(8) << fixed << "0.0000000";
			else if(d+r <= R) fout << setprecision(8) << fixed << PI*r*r;
			else
			{
				long double A = r*r*acos((d*d+r*r-R*R)/(2.0*d*r))
				+ R*R*acos((d*d+R*R-r*r)/(2.0*d*R))
				- 0.5*sqrt((r+R-d)*(d+r-R)*(d-r+R)*(d+r+R));
				fout << setprecision(8) << fixed << A;
			}
			
			if(m != M-1) fout << " ";
		}
		fout << endl;
		
	}
	
	return 0;
}