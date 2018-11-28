
/***** Author : Akshay *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int, ii> Lii;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

/* Function for string split . If string starts with de-lim then call split(s.substr(1,s.length()),DELIM);
 *  *    else call split(s,DELIM);*/
std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) 
{
	std::stringstream ss(s);
	std::string item;
	while(std::getline(ss, item, delim)) 
		elems.push_back(item);
	return elems;
}
std::vector<std::string> split(const std::string &s, char delim) 
{
	std::vector<std::string> elems;
	return split(s, delim, elems);
}
string tostring(int n)
{
	stringstream ss ; ss<<n; return ss.str();
}
string gogo( char ch )
{
	string res = "a";
	res[0]= ch;
	return res;
}
int main()
{
	int n;
	string s,res;
	cin >> n;
	getchar();
	map<char,char> M;
	M['a']='y';
	M['b']='h';
	M['c']='e';
	M['d']='s';
	M['e']='o';
	M['f']='c';
	M['g']='v';
	M['h']='x';
	M['i']='d';
	M['j']='u';
	M['k']='i';
	M['l']='g';
	M['m']='l';
	M['n']='b';
	M['o']='k';
	M['p']='r';
	M['r']='t';
	M['s']='n';
	M['t']='w';
	M['u']='j';
	M['v']='p';
	M['w']='f';
	M['x']='m';
	M['y']='a';
	M['z']='q';
	M['q']='z';
	for(int i=0;i<n;i++)
	{
		getline( cin , s );
		res="";
		for( int j=0;j<(int)s.length();j++)
		{
			if( s[j] ==' ' ) res= res + " ";
			else res = res + gogo( M[s[j]] );
		}
		cout << "Case #" <<i+1<< ": " << res << endl;
	}
	return 0;
}
