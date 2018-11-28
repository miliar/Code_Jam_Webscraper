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

int main()
{
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);
	int ttt;
	cin >> ttt;
	for (int tt=1; tt<=ttt; ++tt)
	{
		int n,m;
		cin >> n >> m;
		vector<string> a(n);
		F(i,a) cin >> a[i];
		for (int i=0; i<n-1; ++i)
			for (int j=0; j<m-1; ++j)
				if (a[i][j]=='#' && a[i+1][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#')
				{
					a[i][j]='/';
					a[i+1][j]='\\';
					a[i][j+1]='\\';
					a[i+1][j+1]='/';
				}
		cout << "Case #" << tt << ":\n";
		bool tf=false;
		F(i,a)
			F(j,a[i])
				if (!tf && a[i][j]=='#')
				{
					cout << "Impossible\n";
					tf=true;
				}
		if (!tf)
			F(i,a) cout << a[i] << endl;
	}
	return 0;
}
