#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for (int t = 1;t<=T;t++)
	{
		cout<<"Case #"<<t	<<": ";
		int nVines;
		cin>>nVines;
		vector<pair<long long, long long> > vines(nVines);
		for (int i =0;i<nVines;i++)
			cin>>vines[i].first>>vines[i].second;
		//for (int i =0;i<nVines;i++)
		//	vines[i].first=-vines[i].first;
		sort(vines.begin(),vines.end());
		//for (int i =0;i<nVines;i++)
		//	vines[i].first=-vines[i].first;
		
		vector<long long> maxSwing(nVines);
		for (int i =0;i<nVines;i++)
			maxSwing[i] = 0;
		maxSwing[0] = vines[0].first;
		
		for (int i =0;i<nVines;i++)
		{
			for (int j = i+1;j<nVines;j++)
			{
				if (vines[j].first>vines[i].first+maxSwing[i]) break;
				maxSwing[j] = max(maxSwing[j], (min(vines[j].second,vines[j].first-vines[i].first)));
			}
		}
		int D;
		cin>>D;
		bool ok = false;
		for (int i = 0;i<nVines;i++)
			if (vines[i].first+maxSwing[i]>=D)
			{
				cout<<"YES";
				ok = true;
			}
		if (not ok)
			cout<<"NO";
		//for (int i = 0;i<nVines;i++)
		//	cout<<vines[i].first<<' ';
		
		cout<<endl;
	}
	return 0;
}