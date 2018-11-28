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
#include <fstream>
#include <cassert>
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

const int BLUE = 0;
const int ORANGE = 1;
const int NEITHER = 2;

void main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;

	FU(i,0,T)
	{
		int N;
		in >> N;

		vector<int> color;
		vector<int> pos(N);

		FU(i,0,N)
		{
			string C;
			in >> C >> pos[i];
			color.push_back( (C == "O") ? ORANGE : BLUE );
		}

		int lstPos[2] = { 1, 1 };
		//time
		int tm = 0;
		//ctm[i] is one time after the last time robot i pressed a button
		int ctm[2] = { 0, 0 };
		//The posistion robot i was in the last time it pressed a button
		int cps[2] = { 1, 1 };
		FU(i,0, SZ(color))
		{
			int c = color[i];

			if (i == 0 || color[i-1] == c)
			{
				tm = tm + abs(cps[c]-pos[i]) + 1;
			}
			else
			{
				tm = max(
					tm+1, 
					ctm[c] + abs(cps[c]-pos[i])+1
				);
			}

			ctm[c] = tm;
			cps[c] = pos[i];
		}

		out << "Case #" << i+1 << ": " << tm << "\n";
	}
}