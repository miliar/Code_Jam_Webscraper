
//#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <stdlib.h>
#include <utility>

// NTL:http://www.shoup.net/ntl/
//#include <NTL/ZZ.h>

using namespace std;
//using namespace NTL;

template<typename T>
vector<T> read_vector(istream& is, int n)
{
	vector<T> v(n);
	generate(v.begin(),v.end(),[&]()->T{
		T t;
		is >> t;
		return t;
	});
	return v;
}

template<typename T>
ostream& operator<<(ostream& os, vector<T>& v)
{
	bool fsp = false;
	for_each(v.begin(),v.end(),[&](T& t){
		if(fsp){os << " ";}
		fsp=true;
		os << t;
	});
	return os;
}

struct answer;
//#########################################################
struct header
{
	int prob_num;//i/f

	void read(istream& is);
};

struct problem
{
	int N;

	void read(istream& is);
	answer problem::solve();
};

struct answer
{
	int n;

	void write(ostream& os);
};

//#########################################################

long long comb(int n, int m)
{
	if(m>=n/2)m=n-m;

	long long x=1;
	for(int i=n-m+1; i<=n; ++i){
		x*=i;
	}
	for(int i=2; i<=m; ++i){
		x/=i;
	}
	return x%100003;
}

const int NMAX = 25;

vector<vector<int>> v(NMAX+1, vector<int>(NMAX+1,0));

void header::read(istream& is)
{
	is >> prob_num;


	v[2][1] = 1;

	for(int x=3; x<=NMAX; ++x){
		v[x][1]=1;
		for(int y=2; y<=x-1; ++y){
			v[x][y]=0;
			for(int z=max(1,y-(x-y)); z<=y-1; ++z){
				v[x][y]+=(v[y][z]*comb(x-y-1,y-z-1))%100003;
			}
		}
	}
}

void problem::read(istream& is)
{
	is >> N;
}

answer problem::solve()
{
	answer a;

	a.n=0;
	for(int i=1; i<N; ++i){
		a.n+=v[N][i];
	}

	a.n %= 100003;

	return a;
}

void answer::write(ostream& os)
{
	os << n;
}
//#########################################################
#pragma region
struct input_t
{
	header head;
	vector<problem> probs;
} input;

vector<problem> input_read(const string& filename)
{
	vector<problem> problems;

	ifstream ifs;
	ifs.open(filename, ios::in);
    
	input.head.read(ifs);

	int pn =  input.head.prob_num;

	problem c;
	for(int i=0;i<pn;++i){
		c.read(ifs);
		problems.push_back(c);
	}

	return problems;
}

ostream& operator<<(ostream& os, answer& a)
{
	a.write(os);
	return os;
}

#ifdef NDEBUG
const bool isDebug = false;
#else
const bool isDebug = true;
#endif

int main(int argc, char **argv){
	const string infile = (argc > 1 ? argv[1] : "test.txt");

	ofstream ofs(infile + ".out.txt");
	vector<problem> problems = input_read(infile);

	int n = 0;

	ostream &os = isDebug ? cout : ofs;

	for_each(problems.begin(), problems.end(), [&](problem &p){
		os << "Case #" << ++n << ": ";
		os << p.solve();
		os << endl;
	});
	
	cout<<"end";
	cin.get();
}
#pragma endregion

