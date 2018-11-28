// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <string.h>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

//string split given string a and delimiters


int memo[501][21];

string gcj = "welcome to code jam";
string inp = "";

int welcome(int spot, int cc)
{
	if(cc == 19) return 1;
	if(spot == inp.size()) return 0;
	
	int & ret = memo[spot][cc];
	if(ret != -1) return ret;
	
	ret = 0;
	for(int i = spot; i < inp.size(); i++)
	{
		if(inp[i] == gcj[cc])
		{
			ret += welcome(i+1,cc+1);
			ret %= 10000;
		}
	}
	return ret;
}

int main()
{
	int TC = 0;
	cin >> TC;
	string buff = "";
	getline(cin,buff);
	for(int tcase = 1; tcase <= TC; tcase++)
	{

		getline(cin,buff);
		inp = buff;
	
		memset(memo,-1,sizeof(memo));
		
		
		int ret = welcome(0,0) % 10000;
		string fin = "";
		ostringstream oss;
		oss << ret;
		fin = oss.str();
		
		while(fin.size() < 4) fin = "0" + fin;
		
		
		cout << "Case #" << tcase << ": ";
		cout << fin << endl;
	
	}

  return 0;
}















