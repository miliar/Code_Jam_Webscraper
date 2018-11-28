
#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include<cassert>
#include<set>
#include<cstring>
#include<list>
#include<numeric>
#include<cassert>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 100000000

using namespace std;

typedef long long ll;

int main()
{
	int L, D, N;
	vector<string> words;
	cin >> L >> D >> N;
	fup(i, 1, D)
	{
		string s;
		cin >> s;
		words.push_back(s);
	}
	fup(i, 1, N)
	{
		string s;
		cin >> s;
		bool t[30][30];
		memset(t, 0, sizeof(t));
		int kt = 0;
		int score = 0;
		bool paran = false;
		REP(j, s)
		{
			if(s[j] == '(')
			{
				paran = true;
			}
			else if(s[j] == ')')
			{
				paran = false;
				kt ++;
			}
			else if(s[j] >= 'a' and s[j] <= 'z')
			{
				t[kt][s[j] - 'a'] = 1;
				if(!paran) kt ++;
			}
		}
		REP(j, words)
		{
			bool add = true;
			REP(k, words[j])
			{
				if(t[k][words[j][k] - 'a'] == 0)
				{
				   	add = false;
					break;
				}
			}
			if(add) score ++;
		}
		cout << "Case #" << i << ": " << score << endl;
	}

	return 0;
}



