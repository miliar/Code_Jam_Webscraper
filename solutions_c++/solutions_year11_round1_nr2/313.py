#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pii;
typedef long long ll;

#define I ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a ; i <= b ; i++)
#define REV(i,a,b) for(int i = a ; i >= b ; i--)
#define REP(i,n) for(int i = 0 ; i < n ; i++)

#define INF 1000000000

int cas;
int N,M;
vector<string> words;
vector<string> dicts;
string s,t;

bool find1(char c)
{
	int l = s.size();
	REP(i,l) if(s[i] == c) return true;
	return false;
}

bool find2(char c)
{
	int l = t.size();
	REP(i,l) if(t[i] == c) return true;
	return false;
}

bool match(char c)
{
	int l = s.size();
	REP(i,l) if( s[i] != t[i] && (s[i] == c || t[i] == c) ) return false;
	return true;
}

void solve()
{
	cin>>N>>M;
	words.resize(N);
	dicts.resize(M);

	REP(i,N) cin>>words[i];
	REP(i,M) cin>>dicts[i];

	cout<<"Case #"<<cas<<": ";
	REP(z,M)
	{
		int best = -1;
		int loc = -1;
		REP(i,N)
		{
			int score = 0;
			s = words[i];
			
			vector<bool> valid(N,true);
			REP(j,N) if(i==j || words[i].size() != words[j].size()) valid[j] = false;
			
			REP(k,26)
			{
				char c = dicts[z][k];
				bool f = false;
				REP(j,N)
				{
					if(valid[j] == false) continue;
					t = words[j];
					if(find2(c))
					{
						f = true;
						break;
					}
				}
				if( f == false && find1(c) == false ) continue;
				
				if(find1(c) == false) score++;
				REP(j,N)
				{
					if(valid[j] == false) continue;
					t = words[j];
					if(match(c) == false)
						valid[j] = false;
				}
			}
			

			if(score > best)
			{
				best = score;
				loc  = i;
			}
		}
		cout<<words[loc];
		if(z+1<M) cout<<" ";
	}
	cout<<endl;
}

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		cas++;
		solve();
	}


	return 0;
}
