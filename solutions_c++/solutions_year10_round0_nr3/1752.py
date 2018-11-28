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

VL gr,sig,ben;
int R,K,n;

ll cb (int a, int r)
{
	if (r==0)
		return 0;
	VI tt (n,-1);
	VL bt (n,-1);
	int act = a;
	ll sm = 0;
	int ttr = 0;
	while (r > 0)
	{
		if (tt[act]>-1) //repetido
		{
			ll tiempo = ttr - tt[act];
			ll beneficio = sm - bt[act];
			return sm + (r/tiempo)*beneficio + cb (act,r%tiempo);
		}
		//no esta repetido
		tt[act]=ttr;
		bt[act]=sm;
		ttr++;
		r--;
		sm+=ben[act];
		act=sig[act];
	}
	return sm;
}

int main()
{
	int T;
	cin >> T;
	
	for (int caso=1;caso<=T;caso++)
	{
		cin >> R >> K >> n;
		gr = VL (n);
		fi (n)
			cin >> gr[i];
		sig=ben=VL (n);
		fi (n)
		{
			//calculamos siguiente y beneficio empezando por i
			ll suma = 0;
			int ii = i;
			if (gr[i]<=K)
			{
				suma+=gr[i];
				ii++;
				ii%=n;
				while (ii!=i and suma+gr[ii] <= K)
				{
					suma+=gr[ii++];
					ii%=n;
				}
			}
			ben[i]=suma;
			sig[i]=ii;
		}
		
		
		
		cout << "Case #" << caso << ": " << cb(0,R) << endl;
	}
}
