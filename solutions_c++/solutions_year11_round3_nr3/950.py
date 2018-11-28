#pragma warning(disable : 4996)
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#define F(i,a) for(int i=0;i<int((a).size());i++)
#define INF 1000000000
#define MP make_pair
#define ALL(a) (a).begin(), (a).end()
#define X first
#define Y second
#define LL long long
#define LD long double
#define SQR(a) ((a)*(a))
using namespace std;

vector<int> a;

bool ok(int c)
{
	F(i,a)
		if (a[i]%c!=0 && c%a[i]!=0)
			return false;
	return true;
}

int main()
{
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);
	int ttt;
	cin >> ttt;
	for (int tt=1; tt<=ttt; ++tt)
	{
		int n,l,h;
		cin >> n >> l >> h;
		a.resize(n);
		F(i,a) cin >> a[i];
		int i;
		for (i=l; i<=h; ++i)
			if (ok(i))
				break;
		cout << "Case #" << tt << ": ";
		if (i<=h)
			cout << i << endl;
		else
			cout << "NO\n";
	}
	return 0;
}
