#include <iostream>
#include <vector>
using namespace std;
typedef pair<int,int> pi;
int policz(string s)
{
	int k=0;
	k+=600*(s[0]-'0');
	k+=60*(s[1]-'0');
	k+=10*(s[3]-'0');
	k+=s[4]-'0';
	//cout<<s<<" : "<<k<<endl;
	return k;
}
int main()
{
	int w;
	cin>>w;
	for (int u=1; u<=w; u++)
	{
		int tim,n,m;
		cin>>tim>>n>>m;
		vector<pi> v[2];
		for (int i=0; i<n; i++)
		{
			string a,b;
			cin>>a>>b;
			v[0].push_back(pi(policz(a),1));
			v[1].push_back(pi(policz(b)+tim,-1));
		}
		for (int i=0; i<m; i++)
		{
			string a,b;
			cin>>a>>b;
			v[1].push_back(pi(policz(a),1));
			v[0].push_back(pi(policz(b)+tim,-1));
		}
		int t[2]={0};
		for (int i=0; i<2; i++)
		{
			sort(v[i].begin(),v[i].end());
			int k=0;
			for (int j=0; j<v[i].size(); j++)
			{
				//printf("%d %d\n",v[i][j].first,v[i][j].second);
				k+=v[i][j].second;
				t[i]=max(k,t[i]);
			}
		}
		printf("Case #%d: %d %d\n",u,t[0],t[1]);
	}
}
