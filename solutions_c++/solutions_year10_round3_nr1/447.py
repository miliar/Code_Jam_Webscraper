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
		int N;
		cin >> N;
		VI A(N);
		VI B(N);
		fi (N)
			cin >> A[i] >> B[i];
		int rp = 0;
		fi (N)
		{
			fj (i)
			{
				if ((A[i]-A[j])*(B[i]-B[j])<0)
					rp++;
			}
		}
		cout << "Case #" << caso << ": " << rp << endl;
	}
}
