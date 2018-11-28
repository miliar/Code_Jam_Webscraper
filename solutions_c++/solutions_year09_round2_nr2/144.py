#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

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
		string N;
		cin >> N;
		string res=N;
		if (not next_permutation(res.begin(),res.end()))
		{
			res=N;
			sort(res.begin(),res.end());
			res='0'+res;
			fi(res.size())
			{
				if (res[i]!='0')
				{
					res[0]=res[i];
					res[i]='0';
					break;
				}
			}
		}
		cout << "Case #" << caso << ": " << res << endl;
	}
}
