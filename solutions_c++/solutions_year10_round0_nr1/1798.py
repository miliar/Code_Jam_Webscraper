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
	/*int mask [32][32];
	for (int i=0;i<32;i++)
		mask[0][i]=1;
	for (int i=1;i<32;i++)
	{
		mask[i][0]=0;
		for (int j=1;j<32;j++)
		{
			mask[i][j]=(mask[i][j-1]+mask[i-1][j-1])%2;
			cout << mask[i][j] << " ";
		}
		cout << endl;
	}*/
	string res[2];
	res[0]="OFF";
	res[1]="ON";
	int T;
	cin >> T;
	
	for (int caso=1;caso<=T;caso++)
	{
		int N,K;
		cin >> N >> K;
		K++;
		int rp = 0;
		if (K%(1<<N)==0)
			rp=1;
		cout << "Case #" << caso << ": " << res[rp] << endl;
	}
}
