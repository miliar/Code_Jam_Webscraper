#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.00000001
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
typedef vector<string> VS;

int main()
{
	int T;
	cin >> T;
	for (int caso = 1; caso <= T; caso++)
	{
		cout << "Case #" << caso << ": ";
		double mn = 0;
		double mx = 1e13;
		int c;
		double d;
		cin >> c >> d;
		VI qt (c);
		VD pos (c);
		fi (c) cin >> pos[i] >> qt[i];
		
		int sum = 0;
		fi (c) sum+=qt[i];
		
		VD lv (sum);
		int ii = 0;
		fi (c) fj (qt[i]) lv[ii++] = pos[i];
		
		sort (lv.begin(),lv.end());
		int n = lv.size();
		
		
		while (fabs(mx-mn)/((mx+mn)/2.) > eps)
		{
			double md = (mx+mn)/2;
			double ini = lv[0] - md;
			bool ok = true;
			for (int i=1;i<n and ok;i++)
			{
				if (lv[i] + md < ini + d) ok = false;
				else 
				{
					if (lv[i] - md < ini + d) ini += d;
					else ini = lv[i] - md;
				}
			}
			if (ok)
				mx = md;
			else
				mn = md;
		}
		
		cout.setf(ios::fixed);
		cout.precision(10);
		cout << (mn+mx)/2. << endl;
	}
}
