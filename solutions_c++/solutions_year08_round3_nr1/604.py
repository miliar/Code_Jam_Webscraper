#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main(void)
{
	int t;
	int i,j;
	int p,k,l;
	int alpha,tmp;

	vector<int> f;

	cin >> t;
	for (int cas=1; cas<=t; cas++)
	{
		cin >> p >> k >> l;
		alpha=p*k;
		for (i=0; i<l; i++)
		{
			cin >> tmp;
			f.push_back(tmp);
		}
		sort(f.begin(),f.end());
		reverse(f.begin(),f.end());

		int xp=1,xk=1;
		int tot=0;
		bool poss=true;
		for (i=0; i<f.size(); i++)
		{
			if (f[i]==0)
				break;
			tot+=xp*f[i];
			if (xk%k==0)
			{
				xk=1;
				xp++;
				if (xp>p)
				{
					break;
					poss=false;
				}
			}
			else
				xk++;
		}
		cout << "Case #" << cas << ": ";
		if (poss==false)
			cout << "Impossible";
		else
			cout << tot;
		cout << endl;

		f.clear();
	}

	return 0;
}