#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>

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
typedef vector<string> VS;

int main()
{
	int T;
	cin >> T;
	for (int caso = 1; caso <= T; caso++)
	{
		cout << "Case #" << caso << ":" << endl;
		int n;
		cin >> n;
		VI vic (n);
		VI jug (n);
		VD WP (n);
		VD OWP (n);
		VD OOWP (n);
		
		VS v(n);
		fi (n) cin >> v[i];
		
		fi (n)
		{
			fj (n)
			{
				if (v[i][j] == '1') vic[i]++;
				if (v[i][j] != '.') jug[i]++;
			}
		}
		
		fi (n)
			WP[i] = double (vic[i]) / double(jug[i]);
			
		fi (n)
		{
			fj (n)
				if (v[i][j]!='.')
					OWP[i] += double (vic[j]-(v[j][i]=='1'?1:0)) / double (jug[j]-(v[j][i]!='.'?1:0));
			OWP[i] /= jug[i];
		}
		
		fi(n)
		{
			fj(n)
				if (v[i][j]!='.')
					OOWP[i] += OWP[j];
			OOWP[i] /= jug[i];
		}
		cout.setf(ios::fixed);
		cout.precision(10);
		fi (n)
			cout << (WP[i]+2*OWP[i]+OOWP[i])/4. << endl;
	}
}
