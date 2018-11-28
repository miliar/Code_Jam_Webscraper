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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
#include <queue>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("a.in");
ofstream fout("a.out");

int T;

int W;

double P1[110][2];
double P2[110][2];
int A;
int B;
int N;

double P[220][2];
double getArea(int pn)
{
	double area = 0;


	for(int i = 1; i+1<pn; i++){
		double x1 = P[i][0] - P[0][0];
		double y1 = P[i][1] - P[0][1];
		double x2 = P[i+1][0] - P[0][0];
		double y2 = P[i+1][1] - P[0][1];
		double cross = x1*y2 - x2*y1;
		area += cross;
	}
	return abs(area/2.0);

	
}
double getTy(double pp[][2], int n, double tx)
{
	for(int i=0;i+1<n;i++)
	{
		if(pp[i][0]<tx+eps && pp[i+1][0]+eps>tx)
		{
			return ((pp[i+1][1] - pp[i][1])/(pp[i+1][0]-pp[i][0]))*(tx-pp[i][0]) + pp[i][1];
		}
	}
	assert(false);
	return 0.0;
}
int main()
{
	
	fin>>T;
	for(int c=1;c<=T;c++)
	{
		fin>>W>>A>>B>>N;
		int x,y;

		for(int i=0;i<A;i++)
		{
			fin>>x>>y;
			P1[i][0] = x;
			P1[i][1] = y;

		}
		for(int i=0;i<B;i++)
		{
			fin>>x>>y;
			P2[i][0] = x;
			P2[i][1] = y;
		}
		int pi = 0;
		for(int i=0;i<B;i++)
		{
			P[i][0] = P2[i][0];
			P[i][1] = P2[i][1];

		}
		pi = B;
		for(int i=A-1;i>=0;i--)
		{
			P[pi][0] = P1[i][0];
			P[pi++][1] = P1[i][1];


		}
		double Area = getArea(pi);

		vector<double> res;
		res.push_back(0.0);
		for(int i=1;i<N;i++)
		{
			double targetArea = (Area*i)/N;
			double left = res[i-1];
			double right = W;
			while(left+eps<right)
			{
				double tx = (left+right)/2.0;
				double ty1 = getTy(P1,A,tx);
				double ty2 = getTy(P2,B,tx);
				
				int pi = 0;
				for(int i=0;i<B;i++)
				{
					if(P2[i][0]+eps > tx) break;
					P[pi][0] = P2[i][0];
					P[pi][1] = P2[i][1];
					pi++;
				}
				P[pi][0] = tx;
				P[pi++][1] = ty2;
				P[pi][0] = tx;
				P[pi++][1] = ty1;
			
				for(int i=A-1;i>=0;i--)
				{
					if(P1[i][0]+eps > tx) continue;
					P[pi][0] = P1[i][0];
					P[pi++][1] = P1[i][1];
				}
				double tArea = getArea(pi);
				if(tArea > targetArea)
					right = tx;
				else
					left = tx;
			}
			res.push_back(left);
		}



		cout<<"Case #"<<c<<":"<<endl;
		fout<<"Case #"<<c<<":"<<endl;

		 cout.setf(ios::fixed,ios::floatfield);
		 fout.setf(ios::fixed,ios::floatfield);
		for(int i=1;i<N;i++)
		{
			cout<<setprecision(8)<<res[i]<<endl;
			fout<<setprecision(8)<<res[i]<<endl;

		}
		
	}
	return 0;
}
