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
	for (int caso=1;caso<=T;caso++)
	{
		int R, C, D;
		cin >> R >> C >> D;
		VVI v (R, VI (C,D));
		fi (R)
		{
			string s;
			cin >> s;
			fj (C)
			{
				v[i][j]+=s[j]-'0';
			}
		}
		int mx = 0;
		fkk (3, 11)
		{
			fi (R-k+1)
			{
				fj (C-k+1)
				{
					int cx, cy;
					cx = cy = 0;
					for (int ii=0;ii<k;ii++)
					{
						for (int jj=0;jj<k;jj++)
						{
							if (((ii == 0) or (ii == k-1)) and ((jj == 0) or (jj == k-1))) continue; 
							if (k%2==0)
							{
								cx+=(k-1-2*ii)*v[i+ii][j+jj];
								cy+=(k-1-2*jj)*v[i+ii][j+jj];
							}
							else
							{
								cx+=(k/2-ii)*v[i+ii][j+jj];
								cy+=(k/2-jj)*v[i+ii][j+jj];
							}
						}
					}
					if (cx == 0 and cy == 0)
					{
						mx = max (mx, k);
						//cout << i << " " << j << " " << k << endl;
					}
				}
			}
		}
		cout << "Case #" << caso << ": ";
		if (mx >= 3)
			cout << mx << endl;
		else
			cout << "IMPOSSIBLE" << endl;
		
	}
}
