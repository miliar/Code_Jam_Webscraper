#include<iostream>
#include<set>
#include<string>
#include<algorithm>
using namespace std;
#define forn(i,n) for(int i = 0; i < n; i++)


set<char> tset;
int a[1000];

int main()
{
	freopen("C:\\1.txt","rt",stdin);
	freopen("C:\\2.txt","wt",stdout);
	int T;
	cin >> T;
	for(int test = 0; test < T; test++)
	{
	int i;
	tset.clear();
	for(i = 0; i < 1000; i++) a[i] = 0;
	string s;
	cin >> s;
	for(i = 0; i < s.length(); i++) tset.insert(s[i]);
	int k =  tset.size();
	if ( k == 1 ) k = 2;
	a[0] = 1;
	for(i = 1; i < s.length(); i++)
	{
		int j;
		for(j = 0; j < i; j++) if ( s[j] == s[i] ) 
		{
			a[i] = 1;
			break;
		}
		if ( j == i ) { a[i] = 0; i++; break; }
	}
	int pos = 2;
	for(; i < s.length(); i++)
	{
		int j;
		for(j = 0; j < i; j++) if ( s[j] == s[i] ) 
		{
			a[i] = a[j];
			break;
		}
		if ( j == i )  { a[i] = pos; pos++; }
	}
	__int64 p, res = 0;
	for(i = s.length() - 1, p = 1; i >= 0; i--, p*=k )
	{
		res += p * a[i];
	}
	cout << "Case #" << test + 1 << ": ";
	cout << res << endl;
	}
	return 0;
}