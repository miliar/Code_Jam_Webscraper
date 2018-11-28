#include<list>
#include<set>
#include<map>
#include<ctime>
#include<stack>
#include<string>
#include<vector>
#include<cstdio>
#include<cmath>
#include<queue>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<iterator>
#include<cassert>
#include<fstream>
#include<numeric>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<algorithm>
using namespace std;
 
#define For(i,n) for( int i=0; i < n; i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define ALL(c)  c.begin() , c.end()
#define LL long long
#define SET(t,v) memset((t), (v), sizeof(t))

typedef vector < int > VI;
typedef pair< int , int > PII;
#define fr first
#define se second

string f( string s )
{
	string a = "abcdefghijklmnopqrstuvwxyz";
	string b = "yhesocvxduiglbkrztnwjpfmaq";
	string ret = "";
	For( i , s.size() )
		if( islower( s[i] ) )
			ret += b[ s[i]-'a' ];
		else
			ret += s[i];
	return ret;
}

int main()
{
	int t;
	string g;
	cin >> t;
	cin.ignore();
	For( i , t )
	{
		getline( cin , g );
		cout << "Case #" << i+1 << ": " << f(g) << endl;
	}
	return 0;
}
