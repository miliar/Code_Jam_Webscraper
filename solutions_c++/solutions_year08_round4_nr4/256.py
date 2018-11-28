#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#define pb push_back
#define fi first
#define se second
#define INF 1000000000
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
		
int main()
{
	int tests;
	scanf("%d",&tests);
	for (int u=1; u<=tests; u++)
	{
		int k;
		scanf("%d",&k);
		string s;
		cin>>s;
		vector<int> v;
		for (int i=0; i<k; i++)
			v.pb(i);
		int w=INF;
		string pp(s.size(),' ');
		while (true)
		{
			for (int i=0; i<s.size(); i++)
				pp[i]=s[k*(i/k)+v[i%k]];
			//cout<<pp<<"  "<<w<<endl;
			char c=' ';
			int p=0;
			for (int i=0; i<s.size(); i++)
				if (pp[i]!=c)
			{
				c=pp[i];
				p++;
			}
			w=min(w,p);
			if (!next_permutation(v.begin(),v.end())) break;
			
		}
		printf("Case #%d: %d\n",u,w);
	}
}
