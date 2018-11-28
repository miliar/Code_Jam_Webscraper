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

ifstream fin("c:\\A-large.in");
ofstream fout("c:\\A-large.out");

double run()
{
	vector<int> B,E,W,Len;
	int x,s,r,n;
	double t;
	fin >> x >> s >> r >> t >> n;
	int walk = x;
	for_(i,0,n)
	{
		int b,e,w;
		fin >> b>>e>>w;
		B.push_back(b);
		E.push_back(e);
		W.push_back(w);
		Len.push_back(e-b);
		walk -= e-b;
	}
	
	Len.push_back(walk);
	W.push_back(0);
	int num = W.size();
	for_(i,0,num)
		for_(j,i+1,num)
			if ( W[j]<W[i] )
			{
				int tmp;
				tmp = W[j]; W[j] = W[i]; W[i] = tmp;
				tmp = Len[j]; Len[j] = Len[i]; Len[i] = tmp;
			}
	double res = 0;
	//for_(i,0,num) cout<<Len[i]<<' ';
	//cout<<endl;
	//for_(i,0,num) cout<<W[i]<<' ';
	//cout<<endl;
	
	for_(i,0,num)
	{
		double time1 = (double)Len[i] / (W[i]+s);
		double time2 = (double)Len[i] / (W[i]+r);
		
		if ( time2 <= t )
		{
			t-= time2;
			res += time2;
		}
		else
		{
			res += t + (Len[i] - (W[i]+r) * t ) / (W[i]+s);
			t = 0;
		}
	}
	return res;
}
int main() {
  
	int N;
	fin>> N;
	for( int n = 1; n <= N; n++)
	{
		double ret = run();
		//printf("Case #%d: %d\n", n, ret);
		//out<<"Case #"<<n<<": "<<ret<<endl;
		fout << fixed;
		fout<<"Case #"<<n<<": "<<setprecision(10)<<ret<<endl;
   }
   return 0;
}