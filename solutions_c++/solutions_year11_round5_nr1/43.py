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

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		cout << "Case #" << caso << ":" << endl;
		int W, L, U, G;
		cin >> W >> L >> U >> G;
		VD llx,lly;
		llx=lly=VD(L);
		VD lux, luy;
		lux=luy=VD(U);
		fi (L)
			cin >> llx[i] >> lly[i];
		fi (U)
			cin >> lux[i] >> luy[i];
			
		//area total
		double at = 0;
		fi (U-1)
			at+= (lux[i+1]-lux[i])*(luy[i+1]+luy[i])/2.;
		fi (L-1)
			at-= (llx[i+1]-llx[i])*(lly[i+1]+lly[i])/2.;
		fii (1,G)
		{
			double obj = double(i)*at/double(G);
			double mn = 0;
			double mx = W;
			while (fabs(mx-mn) > eps)
			{
				double md = (mx+mn)/2;
				double an = 0;
				
				fi (U-1)
				{
					if (lux[i+1] > md)
					{
						double dx = md - lux[i];
						double dy = (luy[i+1]-luy[i])*dx/(lux[i+1]-lux[i]);
						an+=dx*(luy[i]+luy[i]+dy)/2.;
						break;
					}
					an += (lux[i+1]-lux[i])*(luy[i+1]+luy[i])/2.;
				}
				fi (L-1)
				{
					if (llx[i+1] > md)
					{
						double dx = md - llx[i];
						double dy = (lly[i+1]-lly[i])*dx/(llx[i+1]-llx[i]);
						an-=dx*(lly[i]+lly[i]+dy)/2.;
						break;
					}
					an -= (llx[i+1]-llx[i])*(lly[i+1]+lly[i])/2.;
				}
				
				if (an > obj)
					mx = md;
				else
					mn = md;
			}
			cout.setf(ios::fixed);
			cout.precision(10);
			cout << (mx+mn)/2. << endl;
		}
	}
}
