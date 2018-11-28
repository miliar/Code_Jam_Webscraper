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

void main()
{
	ifstream in("in.txt");
  ofstream out("out.txt");

	int T;
	in >> T;

	REP(zzz,T)
	{
		out << "Case #" << zzz+1 << ": ";
		int N,K;
		in >> N >> K;

		//is K congruent to -1 mod 2^n ? if so, return ON. else, return off.
		int modulus = 1;
		REP(i,N) modulus *= 2;

		if(K%modulus == modulus-1)
			out << "ON" << endl;
		else
			out << "OFF" << endl;
	}
}