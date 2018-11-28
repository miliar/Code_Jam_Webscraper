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
#include <iomanip>
#include <queue>

using namespace std;
#define PI 3.14159265358979323846264338327950288
#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x))

ifstream fin("c:\\B-small-attempt0.in");
ofstream fout("c:\\B-small-attempt0.out");

string run()
{
	int R,C,D;
	fin >> R>>C>>D;
	vector<string> val;
	for_(i,0,R)
	{
		string s;
		fin >> s;
		val.push_back(s);
	}
	
	int maxC = 0;
	int maxK = min(R,C);
	for(int k=3; k<=maxK; k++)
	{
		for(int i=0; i+k<=R; i++)
			for(int j=0; j+k<=C; j++)
			{
				//cout<<k<<' '<<i<<' '<<j<<endl;
					double mx = 0;
					double my = 0;
					double cX = i + (double)k/2;
					double cY = j + (double)k/2;
					
					
				for_(i1,i,i+k)
				for_(j1,j,j+k)
				if ( !(i1 == i && j1 == j )
					&& !(i1 == i && j1 == j + k - 1 )
					&& !(i1 == i + k - 1 && j1 == j + k - 1 )
					&& !(i1 == i + k - 1 && j1 == j  )
					)
				{
					mx += (double(i1) + 0.5 - cX) * (val[i1][j1] - '0' + D);
					my += (double(j1) + 0.5 - cY) * (val[i1][j1] - '0' + D);
						//if ( k == 5 && i == 1 && j == 2 )
						//cout<<i1<<' '<<j1<<"}}}";
				
				}
				//cout<<fabs(mx)<<' '<<fabs(my)<<endl;
				if ( fabs(mx)<0.00000001 && fabs(my)<0.00000001) 
					{
						maxC = max(maxC,k);
						//cout<<k<<endl;
						//cout<<i<<' '<<j<<endl;
						//cout<<maxC<<' '<<mx<<' '<<my<<endl;
					}
			}
			//cout<<endl;
	}
		
	if ( maxC >= 3 )
	{
		ostringstream tr;
		tr<<maxC<<endl;
		return tr.str();
	}
	return string("IMPOSSIBLE");
}

int main() {
  
	int N;
	fin>> N;
	for( int n = 1; n <= N; n++)
	{
		string ret = run();
		//printf("Case #%d: %d\n", n, ret);
		fout<<"Case #"<<n<<": "<<ret<<endl;
		//fout << fixed;
		//fout<<"Case #"<<n<<": "<<setprecision(10)<<ret<<endl;
   }
   return 0;
}