#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;
#define LET(x,a) typeof(a)x(a)
#define FOR(i,a,n) for(LET(i,a);i<n;++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define cs c_str()
#define GI ({int t; scanf("%d",&t); t;})
#define EACH(it,v) for(LET(it,v.begin()); it!=v.end(); ++it)
#define dbg(x) (fout << #x << ":" << (x) << "\t")
#define dbge(x) (dbg(x), fout << endl)

ifstream fin("input.txt");
ofstream fout("output.txt");

typedef long double ld;

int main()
{

  	clock_t start=clock();
	
	int kases; fin>>kases;
	for(int kase = 0; kase<kases;++kase)
	{
		int N; fin>>N;
		int x[N], y[N], z[N], vx[N], vy[N], vz[N];
		
		ld a0=0, a1=0, b0=0, b1=0, c0=0, c1=0;
		REP(i,N)
		{
			fin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
			a0 += (ld)x[i];
			a1 += (ld)vx[i];
			b0 += (ld)y[i];
			b1 += (ld)vy[i];
			c0 += (ld)z[i];
			c1 += (ld)vz[i];
		}
		
		a0/=N; a1/=N; b0/=N; b1/=N; c0 /= N; c1 /= N;
		
		
		ld tmin = 0;
		if(a1*a1 + b1*b1 + c1*c1 > 0)tmin = -(a0*a1+ b0*b1+ c0*c1)/(a1*a1 + b1*b1 + c1*c1);
		if(tmin <= 0) tmin = 0;
		
		ld dmin = tmin*tmin*(a1*a1 + b1*b1 + c1*c1) + 2*tmin*(a0*a1+b0*b1+c0*c1) + (a0*a0 + b0*b0 + c0*c0);
		if(dmin < 0) dmin = -dmin;
		dmin = pow((double)dmin, (double)0.5);
		
		fout<<"Case #"<<(kase+1)<<": "<<dmin<<" "<<tmin<<endl;
	}

	clock_t end=clock();
	cout <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	
	return 0;
}
