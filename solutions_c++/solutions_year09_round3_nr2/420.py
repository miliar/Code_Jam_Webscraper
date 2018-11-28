#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <utility>
#include <sstream>
#include <cstring>
#include <iomanip>


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RP(i,s,e) for(int i=s;i<e;i++) 
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin();i!=(x).end();++i)
#define M make_pair
#define pB push_back
#define _1 first
#define _2 second
#define foreach(t,i) RI(i,t)
#define CLEAR(x,v) memset((x),(v),sizeof((x))
#define PRINT(o,b) RI(i,b) o << *i << (--b.end()==i ? "" : " ");
#define PE(s,e) cout << #s << " : "; for(typeof(s) i=s; i!=e; ++i) cout << (*i) << " "; cout << endl;

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<" "; return o;}

//Cake please.

int main()
{
	int cst;
	cin >> cst;
	
	RP(css, 1, cst+1)
	{
		int n;
		cin >> n;
		
		int x[n];
		int y[n];
		int z[n];
		
		int vx[n];
		int vy[n];
		int vz[n];
		
		//cout << n << endl;
		RP(i, 0, n)
		{
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
			//cout << i << " " << x[i] << " " << y[i] << " " << z[i] << "; " << vx[i] << " " << vy[i] << " " << vz[i] << endl;
		}
		

//long double ccx = 0.0;
//long double ccy = 0.0;
//long double ccz = 0.0;
//
//RP(i, 0, n)
//{
//	ccx += x[i];
//	ccy += y[i];
//	ccz += z[i];
//}
//
//ccx /= n;
//ccy /= n;
//ccz /= n;
//
//long double nd = sqrt(ccx * ccx + ccy * ccy + ccz * ccz);
//cout << "=======   " << nd << endl;




		long double me = 1 << 30;
		long double mi = 0;
		
		long double cm;
		long double ci;
		
		long double cx = 0.0;
		long double cy = 0.0;
		long double cz = 0.0;
		{
			cx = cy = cz = 0.0;
			RP(i, 0, n)
			{
				cx += x[i];
				cy += y[i];
				cz += z[i];
			}
			
			cx /= n;
			cy /= n;
			cz /= n;
		}
		ci = cx * cx + cy * cy + cz * cz;
		
		{
			cx = cy = cz = 0.0;
			RP(i, 0, n)
			{
				cx += x[i] * me;
				cy += y[i] * me;
				cz += z[i] * me;
			}
			
			cx /= n;
			cy /= n;
			cz /= n;
		}
		cm = cx * cx + cy * cy + cz * cz;
		
		long double td = me / 4;
	
		while (me - mi > 0.000000001)
		{	
			long double l2 = (me * 2 + mi) / 3;
			long double l1 = (me + 2 * mi) / 3;
			
			long double cx = 0.0;
			long double cy = 0.0;
			long double cz = 0.0;
			
			RP(i, 0, n)
			{
				cx += x[i] + vx[i] * l1;
				cy += y[i] + vy[i] * l1;
				cz += z[i] + vz[i] * l1;
			}
			
			cx /= n;
			cy /= n;
			cz /= n;
			
			long double nd1 = cx * cx + cy * cy + cz * cz;
			
			
			cx = cy = cz = 0.0;
			
			RP(i, 0, n)
			{
				cx += x[i] + vx[i] * l2;
				cy += y[i] + vy[i] * l2;
				cz += z[i] + vz[i] * l2;
			}
			
			cx /= n;
			cy /= n;
			cz /= n;
			
			long double nd2 = cx * cx + cy * cy + cz * cz;
			

			
			
			//cout << ci << ", " << mi << " (" << l1 << ", " << l2 << ") " << me <<  ";; " << td << " " << nd1 << "   " << nd2  << " = " << (nd1 - nd2) << endl;
			
			if ((nd1 - nd2) > -0.00000000001)
			{
				mi = l1;
				ci = nd1;
			}
			else
			{
				me = l2;
				cm = nd2;
			}
			
			td /= 2;
		}

//		for (long double k = 0; k < 5; k += 0.01)
//		{
//			long double cx = 0.0;
//			long double cy = 0.0;
//			long double cz = 0.0;
//			
//			RP(i, 0, n)
//			{
//				cx += x[i] + vx[i] * k;
//				cy += y[i] + vy[i] * k;
//				cz += z[i] + vz[i] * k;
//			}
//			
//			cx /= n;
//			cy /= n;
//			cz /= n;
//			
//			long double nd = sqrt(cx * cx + cy * cy + cz * cz);
//			
//			cout << nd << endl;
//		}
//		cout << "=========================" << endl << endl;
		
		cout << "Case #" << css << ": " << setprecision(8) << fixed << sqrt(ci) << " " << (mi < 500 ? mi : 0) << endl;
		
		cout.unsetf(ios_base::floatfield);
	}
	
	return 0;
}