#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;
typedef map<double,double> MID;
typedef pair<double,double> PD;
typedef vector<PD> VPD;

int main()
{
	int T;
	cin >> T;
	VL lp;
	VB esp (2000000, true);
	fii (2, esp.size())
	{
		if (esp[i])
		{
			lp.push_back(i);
			for (int j=2;j*i<esp.size(); j++)
			{
				esp[i*j]=0;
			}
		}
	}
	for (int caso = 1; caso<=T; caso++)
	{
		ll a;
		cin >> a;
		ll ans = 0;
		if (a>1) ans++;
		fi (lp.size())
		{
			ll p = lp[i];
			ll val = 1;
			int ii = 0;
			while (val*p <= a)
			{
				val*=p;
				ii++;
			}
			if (ii>0) ii--;
			ans+=ii;
		}
		cout << "Case #" << caso << ": " << ans << endl;
	}
}
