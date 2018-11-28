#include <iostream>
#include <vector>
#include <string>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		int N;
		cin >> N;
		VI ult (N);
		fi (N)
		{
			string s;
			cin >> s;
			int u=-1;
			fj (N)
			{
				if (s[j]=='1')
					u=j;
			}
			ult[i]=u;
		}
		int res=0;
		fi (N)
		{
			int enc;
			for (int j=i;j<N;j++)
			{
				if (ult[j]<=i)
				{
					enc=j;
					break;
				}
			}
			while (enc!=i)
			{
				res++;
				int aux=ult[enc];
				ult[enc]=ult[enc-1];
				ult[enc-1]=aux;
				enc--;
			}
		}
		cout << "Case #" << caso << ": " << res << endl;
	}
}
