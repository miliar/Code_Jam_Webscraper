#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <sstream>
#include <cmath>
#include <cassert>
#include <fstream>
using namespace std;
 
#define MSG(a)  cout << #a << "=" << a << endl;
#define VAR(a,b) __typeof(b) a=b
#define FORIT(it,v) for(VAR(it,(v).begin());it!=(v).end();++(it))
template<class T, class U> T cast (U x) { T y; ostringstream a; a<<x; 
istringstream b(a.str()); b>>y; return y; }
#define SZ(v) ((int)(v).size())
#define FU(i,a,b) for(int i=(a);i<int(b);++i)
#define FD(i,a,b) for(int i=(a);i>=int(b);--i)
#define REP(i,n) FU(i,0,n)
#define ALL(a) a.begin(),a.end()
#define ISS istringstream
#define OSS ostringstream

map<string, bool> hasDir;



int Traverse(string& s)
{
	int ret = 0;
	string::iterator it = s.begin();
	while(true)
	{
		it = find(it,s.end(),'/');
				
		if (!hasDir[s.substr(0,it-s.begin())])
		{
			string add = s.substr(0,it-s.begin());
			hasDir[add] = true;
			++ret;
		}

		if(it == s.end())
			break;

		++it;
	}

	return ret;
}

int Traverse(char* str)
{
	return Traverse( string(str) );
}

void main()
{
	ifstream in("in.txt");
  ofstream out("out.txt");

	int T;
	in >> T;

	REP(zzz,T)
	{
		out << "Case #" << zzz+1 << ": ";
		int N,M;
		in >> N >> M;

		hasDir = map<string,bool>();
		hasDir[""] = true;

		FU(i,0,N)
		{
			string path;
			in >> path; 
			Traverse(path);
		}

		int ret = 0;
		FU(i,0,M)
		{
			string path;
			in >> path;
			ret += Traverse(path);
		}

		out << ret << endl;
	}
}