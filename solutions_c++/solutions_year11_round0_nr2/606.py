#define fr(i, a, x) for(int(i) = a; i <= x; ++i)
#define rfr(i, a, x) for(int(i) = a; i >= x; --i)

#include <fstream>
#include <vector>
#include <string>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{
	int t, c, d, n;
	cin >> t;
	fr(re, 1, t)
	{
		cin >> c;
		vector<string> cs(2 * c);
		string ns, k;
		c *= 2;
		for(int i = 0; i < c; i += 2)
		{
			cin >> cs[i];
			cs[i + 1] += cs[i][1];
			cs[i + 1] += cs[i][0];
			cs[i + 1] += cs[i][2];
		}
		cin >> d;
		vector<string> ds(2 * d);
		d *= 2;
		for(int i = 0; i < d; i += 2)
		{
			cin >> ds[i];
			ds[i + 1] += ds[i][1];
			ds[i + 1] += ds[i][0];
		}	
		cin >> n;
		cin >> ns;
		fr(i, 0, n - 1)
		{
			k += ns[i];
			int u = k.size();
			if (u > 1) 
			{
				string sh;
				sh += k[u - 1];
				sh += k[u - 2];
				for(int j = 0; j < c; ++j)
					if (sh[0] == cs[j][0] && sh[1] == cs[j][1]) 
					{
						k.erase(k.end() - 2, k.end());
						k += cs[j][2];
						break;
					}
			}
			u = k.size();
			for(int j = 0; j < u && u > 1; ++j)
			{
				string sh;
				sh += k[j];
				sh += k[u - 1];
				bool tew = false;
				for(int l = 0; l < d; ++l)
					if (sh == ds[l])
					{
						k.erase(k.begin(), k.end());
						tew = true;
						break;
					}
				if (tew) break;
			}
			bool rfsd = false;
		}
		cout << "Case #" << re << ": [";
		for(int i = 0; i < k.size() - 1 && !k.empty(); ++i)
			cout << k[i] << ", ";
		if (!k.empty()) cout << k[k.size() - 1] << "]\n";
		else cout << "]\n";
	}
	return 0;
}