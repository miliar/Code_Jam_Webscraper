#include <iostream>
#include <vector>
#include <algorithm>
#define PB push_back
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
using namespace std;

long long solve()
{
	return 0;
}

int main()
{
	long long n,k,x,y,a,b,c,d,m;
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	cin >> k;
	for (int cn=0;cn<k;cn++)
	{
		int cc=0;
		vector <long long> cx;
		vector <long long> cy;
		cin >> n >> a >> b >> c >> d >> x >> y >> m; cx.PB(x); cy.PB(y);
		for (int i=1;i<n;i++)
		{
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			cx.PB(x); cy.PB(y);
		}
		for (int i=0;i<n;i++)
			for (int j=i+1;j<n;j++)
				for (int q=j+1;q<n;q++)
					if ((cx[i]+cx[j]+cx[q])%3 == 0 && (cy[i]+cy[j]+cy[q])%3==0) cc++;
		cout << "Case #" << cn+1 << ": " << cc << endl;
	}
	return 0;		
}
