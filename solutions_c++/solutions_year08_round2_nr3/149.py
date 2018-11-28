#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		int K;
		cin >> K;
		int n;
		cin >> n;
		vector <int> v(n);
		for (int i=0;i<n;i++)
		{
			cin >> v[i];
		}
		vector <int> B (K,-1);
		int pant=K-1;
		for (int i=1;i<=K;i++)
		{
			int pos=(i-1)%(K-i+1);
			while (pos>0)
			{
				pant++;
				if (pant==K)
					pant=0;
				if (B[pant]==-1)
					pos--;
			}
			pant++;
			if (pant==K)
				pant=0;
			while (B[pant]!=-1)
			{
				pant++;
				if (pant==K)
					pant=0;
			}
			B[pant]=i;
		}
		cout << "Case #" << caso << ":";
		for (int i=0;i<n;i++)
		{
			cout << " " << B[v[i]-1];
		}
		cout << endl;
	}
}
