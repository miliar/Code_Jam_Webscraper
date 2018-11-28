#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int d[20][256][256];

int ds[501][20];

string converse(int x)
{
	string ret = "";
	
	int t = 0;
	
	while (x != 0)
	{
		t++;
		ret += (char)(x % 10 + '0');
		x /= 10;
	}
	
	for (int i=t; i<4; i++)
	{
		ret += '0';
	}
	
	reverse(ret.begin(), ret.end());
	
	return ret;
}

int main ()
{
    ifstream cin("input.txt");
	ofstream cout("output.txt");
	
	d[0]['w']['e'] = 1;
	d[1]['e']['l'] = 1;
	d[2]['l']['c'] = 1;
	d[3]['c']['o'] = 1;
	d[4]['o']['m'] = 1;
	d[5]['m']['e'] = 1;
	d[6]['e'][' '] = 1;
	d[7][' ']['t'] = 1;
	d[8]['t']['o'] = 1;
	d[9]['o'][' '] = 1;
	d[10][' ']['c'] = 1;
	d[11]['c']['o'] = 1;
	d[12]['o']['d'] = 1;
	d[13]['d']['e'] = 1;
	d[14]['e'][' '] = 1;
	d[15][' ']['j'] = 1;
	d[16]['j']['a'] = 1;
	d[17]['a']['m'] = 1;
	d[18]['m']['!'] = 1;
	
	int n;
	
	cin >> n;	
	
	string s;
	
	getline(cin, s);
	
	for (int i=0; i<n; i++)
	{
		
		getline(cin, s);
		
		for (int j=0; j<s.length(); j++)
		{
			for (int k=0; k<19; k++)
			{
				ds[j][k] = 0;
			}
			
			if (s[j] == 'w')
			{
				ds[j][0] = 1;
			}
				
			for (int k=0; k<19; k++)
			{
				for (int p=0; p<j; p++)
				{
					if (d[ k ][ s[p] ][ s[j] ])
					{
						ds[ j ][ k + 1 ] = (ds[ j ][ k + 1 ] + ds[ p ][ k ]) % 10000;
					}
				}
			}
		}
		
		int ans = 0;
		
		for (int j=0; j<s.length(); j++)
		{
			ans = (ans + ds[j][18]) % 10000;
		}		
		
		cout << "Case #" << i + 1 << ": " << converse(ans) << endl;
		
		
	}
}