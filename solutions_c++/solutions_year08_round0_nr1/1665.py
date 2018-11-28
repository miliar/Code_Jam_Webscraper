#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace __gnu_cxx;
using namespace std;

#define REP(i,n) for(uint i=0,_n=(n);i<_n;i++)
#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define X first
#define Y second
#define all(x) (x).begin(),(x).end()

typedef unsigned int uint;

uint N,S,Q;

void read(ifstream& ifs, vector<string>& v, uint& n)
{
	v.clear();
	string s;
	getline(ifs,s);
	istringstream iss(s);
	iss >> n;
	REP(i,n)
	{
		string s;
		getline(ifs,s);
		v.push_back(s);
	};
	return;
}

template <uint E>
void
find_set(const map<string,uint>& m, set<string>& s)
{
	s.clear();
	FORE(p,m)
	{
		if (p->second == E)
			s.insert(p->first);
	}
	return;
};

void
complete_run(const vector<string>& v, map<string,uint>& m)
{
	FORE(s_p,v)
	{
		if (m.find(*s_p) == m.end())
			m[*s_p] = 0;
	}
	return;
};

uint nb_switch(const vector<string>& engs, const vector<string>& queries)
{
	if (Q == 0)
		return 0;
	uint runs = 0;
	bool complete = false;
	map<string,uint> engs_cur,engs_save;
	REP(q,Q)
	{
		if (complete)
		{
			//complete = false;
			engs_cur.clear();
		}
		//while ( ((q+1) < Q) && (queries[q+1] == queries[q]) )
		//	++q;
		engs_cur[queries[q]] += 1;
		if (engs_cur.size() == S)
		{
			++runs;
			engs_cur.clear();
			//engs_save = engs_cur;
			//complete = true;
			--q;
		}
	}

	//if (complete || (runs == 0))
	//	return runs;
	//else
	//{
	//	set<string> cands,good_switch;
	//	complete_run(engs,engs_cur);
	//	find_set<0>(engs_cur, cands);
	//	find_set<1>(engs_save, good_switch);
	//	set<string> inter;
	//	set_intersection(all(cands),all(good_switch),inserter(inter,inter.begin()));
	//	if (inter.size() != 0)
	//		return runs;
	//	else
	//		return runs+1;
	//}
	return runs;
}

int main(int argc, char* argv[])
{
	ifstream infile(argv[1]);
	string s;
	getline(infile,s);
	istringstream iss(s);
	iss >> N;
	//cout << "N: " << N << endl;
	REP(i,N)
	{
		vector<string> engs,queries;
		read(infile,engs,S);
		//cout << "S: " << S << endl;
		//FORE (s_p, engs)
		//	cout << *s_p << endl;
		read(infile,queries,Q);
		//cout << "Q: " << Q << endl;
		//FORE (s_p, queries)
		//	cout << *s_p << endl;
		cout << "Case #" << i+1 << ": " << nb_switch(engs,queries) << endl;
	}
};