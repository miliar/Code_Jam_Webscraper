#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

inline int getLen(int val, int base)
{
	int x = 0;
	for (;val>0;x++,val/=base);
	return x;
}

inline int pow(int val, int base, int exp)
{
	int z = val;
	for (;exp>0;exp--, z*=base);
	return z;
}

int main()
{
	freopen("inp.txt", "r", stdin);	
	freopen("outp.txt", "w", stdout);
	int t;
	cin >> t;
	set< int > dim;
	for (int i=1;i<=t;i++)
	{	
		int a, b;
		cin >> a >> b;
		int ans = 0;
		for (int j=a;j<=b;j++)
		{			
			dim.clear();
			int len10 = getLen(j, 10);
			for (int h=1;h<len10;h++)
			{
				int tenpo = pow(1, 10, h);
				int rst = j % tenpo;
				if (getLen(rst, 10) == h)
				{
					int val = j/tenpo;
					val += rst*pow(1, 10, getLen(val, 10));
					if (val <= b && val > j && dim.find(val) == dim.end())
					{
						ans++;
						dim.insert(val);
					}
				}
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}