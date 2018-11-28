#include <string>
#include <iostream> 
#include <fstream>
#include <math.h>
#include <vector>
#include <time.h>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
const double eps = 1e-8;
#define M_PI       3.14159265358979323846

#ifdef _MSC_VER
#else
typedef long long __int64;
#endif

#define MODULO 100003

__int64 c[600][600];
__int64 a[600][600];

void prec()
{
	for (int i=0;i<600;i++)
		c[i][0] = 1;

	for (int i=1;i<600;i++)
		for (int j=1;j<600;j++)
			c[i][j] = (c[i-1][j] + c[i-1][j-1]) % MODULO;

	for (int n=2;n<600;n++)
		a[n][1] = 1;
	
	for (int n=3;n<600;n++)
		for (int k=2;n-k-1>=0;k++)
		{
			for (int i=0;k-i-1>=0;i++)
			{
				a[n][k] += a[k][k-i-1]*c[n-k-1][i];
				a[n][k] %= MODULO;
			}
		}


}


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	prec();

	int tn;
	cin>>tn;
	for (int aaa=1;aaa<=tn;aaa++)
	{
		int n;
		cin>>n;

		__int64 ans = 0;
		for (int i=0;i<=n;i++)
		{
			ans += a[n][i];
			ans %= MODULO;
		}
		cout<<"Case #"<<aaa<<": "<<ans;
		cout<<endl;
	}




	return 0;
}