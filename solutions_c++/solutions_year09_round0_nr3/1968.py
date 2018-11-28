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

string text = "welcome to code jam";

int main()
{
	int N;
	cin >> N;
	string nothing;
	getline(cin, nothing);
	fup(i, 1, N)
	{
		string s;
		getline(cin, s);
		int many[50];
		memset(many, 0, sizeof(many));
		many[0] = 1;
		REP(j, s)
		{
			fdo(k, siz(text) - 1, 0)
			{
				if(s[j] == text[k])
				{
					many[k + 1] += many[k];
					many[k + 1] %= 1000;
				}
			}
		}
		stringstream pp;
		pp << many[siz(text)];
		string score;
		pp >> score;
		while(siz(score) < 4) score = '0' + score;
		cout <<"Case #" << i << ": " << score << endl;
	}

	return 0;
}



