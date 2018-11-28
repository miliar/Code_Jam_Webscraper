#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define rev(x) reverse((x).begin(), (x).end())
#define sor(x) sort(x.begin(), x.end())
#define sz size()
#define pb push_back
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define ll long long
#define fill(var,val) memset(var, val, sizeof(var))
#define rep(i, n) for(i = 0; i < n; i++)
#define repa(i, a, n) for(i = a; i < n; i++)
#define s(n) scanf("%d", &n);
#define p(n) printf("%d\n", n);

int main()
{
	int t;
	s(t);
	int k = 0;
	while(t--)
	{
		k++;
		int n, l, h;
		s(n);s(l);s(h);
		long long fp = 1;
		int i, j;
		vi freqs;
		rep(i,n) { int f;cin >> f; freqs.pb(f);  }
		sor(freqs);
		
		int freq = -1;
		repa(i,l,h+1)
		{
			bool found = true;
			rep(j,freqs.sz)	if(freqs[j]%i!=0 && i%freqs[j]!=0){found=false;break;}
			if(found) { freq=i;break;}
		}
		cout << "Case #" << k << ": ";
		if(freq == -1) cout << "NO" << endl;
		else cout << freq << endl;
	}
	return 0;
}
