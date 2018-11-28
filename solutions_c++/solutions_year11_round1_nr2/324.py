#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef long long       Long;

#define toStr(a)      (((stringstream&)((stringstream()<<(a)))).str())
#define FOR(i,a,b)    for (int i = (a); i < (b); i++)
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it! = (c).end(); it++)
#define all(a)        ((a).begin(), (a).end())
#define pb(a)         push_back(a)
#define mp            make_pair
#define _x            first
#define _y            second

string dic[10005];
string strategy[128];
int N, M;

bool contains(string & s, char a)
{ return s.find(a) != string::npos; }

bool hasLocs(char a, vector<int> & loc, string & w)
{
	vector<int> loc2;
	FOR(i,0,(int)w.length())
		if (w[i] == a) loc2.push_back(i);

	if (loc.size() != loc2.size()) return false;
	FOR(i,0,loc.size())
		if (loc[i] != loc2[i]) return false;
	
	return true;
}

void print(vector<string> l)
{ 
	FOR(i,0,l.size()) cout << l[i] << " ";
	cout << endl;
}

int play(string word, string stra)
{
	int len = word.length();

	vector<string> cand;
	FOR(i,0,N)
		if (dic[i].length() == len) cand.push_back(dic[i]);

	int penalty = 0;
	int inx = 0;

	while (cand.size() > 1)
	{
		//cout << "============\n";
		//print(cand);

		vector<string> next;

		for (; inx < 26; inx++)
		{
			char a = stra[inx];
			FOR(i,0,(int)cand.size())
				if (contains(cand[i], a)) goto skip;
		}

		skip:

		char a = stra[inx]; inx++;
		//cout << "trying char - " << a << endl;
		vector<int> loc_reveal; //locations that will be revealed next turn
		FOR(i,0,len)
			if (word[i] == a)
				loc_reveal.push_back(i);

		if (loc_reveal.size() == 0) 
		{
			penalty++;
			FOR(i,0,(int)cand.size())
				if (!contains(cand[i], a))
					next.push_back(cand[i]);
		}
		else
		{
			FOR(i,0,(int)cand.size())
				if (hasLocs(a, loc_reveal, cand[i]))
					next.push_back(cand[i]);			
		}

		assert(cand.size() >= next.size());
		cand = next;
	}

	assert(cand[0] == word);
	return penalty;
}

int main()
{
	freopen("data.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin >> T;
	
	for (int x=1; x<=T; x++)
	{
		cout << "Case #" << x << ":" << flush; 

		cin >> N >> M;
		FOR(i,0,N)
			cin >> dic[i];

		FOR(i, 0, M)
			cin >> strategy[i];

		FOR(i,0,M)
		{
			int score = -1;
			string ans;

			FOR(j,0,N)
			{
				int sc = play(dic[j], strategy[i]);
				if (sc > score)
				{
					score = sc;
					ans = dic[j];
				}
			}
			cout << " " << ans << flush;
		}

		cout << endl;
	}
}