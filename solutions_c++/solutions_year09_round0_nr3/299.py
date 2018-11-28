
#include <iostream> 
#include <vector> 
#include <string>

using namespace std;

const string b("welcome to code jam");
//const string b("a");
const int MAXLEN = 501; 
const int m = b.length();
int n;
string a;
int cnt[MAXLEN][20];

void InitArray()
{
	for (int i=0; i<n; ++i)
		for (int j=0; j<m; ++j)
			cnt[i][j] = -1;
	for (int i=0; i<=n; ++i)
		cnt[i][m] = 1;
	for (int i=0; i<m; ++i)
		cnt[n][i] = 0;
}

int Count( int i, int j )
{
	if ( cnt[i][j] > -1 ) return cnt[i][j];
	//if ( i == n ) return cnt[i][j] = 0;

	if ( a[i] == b[j] ) { return cnt[i][j] = (Count( i + 1, j + 1 ) + Count( i + 1, j )) % 10000; }
	else return  cnt[i][j] = Count(i+1, j);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int N;
	
	cin >> N; 
	cin.get();
	for (int i=1; i<=N; ++i)
	{
		char astr[MAXLEN];
		cin.getline(astr, MAXLEN);
		a = astr;
        n = a.length();		
		InitArray();
		cout << "Case #"<<i << ": " ;
		int number = Count(0, 0);
		if (number < 1000) cout << 0;
		if (number < 100) cout << 0;
		if (number < 10) cout << 0;
		cout << number;
		cout << "\n";
	}
	return 0;
}
