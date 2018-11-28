#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int readint()
{
  int n;
  cin >> n;
  return n;
}

string readstring()
{
  string s;
  cin >> s;
  return s;
}

string readline()
{
	char buff[1000];
	cin.getline(buff,1000);
	
	if (cin.gcount() < 2)
	{
		cin.getline(buff,1000);
	}
	
	return string(buff);
}

class Fly
{
public:
	int x,y,z;
	int vx,vy,vz;
};

double x=0, y=0, z=0;
double vx=0, vy=0, vz=0;

double distat(double t)
{
	double mx = x + vx*t;
	double my = y + vy*t;
	double mz = z + vz*t;
	
	return sqrt(mx*mx+my*my+mz*mz);
}


int main(int argc, char* argv[])
{
	int start = clock();
	
	int T = readint();
	
	Fly fly[501];
	
	for (int test=1; test<=T; test++)
	{
		int N = readint();
		
		int sumx=0, sumy=0, sumz=0;
		int sumvx=0, sumvy=0, sumvz=0;
		
		for (int i=0; i<N; i++)
		{
			sumx += readint();
			sumy += readint();
			sumz += readint();
			sumvx += readint();
			sumvy += readint();
			sumvz += readint();
		}
		
		x = double(sumx) / N;
		y  = double(sumy) /N;
		z  = double(sumz) / N;
		vx = double(sumvx) /N;
		vy = double(sumvy) /N;
		vz = double(sumvz) /N;
		
		printf("%f %f %f %f %f %f\n", sumx, sumy, sumz, sumvx, sumvy, sumvz);
		
		
		double t0 = 0;
		double t1 = 6;
		double d0 = distat(t0);
		double d1 = distat(t1);
		
		
		
		while (d1 < d0)
		{
			t1 *= 2;
			d1 = distat(t1);
		}		
		
		double t2,d2,t3,d3;
		while (t1 - t0 > 0.000000001)
		{
			t2 = t0 + (t1-t0)/3;
			t3 = t0 + 2*(t1-t0)/3;
			
			d2 = distat(t2);
			d3 = distat(t3);
			
			if (d2 <= d3)
			{
				t1 = t3;
				d1 = d3;
			}
			else
			{
				t0 = t2;
				d0 = d2;
			}
		}
		
		
		fprintf(stderr, "Case #%d: %7f %7f\n", test, d0, t0);
		//cerr << "Case #" << test << ": " << d0 << " " << t0 << endl;
	}
	
	cout << "time used " << float(clock()-start)/CLOCKS_PER_SEC << endl;
}

