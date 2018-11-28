
#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <stdlib.h>
#include <utility>

#include <NTL/ZZ.h>

using namespace std;
using namespace NTL;

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
	int n;
	vector<ZZ> v;

	void read(istream& is);
	answer solve();
};

struct answer
{
	ZZ n;

	void write(ostream& os);
};

//#########################################################
void header::read(istream& is)
{
	is >> prob_num;
}

void problem::read(istream& is)
{
	int n;
	is >> n;
	v = read_vector<ZZ>(is, n);
}

answer problem::solve(){
	vector<ZZ> diffs(v.size()-1);

	sort(v.begin(), v.end());

	transform(v.begin(), v.end()-1, v.begin()+1, diffs.begin(), [](ZZ& a, ZZ& b)->ZZ{
		return b-a;
	});

	ZZ gcd = diffs[0];
	for_each(diffs.begin()+1, diffs.end(), [&](ZZ& a){
		gcd = GCD(gcd, a);
	});

	ZZ r = v[0]%gcd;
	ZZ n = (r==to_ZZ(0) ? to_ZZ(0) : gcd-r);

	answer a;
	a.n = n;

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

