#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;
int main()
{
	int t;

	cin >> t;
	for(int te = 1 ; te<=t ; te++)
	{
		int n, s, po = 1, pb = 1, no = 0, nb = 0, tot = 0;
		char ch;
		cin >> n;
		for(int i=0 ; i<n ; i++)
		{
			cin >> ch >> s;
			int tt = 0;
			if(ch == 'O')
			{
				tt = max(abs(s - po) - nb, 0);
				tt++;
				nb = 0;
				po = s;
				no+=tt;
			}
			else if(ch == 'B')
			{
				tt = max(abs(s - pb) - no, 0);
				tt++;
				no = 0;
				pb = s;
				nb+=tt;
			}
			tot += tt;
		}
		cout << "Case  #" << te << ": " << tot << endl;
	}
}
