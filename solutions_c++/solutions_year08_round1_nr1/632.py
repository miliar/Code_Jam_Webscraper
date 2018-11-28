#include <iostream>
#include <vector>
#include <list>
#include <iterator>
#include <algorithm>
using namespace std;

int main()
{
	int ncase;
	cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << icase+1 << ": ";
		
		int nv; cin >> nv;
		vector<int> vx(nv), vy(nv);
		
		for(int i=0; i < nv; i++)
			cin >> vx[i];
		for(int i=0; i < nv; i++)
			cin >> vy[i];
		sort(vx.begin(), vx.end());
		sort(vy.begin(), vy.end());
		
		long long ret = 0;
		for(int i=0; i < nv; i++)
		{
			ret += vx[i] * vy[nv-i-1];
		}

		cout << ret;	
		cout << "\n";
	}
}
