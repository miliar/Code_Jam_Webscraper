
#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <cmath>
#include <cstdio>
#include <algorithm>

#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for (int i = (a); (i) <= (b); (i)++)
using namespace std;

int n;
string a,b;
int s[200], used[200];




int main()

{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	FOR(i,1,26)
	{
		int x,y;
		cin >> x >> y;
		s[x] = y;
		used[y] = 1;
	}
	scanf("%d\n",&n);
	FOR(i,1,n)
	{
		getline(cin,a);
		int m = a.size();
		printf("Case #%d: ",i);
		for (int j = 0; j<m; j++)
		if (a[j] >= 'a' && a[j] <='z')
		{
			cout << char(s[int(a[j])]);
		} else cout << a[j];
		cout << endl;
	}
	return 0;
}
