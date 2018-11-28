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
#include <set>
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

typedef pair<char, char> ZZZ;

void main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	
	int T;
	in >> T;

	FU(ttt,0,T)
	{
		int C;
		in >> C;

		map<ZZZ, char> cm;
		map<char, vector<char> > op;

		FU(i,0,C)
		{
			string s;
			in >> s;

			cm[ ZZZ(s[0],s[1]) ] = s[2];
			cm[ ZZZ(s[1],s[0]) ] = s[2];
		}

		int D;
		in >> D;
		FU(i,0,D)
		{
			string s;
			in >> s;

			op[s[0]].push_back(s[1]);
			op[s[1]].push_back(s[0]);
		}

		int N;
		in >> N;

		string s;
		in >> s;

		stack<char> stck;
		map<char, int> all;

		FU(j,0,N)
		{
			if(stck.empty())
			{
				stck.push(s[j]);
				all[s[j]]++;
			}
			else
			{
				if(cm.count( ZZZ(stck.top(), s[j]) ) > 0)
				{
					char n = cm[ ZZZ(stck.top(), s[j]) ];
					all[stck.top()]--;
					if(all[stck.top()] == 0)
						all.erase( stck.top() );
					stck.pop();
					stck.push(n);
					all[n]++;
				}
				else
				{
					FU(k,0,SZ(op[s[j]]))
					{
						if (all.count(op[s[j]][k]) > 0)
						{
							stck = stack<char>();
							all = map<char,int>();
							goto next;
						}
					}

					stck.push(s[j]);
					all[s[j]]++;
				}

				next:;
			}
		}
		
		vector<char> ret(stck.size(), ' ');
		int i = 1;
		while(!stck.empty())
		{
			ret[SZ(ret)-i] = stck.top();
			stck.pop();
			++i;
		}

		out << "Case #" << ttt+1 << ": " << "[";
		FU(i,0,SZ(ret)-1)
			out << ret[i] << ", ";

		if(SZ(ret) > 0)
			out << ret[SZ(ret)-1];

		out << "]" << endl;
	}
}