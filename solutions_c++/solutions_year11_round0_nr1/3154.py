#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef pair<int,int> pii;

int main()
{
	int t,k,tmp;
	string a;
	cin >> t;

	for (int test=1;test<=t;test++)
	{
		cin >> k;
		vector<pii> o;
		vector<pii> b;
		//vector<pii> all;

		for (int i=0;i<k;i++)
		{
			cin >> a >> tmp;
			int curr = (a=="O" ? 0 : 1);
			//all.push_back(make_pair(curr ,tmp));
			if (curr==0) o.push_back(make_pair(tmp,i));
			else b.push_back(make_pair(tmp,i));
		}

		int pos=0;
		int ans=0;
		int previous = 0, posb=1, poso=1;
		int compb=0,compo=0;
		while(compb<b.size() || compo<o.size())
		{
			if (compo==o.size() || (compb<b.size() && b[compb].second<o[compo].second))
			{
				int steps=abs(b[compb].first-posb);
				ans+=abs(b[compb].first-posb);
				posb=b[compb].first;

				if (compo<o.size())
				{
					if (poso<o[compo].first) poso+=min(1+steps,abs(poso-o[compo].first));
					else poso-=min(1+steps,abs(poso-o[compo].first));
				}
				compb++;
				ans++;
			}
			else
			{
				int steps=abs(o[compo].first-poso);
				ans+=abs(o[compo].first-poso);
				poso=o[compo].first;

				if (compb<b.size())
				{
					if (posb<b[compb].first) posb+=min(1+steps,abs(posb-b[compb].first));
					else posb-=min(1+steps,abs(posb-b[compb].first));
				}
				compo++;
				ans++;
			}
		}

		cout << "Case #" << test << ": " << ans << endl;
	}
	//system("pause");
	return 0;
}