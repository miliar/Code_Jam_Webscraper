#include <iostream>
using namespace std;
string s[102], ss[102];
int n1, n2;
bool findPair( string ts )
{
	if ( ts.size() < 2 ) return 0;
	string ts1( ts, ts.size()-2);
	string ts2 = ts1.substr(1)+ ts1.substr(0,1);
	for ( int i = 1; i <= n1; ++i )
	{
		string tmp( s[i], 0, 2 );
		if ( !ts1.compare(tmp) || !ts2.compare(tmp) )
			return i;
	}
	return 0;
}
void makeNew( string& ts, int pos )
{
	ts.erase( ts.size()-2, 2 );
	ts +=  s[pos][2] ;
}
bool makeDispose( string ts )
{	
	char t = ts[ts.size()-1];
	for ( int i = 0; i < ts.size()-1; ++i )
		if ( ts[i] != t  )
		{
			for ( int j = 1; j <= n2; ++j )
			{
				if ( ss[j].find(t)< 100000 && ss[j].find(ts[i])<10000 )
					return true;
			}

		}
	return false;
}
int main()
{
	int T;
	cin >> T;
	for ( int ti = 1; ti <= T; ++ti )
	{
		int i;
		cin >> n1;
		for ( i = 1; i <= n1; ++i )
			cin >> s[i];
		cin >> n2;
		for ( i = 1; i <= n2; ++i )
			cin >> ss[i];
		int l; cin >> l;

		char c;
		string S;
		for ( i = 0; i < l; ++i )
		{
			cin >> c;
			S += c;
			while ( int w = findPair( S) )
				makeNew( S,w );
			if ( makeDispose(S) )
				S = "";
		}
		cout << "Case #" << ti << ": [";
		if ( S.size() > 0 )
		for ( i = 0; i < S.size()-1; ++i )
			cout << S[i] << ", ";
		if ( S.size() > 0 )cout << S[S.size()-1];
		cout << "]"<<endl;

	}
}
				
