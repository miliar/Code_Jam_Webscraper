#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MAXQ = 1000;
const int MAXS = 100;
int d[MAXQ][MAXS];

int main()
{
	int n; // Test Case count
	int s; // Search Engine count
	int q; // Query count
	cin >> n;
	string str;
	for (int tc = 0; tc < n; tc++)
	{
		vector<string> eng;
		vector<string> query;
		memset(d, 0, MAXQ*MAXS*sizeof(int));
		cin >> s;
		getline(cin,str);
		for (int i = 0; i < s; i++)
		{
			getline(cin,str);
			eng.push_back(str);
		}
		cin >> q;
		getline(cin,str);
		for (int i = 0; i < q; i++)
		{
			getline(cin,str);
			query.push_back(str);
		}
		for (int i=0; i<q; i++)
		{
			for (int j=0; j<s; j++)
			{
				if (i==0) 
					if (query[i] != eng[j])
						d[i][j] = 0;
					else
						d[i][j] = 1000000;
				else 
				{
					d[i][j] = 1000000;
					if (query[i] != eng[j])
					for (int k=0; k<s; k++)
					{
						if (j != k)
							d[i][j] = min(d[i][j], d[i-1][k]+1);
						else
							d[i][j] = min(d[i][j], d[i-1][k]);
					}
				}
			}
		}
		int j = 1000000;
		for (int i=0; i<s; i++)
			j = min(j, d[q-1][i]);
		if (q==0) j = 0;
		cout << "Case #" << tc+1 << ": " << j << endl;
	}
	return 0;
}




