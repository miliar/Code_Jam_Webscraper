#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
using namespace std;
int main(void)
{
	int t,q;
	int c,d,n;
	char so[100];
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (q = 1; q <= t; q++)
	{
		map<string,string> m;
		map<char,vector<char> > del;
		string ss;
		scanf("%d",&c);
		for (int i = 0 ; i < c; i++)
		{
			scanf("%s",&so);
			ss = (string) so;
			string nn = ss.substr(0,2);
			m[nn] = ss[2];
			reverse(nn.begin(),nn.end());
			m[nn] = ss[2];

		}
		scanf("%d",&d);
		for (int i = 0; i < d; i++)
		{
			scanf("%s",&so);
			ss = (string) so;
			del[ss[0]].push_back(ss[1]);
			del[ss[1]].push_back(ss[0]);
		}
		scanf("%d",&n);
		vector<char> vc;
		multiset<char> sc;
		char pr = ' ',ch;
		scanf("%c",&ch);
		for (int i = 0 ; i < n; i++)
		{
			scanf("%c",&ch);
			
				string cheak ="";
				cheak+= pr;
				cheak+= ch;
				if (m[cheak] != "")
				{
					vc.pop_back();
					sc.erase(sc.find(pr));
					vc.push_back(m[cheak][0]);
					sc.insert(m[cheak][0]);
					pr = m[cheak][0];
				} else
				{
					bool ok = true;
					for (int j = 0 ; j < del[ch].size(); j++)
					{
						if (sc.find(del[ch][j]) != sc.end())
						{
							sc.clear();
							vc.clear();
							pr = ' ';
							ok = false;
							break;
						}
					}
					if (ok)
					{
						vc.push_back(ch);
						sc.insert(ch);
						pr = ch;
					}
				}

		}
		printf("Case #%d: [",q);
		if (vc.size() == 0)
			printf("]\n"); else
		{
			for (int i = 0 ; i < vc.size()-1;i++)
				printf("%c, ",vc[i]);
			printf("%c]\n",vc[vc.size()-1]);
		}
	}
	return 0;
}