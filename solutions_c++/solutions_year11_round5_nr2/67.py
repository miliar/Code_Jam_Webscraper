#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>

#define ll long long

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int TT=1;TT<=T;++TT)
	{
		printf("Case #%d: ",TT);
		int n,nums[1002]={0},kol[10002]={0};
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&nums[i]);
			kol[nums[i]]++;
		}
		vector <int> l;
		int mn=100000;
		for(int i=1;i<=10000;i++)
		{
			if (kol[i]>0)
			{
				sort(l.begin(),l.end());
				for(int j=0;j<kol[i];j++)
				{
					if (j<l.size()) l[j]++;
					else l.push_back(1);
				}
				for(int j=l.size()-1;j>=kol[i];j--)
				{
					mn=min(mn,l[j]);
					l.pop_back();
				}
			}
			else
			{
				for(int j=0;j<l.size();j++)
					mn=min(mn,l[j]);
				l.clear();
			}
		}
		for(int i=0;i<l.size();i++)
			mn=min(mn,l[i]);
		if (mn==100000) mn=0;
		printf("%d\n",mn);
	}
	return 0;
}
