/* Brian's GCJ entries */
#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;
int bitct(long long r) {return r == 0 ? 0 : (bitct(r>>1) + (r&1));}
long long gcd(long long x, long long y) {return x ? gcd(y%x,x) : y;}
template<typename T> ostream& operator << (ostream &o,vector<T> v)
 {o<<"{";int i=0;for(;i<v.size()-1;i++)o<<v[i]<<", ";o<<v[i]<<"}";return o;}
long long choose(long long n, long long q)
{ if(n==0 || q==0) return 1;
	if (q==1) return n; else return ( choose(n, q-1) * (n-q+1 ) /q); }
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); ++i)

void calc(ifstream &, ofstream &);
main()
{
	stringstream filename, fnamein, fnameout;
	string file("C");
	filename << file << "-large.";
	fnamein << filename.str() << "in";
	fnameout << filename.str() << "out";

	ifstream fin(fnamein.str().c_str());
	ofstream fout(fnameout.str().c_str());
	int count;
	fin >> count;
	string test;
	getline(fin, test);
	for(int i=0;i<count;i++)
		{
		fout << "Case #" << (i+1) << ": ";
		calc(fin, fout);
		fout.flush();
		}

	fin.close();
	fout.close();
}

void calc(ifstream &fin, ofstream &fout)
	{
	string wcj("welcome to code jam");
	string test;
	getline(fin, test);
	cout << test << endl;

	vector<int> counts(wcj.size());

	for(int i=0;i<test.size();i++)
		{
		for(int j=0;j<wcj.size();j++)
			if(test[i]==wcj[j])
				{
				if(0==j)
					counts[j]=(counts[j]+1)%10000;
				else
					counts[j]=(counts[j]+counts[j-1])%10000;
				}
		}

	int ans=counts[wcj.size()-1]%10000;

	string shim("");
	if(ans < 10)
		shim = "000";
	else if(ans < 100)
		shim = "00";
	else if(ans < 1000)
		shim = "0";

	fout << shim << ans << endl;
	return; 
	}
