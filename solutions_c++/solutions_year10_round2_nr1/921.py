#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue>  
#include <iostream> 
#include <iterator> 
#include <math.h> 
#include <cstdio> 
#include <cstdlib> 
#include <sstream> 
#include <limits.h>

//#pragma comment(linker, "/STACK:60777216") 

using namespace std; 

typedef pair<int,int> pii; 
typedef long long ll; 
typedef vector<int> vi; 

#define UN(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end()) 
#define SORT(c) sort((c).begin(),(c).end()) 
#define FOR(i,a,b) for (int  i=(a); i < (b); i++)  
#define REP(i,n) FOR(i,0,n)  
#define CL(a,b) memset(a,b,sizeof(a)) 
#define pb push_back  

using namespace std;

vector<string> dict;
vector<string> dirs;
set<string> allDirs;

int N, M;

int addDir(string s)
{
	int ret = 0;

	while(s.length() > 0)
	{
		if( allDirs.find(s) != allDirs.end()) break;

		allDirs.insert( s );
		++ret;

		int ind = s.find_last_of('/');
		if(ind > 0 )
			s = s.substr(0,ind);
		else s = "";
	}

	return ret;
}

int solve()
{
	//create dirs;

	for(int i = 0; i < N; ++i)
	{
		string& s = dict[i];
		
		addDir(s);
	}

	int ret = 0;

	for(int i = 0; i < M; ++i)
	{
		ret += addDir(dirs[i]);
	}
	
	return ret;
}

int main () 
{
  freopen("input","r",stdin);
  freopen("output","w",stdout);

  int tests;
  
  scanf("%d", &tests);
  
  for (int test = 0; test < tests; ++test) 
  {    
	scanf("%d %d", &N, &M);
	string s;

	dict.clear();
	dirs.clear();
	allDirs.clear();

	for(int i = 0; i < N; ++i)
	{		
		cin >> s;
		dict.push_back(s);
	}

	for(int i = 0; i < M; ++i)
	{		
		cin >> s;
		dirs.push_back(s);
	}

	//sort(dict.begin(), dict.end());

    int res = solve();
    
	printf("Case #%d: %d\n", (test+1) , res);
	fflush(stdout);
  }
};
