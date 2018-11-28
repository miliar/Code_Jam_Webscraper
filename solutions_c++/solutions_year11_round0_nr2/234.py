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

string input;
map<pair<char,char>,char > M;
vector<set<char> > V;
int t,N,cas;

vector<char> board;

void check1()
{
	if(board.size() < 2 ) return;
	int sz = board.size();
	char c1 = board[sz-2];
	char c2 = board[sz-1];
	if( M.find(make_pair(c1,c2)) != M.end() )
	{
		char c = M[make_pair(c1,c2)];
		board.pop_back();
		board.pop_back();
		board.push_back(c);
		check1();
	}
}

void check2()
{
	int sz = board.size();
	if( sz < 2 ) return;
	char c = board[sz-1];
	set<char> S = V[c-'A'];
	for(int i = 0 ; i < sz - 1 ; i++)
		if( S.find(board[i]) != S.end() )
		{
			board.clear();
			return ;
		}
}

void solve()
{
	board.clear();
	int len = input.size();
	REP(i,len)
	{
		char c = input[i];
		board.push_back(c);
		check1();
		check2();
	}
	int sz = board.size();
	cout<<"Case #"<<cas<<": ";
	cout<<"[";
	REP(i,sz-1) cout<<board[i]<<", ";
	if(sz-1 >= 0)
		cout<<board[sz-1];
	cout<<"]\n";
}
int main()
{
	cin>>t;
	cas=0;
	while(t--)
	{
		M.clear();
		V.clear();
		V.resize(26);
		cas++;
		cin>>N;
		FOR(i,1,N)
		{
			string temp;
			cin>>temp;
			M[make_pair(temp[0],temp[1])] = temp[2];
			M[make_pair(temp[1],temp[0])] = temp[2];
		}
		cin>>N;
		FOR(i,1,N)
		{
			string temp;
			cin>>temp;
			V[temp[0]-'A'].insert(temp[1]);
			V[temp[1]-'A'].insert(temp[0]);
		}
		cin>>N;
		cin>>input;
		solve();
	}
}
