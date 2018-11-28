#pragma warning(disable : 4996)
#include <iomanip>
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

vector< string > a;
vector<double> wp,owp,oowp;

void fwp()
{
	F(i,a)
	{
		int w=0, c=0;
		F(j,a[i])
			if (a[i][j]!='.')
			{
				++c;
				if (a[i][j]=='1')
					++w;
			}
		wp[i]=double(w)/c;
	}
}

void fowp()
{
	vector<double> wpcopy=wp;
	F(i,a)
	{
		double w=0; int c=0;
		F(j,a)
			if (a[i][j]!='.')
			{
				char ch=a[j][i];
				a[j][i]='.';
				fwp();
				a[j][i]=ch;
				w+=wp[j];
				++c;
			}
		owp[i]=w/c;
	}
	wp=wpcopy;
}

void foowp()
{
	F(i,a)
	{
		double w=0; int c=0;
		F(j,a[i])
			if (a[i][j]!='.')
			{
				w+=owp[j];
				++c;
			}
		oowp[i]=w/c;
	}
}

int main()
{
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);
	cout << fixed << setprecision(7);
	int tt;
	cin >> tt;
	for (int t=1; t<=tt; ++t)
	{
		int n;
		cin >> n;
		a.resize(n); wp.resize(n,0); owp.resize(n,0); oowp.resize(n,0);
		F(i,a) cin >> a[i];
		fwp();
		fowp();
		foowp();
		vector<double> ans(n);
		F(i,ans)
			ans[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		cout << "Case #" << t << ":\n";
		F(i,ans) cout << ans[i] << endl;
	}
	return 0;
}
