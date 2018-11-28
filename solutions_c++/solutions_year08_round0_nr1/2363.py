#include <iostream>
#include <map>
#include <string>
using namespace std; 

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int test=1; test<=t; ++test)
	{
		int n, q;
		cin >> n;
		map <string, int> engine;
		string s;
		getline(cin, s);

		for (int i=0; i<n; ++i)
		{			
			getline(cin, s);
			engine[s]=i;
		}
		cin >> q;
		getline(cin, s);				
		int f[200];
		int g=-1;
		for (int j=0; j<n; ++j)
			f[j]=1000000;
		for (int i=0; i<q; ++i)
		{			
			getline(cin, s);			
			int x=engine[s];
			int h=1000000;
			for (int j=0; j<n; ++j)
			{
				if (j==x)
					f[j]=1000000;
				else
					f[j]=min(f[j], g+1);
				h=min(h, f[j]);
			}
			g=h;
		}		
		if (g==-1) g=0;
		cout << "Case #" << test << ": " << g << endl;
	}
	return 0;
}