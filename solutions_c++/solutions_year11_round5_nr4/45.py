#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>
#include <stack>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28
#define mod 1000003

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
typedef vector<string> VS;
typedef stack<int> SI;

int main()
{
	int T;
	cin >> T;
	for (int caso = 1; caso <= T; caso++)
	{
		cout << "Case #" << caso << ": ";
		string s;
		cin >> s;
		int nin = 0;
		fi (s.size())
			if (s[i] == '?') nin++;
		fi (1<<nin)
		{
			VI v (nin);
			int ii = i;
			fj (nin)
			{
				v[j] = ii%2;
				ii/=2;
			}
			ll num = 0;
			int jj = 0;
			fj (s.size())
			{
				num*=2;
				if (s[j] == '?')
				{
					num+=v[jj++];
				}
				else
				{
					num+=s[j]-'0';
				}
			}
			
			//cout << i << " " << num << endl;
			ll mn = 1;
			ll mx = (1LL<<30)+10;
			while (mn<mx)
			{
				ll md = (mx+mn)/2;
				//cout << mn << " " << md << " " << mx << endl;
				if (md * md < num)
					mn = md+1;
				else
					mx = md;
			}
			if (mx * mx  == num)
			{
				jj = 0;
				fj (s.size())
				{
					if (s[j] == '?')
						cout << v[jj++];
					else
						cout << s[j];
				}
				cout << endl;
				break;
			}
		}
	}
}
