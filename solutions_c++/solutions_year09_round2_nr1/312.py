#include <cstdio>
#include <iostream>
#include <fstream>
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
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int N,L,A;
double re;
string tt;
vector<string> an;
vector < set<string> > fts;

fstream fin("A-large.in",ifstream::in);
fstream fout("A-large.out",ofstream::out);

struct dtrnod {
	int f;
	double w;
	string ft;
	int t1;
	int t2;
};

vector< dtrnod > trs;
vector< string > tmp;
int gli = 0;
stringstream ss (stringstream::in | stringstream::out);

void rea()
{
	int ci = gli;
	dtrnod ret;
	trs.push_back(ret);
	gli++;
	string t;
	if (tmp.size()==0)
	{
		ss >> ret.w;
	}
	else 
	{
		stringstream s1 (stringstream::in | stringstream::out);
		s1 << tmp[0];
		s1 >> ret.w;
		tmp.erase(tmp.begin());
	}
	ss >> t;
	if (t[0]>='a' && t[0]<='z')
	{
		ret.f = 1;
		ret.ft = t;
		ret.t1 = gli;
		rea();
		ret.t2 = gli;
		rea();
	}
	else
	{
		ret.f = 0;
		ret.t1 = ret.t2 = -1;
		ret.ft = "";
		tmp.push_back(t);
	}
	trs[ci] = ret;
}

int main()
{
    fin >> N;
    for(int j=1;j<=N;j++)
    {
		fin >> L;
		getline(fin,tt);
		gli = 0;
		trs.resize(0);
		string t;
		t = "";
		rep(i,L)
		{
			getline(fin,tt);
			t = t + " " + tt;
		}
		rep(i,t.size())
			if (t[i]=='(' || t[i]==')') { t.erase(t.begin()+i); i--; }
		ss.clear();
		ss << t;
		tmp.resize(0);
		rea();
		fin >> A;
		int fnu;
		an.resize(A);
		fts.resize(A);
		rep(i,A)
		{
			fin >> t;
			fts[i].clear();
			an[i] = t;
			fin >> fnu;
			rep(k,fnu) { fin >> t; fts[i].insert(t); }
		}
		fout << "Case #" << j << ":\n";
		rep(i,A)
		{
			double p = 1.0;
			int st = 0;
			while(1)
			{
				p*=trs[st].w;
				if (trs[st].f==0) break;
				if (fts[i].count(trs[st].ft)) st = trs[st].t1;
				else st = trs[st].t2;
			}
			fout << p << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
