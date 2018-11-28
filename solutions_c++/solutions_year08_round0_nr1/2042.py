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

//this could be O(Q) in memory, but whatever
int memo[101][1001];
int q[1001];

int S;
int Q;

int fewest(int eng, int pos)
{
	if(pos == 0) return (q[0] == eng) ? (1<<29) : 0; 
	if(memo[eng][pos] != -1) return memo[eng][pos];

	int ret = q[pos-1] == eng ? (1<<29) : fewest(eng,pos-1);
	FU(i,0,S)
	{
		if(q[pos-1] == i || eng == i) continue;
		ret = min(ret,fewest(i,pos-1)+1);
	}

	return memo[eng][pos] = ret;
}

void main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	
	int N;
	in >> N;

	FU(ZZZ,0,N)
	{
		map<string,int> sId;
		FU(i,0,101) FU(j,0,1001) memo[i][j] = -1;
		
		//read search engines
		in >> S;	
		string crap;
		getline(in,crap);

		FU(i,0,S)
		{
			string name;
			getline(in,name);
			sId[name] = i;
		}

		//read queries
		in >> Q;
		getline(in,crap);

		FU(i,0,Q)
		{
			string name;
			getline(in,name);
			q[i] = sId[name];
		}

		if(Q == 0) out << "Case #" << ZZZ+1 << ": " << 0 << endl;

		else
		{

		int ans = (1<<30);
		FU(i,0,S)
		{
			if(i == q[Q-1]) continue;
			ans = min(ans,fewest(i,Q-1));
		}

		out << "Case #" << ZZZ+1 << ": " << ans << endl;
		}
	}

}