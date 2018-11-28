
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>
#include<ctime>

using namespace std;

const double EPS = 1e-9;
//const long long  INF = 1000000000000000000;

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long

//void precompute()
//{
//	int n ;
//	map<char,char> tr;
//	cin>>n;
//	vector<string> en(n) , dec(n);
//	string line;
//	getline(cin,line);
//	REP(i,n)
//	{
//		getline(cin,line);
//		en[i] = line;
//	}
//	REP(i,n)
//	{
//		getline(cin,line);
//		dec[i] = line;
//	}
//
//	REP(i,n)
//	{
//		REP(j,en[i].size())
//		{
//			tr[en[i][j]] = dec[i][j];
//		}
//	}
//
//	tr['z'] = 'q';
//
//	map<char,char>::iterator it = tr.begin();
//	for(;it!=tr.end();++it)
//	{
//		cout<<"tr[\'"<<it->first<<"\'] = \'"<<it->second<<"\';" <<endl;
//	}
//
//
//}

map<char,char> tr;

void init()
{
	tr[' '] = ' ';
	tr['a'] = 'y';
	tr['b'] = 'h';
	tr['c'] = 'e';
	tr['d'] = 's';
	tr['e'] = 'o';
	tr['f'] = 'c';
	tr['g'] = 'v';
	tr['h'] = 'x';
	tr['i'] = 'd';
	tr['j'] = 'u';
	tr['k'] = 'i';
	tr['l'] = 'g';
	tr['m'] = 'l';
	tr['n'] = 'b';
	tr['o'] = 'k';
	tr['q'] = 'z';
	tr['p'] = 'r';
	tr['r'] = 't';
	tr['s'] = 'n';
	tr['t'] = 'w';
	tr['u'] = 'j';
	tr['v'] = 'p';
	tr['w'] = 'f';
	tr['x'] = 'm';
	tr['y'] = 'a';
	tr['z'] = 'q';
}


int main()
{
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output_a.txt","w",stdout);
#endif

	init();

	int n;
	cin>>n;
	string line;
	getline(cin,line);
	REP(i,n)
	{
		getline(cin,line);
		cout<<"Case #"<<i+1<<": ";
		REP(j,line.size())
		{
			cout<<tr[line[j]];
		}
		cout<<endl;
	}	

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}