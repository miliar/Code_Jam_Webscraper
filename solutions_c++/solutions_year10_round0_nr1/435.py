
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

//#########################################################
struct header
{
	int prob_num;//i/f

	void read(istream& is);
};

struct problem
{
	unsigned int n;
	unsigned int k;

	void read(istream& is);
};

struct answer
{
	bool b;

	void write(ostream& os);
};

//#########################################################
void header::read(istream& is)
{
	is >> prob_num;
}

void problem::read(istream& is)
{
	is >> n >> k;
}

answer solve(problem& p){
	answer a;

	unsigned int f = ~(~0u << p.n);
	unsigned int x = ((p.k+1) & f);
	a.b = !(bool)x;

	return a;
}

void answer::write(ostream& os)
{
	os << (b?"ON":"OFF");
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
		os << solve(p);
		os << endl;
	});
	
	cout<<"end";
	cin.get();
}
#pragma endregion