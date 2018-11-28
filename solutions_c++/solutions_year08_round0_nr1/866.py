#include <cstdio>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

int n , m;
string s[128];
string q[1024];

int used[1024];

void read() {
	int i;
	
	cin >> n;
	getchar();
	for (i=1;i<=n;i++)
		getline ( cin , s[i] );
	
	cin >> m;
	getchar();
	for (i=1;i<=m;i++)
		getline ( cin , q[i] );
}

void solve() {
	int ans = 0;
	int i , j , k;
	int cur;
	
	for (i=1;i<=m;i++) {
		cur = 0;
		
		for (j=1;j<=n;j++)
			used[j] = 0;
		
		for (j=i;j<=m;j++)
			for (k=1;k<=n;k++)
				if ( !used[k] )
					if ( q[j] == s[k] )
						used[k] = j;
		
		cur = 0;
		for (j=1;j<=n;j++) {
			if ( used[j] > cur )
				cur = used[j];
			if ( !used[j] )
				cur = m + 1;
		}
		
		if ( cur != m + 1 ) 
			++ ans;
		i = cur - 1;
	}
	
	cout << ans << endl;
}

int main() {
	int k;
	int i = 1;
	
	cin >> k;
	while ( k -- ) {
		read();
		printf ("Case #%d: ",i);
		solve();
		
		++ i;
	}
	
	return 0;
}
