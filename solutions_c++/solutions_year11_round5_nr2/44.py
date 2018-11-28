#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>

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
typedef map<int,int> MII;

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		cout << "Case #" << caso << ": ";
		int n;
		cin >> n;
		VI v(n);
		fi (n) cin >> v[i];
		sort (v.begin(),v.end());
		int mn = 0;
		int mx = n;
		while (mx>mn)
		{
			int md = (mx+mn+1)/2;
			MII m;
			MII lb;
			fi (n) m[v[i]]++;
			bool ok = true;
			while (ok and not m.empty())
			{
				int a = m.begin()->first;
				if (m[a]==0)
				{
					m.erase(a);
					continue;
				}
				if (lb[a]>0)
				{
					lb[a]--;
					lb[a+1]++;
					m[a]--;
					continue;
				}
				fi (md)
				{
					if (m[a+i] == 0)
					{
						ok = false;
						break;
					}
					m[a+i]--;
				}
				lb[a+md]++;
			}
			if (ok)
				mn = md;
			else
				mx = md-1;
		}
		cout << mx << endl;
	}
}
