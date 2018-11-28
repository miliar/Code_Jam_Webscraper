//In the name of Allah
//
//
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
const int MN=1000*1000+100;
#define int long long
int list[MN];
int list2[MN];
int T,l,t,n,c;
int best;
vector <int> slist;
bool cmp(const int & a,const int & b)
{
	return a>b;
}
main()
{
	cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		best=0;
		slist.clear();
		cin>>l>>t>>n>>c;
		for (int i=0;i<c;i++)
			cin>>list2[i];
		int ct=0;
		for (int i=0;i<n;i++)
			list[i]=list2[ct],ct=(ct+1)%c;
		for (int i=0;i<n;i++)
			best+=list[i]*2;
		int cu=0;
		bool av=false;
		for (int i=0;i<n;i++)
		{
			if (av)
				slist.push_back(list[i]);
			else
			{
				if (cu+2*list[i]<t)
				{
					cu+=2*list[i];
					continue;
				}
				av=true;
				slist.push_back(list[i]-(t-cu)/2);
			}
		}
		sort(slist.begin(),slist.end(),cmp);
		for (int i=0;i<min(l,(int)(slist.size()));i++)
			best-=slist[i];

		cout<<"Case #"<<ca<<": "<<best<<endl;
	}
	return 0;
}
