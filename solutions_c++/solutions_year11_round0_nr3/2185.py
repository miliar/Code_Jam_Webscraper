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
#ifndef ONLINE_JUDGE 
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);
#endif
	int t;
	cin >> t;
	for (int iii=1; iii<=t; ++iii)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		F(i,a) cin >> a[i];
		sort(ALL(a));
		int s=a[0];
		for (int i=1; i<n; ++i)
			s^=a[i];
		cout << "Case #" << iii << ": ";
		if (s==0)
		{
			s=0;
			for (int j=1; j<n; ++j)
				s+=a[j];
			cout << s << endl;
		}else
			cout << "NO\n"; 
	}
	return 0;
}
