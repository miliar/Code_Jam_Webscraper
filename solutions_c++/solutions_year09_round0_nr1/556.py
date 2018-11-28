#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;

int l,d,n;

int main()
{
	cin>>l>>d>>n;
	vector<string> dict(d);
	for (int i=0;i<d;i++)
		cin>>dict[i];
	for (int caseI=1;caseI<=n;caseI++)
	{
		vector<set<char> > pattern(l);
		for (int i=0;i<l;i++)
		{
			char ch;
			cin>>ch;
			if (ch=='(')
			{
				for (cin>>ch;ch!=')';cin>>ch)
					pattern[i].insert(ch);
			}
			else pattern[i].insert(ch);
		}
		int ans=0;
		for (int i=0;i<d;i++)
		{
			bool flag=true;
			for (int j=0;j<l && flag;j++)
				if (!pattern[j].count(dict[i][j]))
					flag=false;
			if (flag) ans++;
		}
		cout<<"Case #"<<caseI<<": "<<ans<<endl;
	}
	return 0;
}

