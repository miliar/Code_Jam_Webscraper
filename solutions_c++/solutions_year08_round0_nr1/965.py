#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int w;
	cin>>w;
	for (int u=1; u<=w; u++)
	{
		int n,m;
		cin>>n;
		char c[201];
		cin.getline(c,103);
		vector<string> v;
		vector<int> t[201];
		for (int i=0; i<n; i++)
		{
			cin.getline(c,103);
			string s(c);
			//cout<<i<<" : "<<s<<endl;
			v.push_back(s);
		}
		cin>>m;
		cin.getline(c,103);
		for (int i=0; i<m; i++)
		{
			cin.getline(c,103);
			string s(c);
			//cout<<i<<" : "<<s<<endl;
			for (int j=0; j<n; j++)
				if (s==v[j])
				{
					t[j].push_back(i);
					break;
				}
		}
		for (int i=0; i<n; i++)
		{
			reverse(t[i].begin(),t[i].end());
			//for (int j=0; j<t[i].size(); j++)
				//printf("%d %d: %d\n",i,j,t[i][j]);
		}
		int k=0;
		int wynik=0;
		while (true)
		{
			//printf("%d\n",k);
			int p=k;
			for (int i=0; i<n; i++)
			{
				while (!t[i].empty()&&t[i].back()<k) t[i].pop_back();
				if (!t[i].empty()) p=max(p,t[i].back());
				else p=m;
				//printf("%d - %d\n",i,p);
			}
			k=p;
			if (k>=m) break;
			wynik++;
		}
		printf("Case #%d: %d\n",u,wynik);
	}
}
