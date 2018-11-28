#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include<climits>

using namespace std;

#define SZ(a) int((a).size())
#define PB push_back
#define MP make_pair
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;i++)
#define REV(i,a,b) for(int i=(int)a;i>(int)b;i--)
#define REP(i,n) for(int i=0;i<(int)n;i++)
#define SETBIT(a,b) a|=(1<<b)
#define UNSETBIT(a,b) a&=~(1<<b)
#define GETBIT(a,b) a&(1<<b)
#define FILL(a,b) memset(a,b,sizeof(a))
#define NBITS(a) __builtin_popcount(a)
#define INF 1000000000
#define EPS 1e-9
typedef long long LL;
typedef pair<int,int> PII;
vector<int> VI;
vector<vector<int> > VVI;
vector<string> VS;

////////// ACUTAL CODE STARTS HERE /////////


int N,M,ans;
vector<string> toAdd;
struct Node
{
	string s;
	vector<int> adj;
	Node(string _s){s=_s;}
};

vector<Node> G;

void Add(vector<string> add,int node)
{
	if(add.empty()) return;
	REP(i,SZ(G[node].adj)) if(G[G[node].adj[i]].s==add[0]) 
	{
		add.erase(add.begin(),add.begin()+1);
		Add(add,G[node].adj[i]);
		return;
	}
	Node temp(add[0]);
	G.PB(temp);
	G[node].adj.PB(SZ(G)-1);
	add.erase(add.begin(),add.begin()+1);
	Add(add,SZ(G)-1);
}


int main()
{
	//freopen("A_in.txt","r",stdin);					 freopen("A_out.txt","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large1.out","w",stdout);
	
	int Tests;
	cin>>Tests;
	REP(tests,Tests)
	{
		G.clear();
		Node TEMP("ROOT");
		G.PB(TEMP);
		cin>>N>>M;
		REP(i,N)
		{
			string s,str;
			cin>>s;
			REP(j,s.size()) if(s[j]=='/') s[j]=' ';
			istringstream in(s);
			toAdd.clear();
			while(in>>str) toAdd.PB(str);
			Add(toAdd,0);
		}
		ans=G.size();
		REP(j,M)
		{
			string s,str;
			cin>>s;
			REP(j,s.size()) if(s[j]=='/') s[j]=' ';
			istringstream in(s);
			toAdd.clear();
			while(in>>str) toAdd.PB(str);
			Add(toAdd,0);
		}
		ans=G.size()-ans;
		cout<<"Case #"<<tests+1<<": "<<ans<<endl;
	}
	return 0;
}
