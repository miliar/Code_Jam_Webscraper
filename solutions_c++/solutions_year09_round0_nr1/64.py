#include <cassert>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))

#define pb push_back
#define sz size()

vector<string> A;
vector<string> T;

int main()
{
	int L, D, N;
	cin >> L >> D >> N;
	FOR(i,0,D)
	{
		string a;
		cin >> a;
		assert(a.sz == L);
		A.pb(a);
	}
	FOR(i,0,N)
	{
		string a;
		cin >> a;
		T.clear();
		int par = 0, tok = 0;
		while(par < a.sz)
		{
			string t = "";
			if(a[par] == '(')
			{
				par++;
				while(a[par] != ')')
					t += a[par++];
			}
			else t += a[par];
			T.pb(t);
			par++;
		}
		assert(T.sz == L);
		int cnt = 0;
		FOR(p,0,D)
		{
			int f = 1;
			FOR(q,0,L)
			{
				int fo = 0;
				FOR(r,0,T[q].sz) if(T[q][r] == A[p][q]) { fo = 1; break;}
				if(!fo) { f = 0; break;}
			}
			cnt += f;
		}
		cout << "Case #" << i+1 << ": " << cnt << endl;
	}
	return 0;
}
