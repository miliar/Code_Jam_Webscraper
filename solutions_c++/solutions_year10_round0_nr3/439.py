
#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <stdlib.h>
#include <utility>

using namespace std;

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
	int R,k,N;
	vector<int> g;

	void read(istream& is);
	answer problem::solve();
};

struct answer
{
	unsigned long long e;

	void write(ostream& os);
};

//#########################################################
void header::read(istream& is)
{
	is >> prob_num;
}

void problem::read(istream& is)
{
	is >> R >> k >> N;
	g = read_vector<int>(is, N);
}

answer problem::solve()
{
	unsigned long long e=0;
	int p=0;
	int i=0;
	int offset=R;
	int cycle=1;
	unsigned long long off_e=0;
	unsigned long long cycle_e=0;
	int looped=false;
	vector<int> mark(N,-1);
	vector<unsigned long long> mark_e(N,0);
	for(i=0; i<R; ++i){
		int m=0;
		int prev_p=p;
		int tail_p;
		while(1){
			if(m+g[p] > k)break;
			m+=g[p];
			tail_p=p++;
			if(p==N){p=0;}
			if(p==prev_p)break;
		}
		e+=m;

		if(!looped){
			if(mark[tail_p]==-1){
				mark[tail_p]=i;
				mark_e[tail_p]=e;
			}else{
				offset=mark[tail_p];
				cycle=i-offset;
				off_e=mark_e[tail_p];
				cycle_e=e-off_e;

				i = R-((R-offset-1) % cycle)-1;
				looped=true;
			}
		}
	}

	answer a;
	int times = (R-offset-1) / cycle;
	a.e=e + cycle_e*(times-1);
	return a;
}

void answer::write(ostream& os)
{
	os << e;
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