#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define REP(i,n) FOR(i,0,(n))
#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define all(x) (x).begin(),(x).end()


using namespace std;

int N;
int NA;
int NB;
int T;

enum station
{
	A,
	B
};

enum type
{
	dep,
	arr
};

struct tick
{
	struct comp
	{
		bool operator()(const tick& t1, const tick& t2) const
		{
			if (t1.t == t2.t)
			{
				if (t1.da == dep)
					return false;
				else
					return true;
			}
			return (t1.t < t2.t);
		}
	};

	void
	stock(int& a,int& b) const
	{
		if (da == dep)
			(s==A?++a:++b);
		else
			(s==A?--b:--a);
	};

	friend
	ostream&
	operator<<(ostream& os, const tick& t)
	{
		os << "t: " << t.t << " station: " << t.s << " type: " << t.da << endl;
		return os;
	}

	unsigned int t;
	station s;
	type da;
	static const comp op;
};

void
read(FILE * in,vector<tick>& v)
{
	fscanf(in,"%d\n",&T);
	fscanf(in,"%d %d\n",&NA,&NB);
	//cout << "T: " << T << endl;
	//cout << "NA: " << NA << " NB: " << NB << endl;
	REP(n,NA)
	{
		tick t1,t2;
		t1.s = A;
		t2.s = A;
		t1.da = dep;
		t2.da = arr;
		int h1,m1,h2,m2;
		fscanf(in,"%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
		t1.t = 60*h1+m1;
		t2.t = 60*h2+m2+T;
		//cout << "dep: " << t1.t << " arr: " << t2.t << endl;
		v.push_back(t1);
		v.push_back(t2);
	}
	REP(n,NB)
	{
		tick t1,t2;
		t1.s = B;
		t2.s = B;
		t1.da = dep;
		t2.da = arr;
		int h1,m1,h2,m2;
		fscanf(in,"%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
		t1.t = 60*h1+m1;
		t2.t = 60*h2+m2+T;
		//cout << "dep: " << t1.t << " arr: " << t2.t << endl;
		v.push_back(t1);
		v.push_back(t2);
	}
	return;
};

void
solve(vector<tick>& v, int& a, int& b)
{
	sort(all(v),tick::op);
	int max_dem_A=0,max_dem_B=0,pend_dem_A=0,pend_dem_B=0;
	FORE(t,v)
	{
		t->stock(pend_dem_A,pend_dem_B);
		if (pend_dem_A > max_dem_A)
			++max_dem_A;
		if (pend_dem_B > max_dem_B)
			++max_dem_B;
	}
	a = max_dem_A;
	b = max_dem_B;
};

int main(int argc, char* argv[])
{
	FILE * in = fopen(argv[1],"r");
	if (!in)
		return 1;
	fscanf(in,"%d\n",&N);
	//cout << "N: " << N << endl;
	REP(n,N)
	{
	  vector<tick> v;
	  read(in,v);
		int a,b;
		solve(v,a,b);
		cout << "Case #" << n+1 << ": " << a << " " << b << endl;
	};
	return 0;
};
