#include<iostream>
#include<set>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
#define forn(i,n) for(int i = 0; i < n; i++)

int a[1000];
int x[1000];

int main()
{
	freopen("C:\\1.txt","rt",stdin);
	freopen("C:\\2.txt","wt",stdout);
	int T;
	cin >> T;
	for(int test = 0; test < T; test++)
	{
		int p,q;
		cin >> p >> q;
		forn(i,q) cin >> a[i];
	
		vector<int> b;
		b.resize(q);
		forn(i,q) b[i] = i;
		int tmin = 100000000;
		do 
		{
			forn(i,p+1) x[i] = 0;
			int ts = 0;
			for(int i = 0; i < q; i++)
			{
				int cur = a[ b[i] ];
				x[ cur ] = 1;
				for(int j = cur - 1; j >= 1 && x[j] == 0; j-- ) ts++;
				for(int j = cur + 1; j <= p && x[j] == 0; j++) ts++;
			}		
			if ( ts < tmin ) tmin = ts;
		} while ( next_permutation(b.begin(), b.end()) );
		cout << "Case #" << test + 1 << ": ";
		cout << tmin << endl;
	}
		return 0;
}