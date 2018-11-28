
//#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
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

vector<string> split( string s, string c )
{
	vector<string> ret;
	for( unsigned int i=0, n; i <= s.length(); i=n+1 ){
		n = s.find_first_of( c, i );
		if( n == string::npos ) n = s.length();
		string tmp = s.substr( i, n-i );
		ret.push_back(tmp);
	}
	return ret;
}

//#########################################################
struct header
{
	int prob_num;//i/f

	void read(istream& is);
};


struct answer;

struct problem
{
	unsigned int N;

	vector<pair<int,int>> wire;

	void read(istream& is);
	answer solve();
};

struct answer
{
	int n;

	void write(ostream& os);
};

//#########################################################
void header::read(istream& is)
{
	is >> prob_num;
}

void problem::read(istream& is)
{
	is >> N;

	wire.resize(N);
	generate(wire.begin(),wire.end(),[&]()->pair<int,int>{
		int a,b;
		is >> a >> b;
		return pair<int,int>(a,b);
	});
}

answer problem::solve(){
	answer ans;

	ans.n=0;

	sort(wire.begin(), wire.end());

	auto e = wire.end();
	for(auto a = wire.begin(); a != e; ++a){
		for(auto b = a+1; b != e; ++b){
			if((*a).second > (*b).second){
				ans.n++;
			}
		}
	}

	return ans;
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