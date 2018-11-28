#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

string comb[1000],del[1000],s;
int N,C,D;

int main()
{
	int T,test=1;
	for (cin >> T;test<=T;++test)
	{
		cin >> C;
		for (int i=0;i<C;++i)
			cin >> comb[i];
		cin >> D;
		for (int i=0;i<D;++i)
			cin >> del[i];
		cin >> N >> s;
		
		string ans="";
		for (int i=0;i<N;++i)
		{
			ans+=s[i];
			int n=ans.size();
			if (n>1)
			{
				for (int j=0;j<C;++j)
				if (comb[j][0]==ans[n-1] && comb[j][1]==ans[n-2]
				 || comb[j][0]==ans[n-2] && comb[j][1]==ans[n-1])
				{
					ans[n-2]=comb[j][2];
					ans.resize(n-1);
					break;
				}
			}
			n=ans.size();
			if (n>1)
			{
				for (int k=0;k+1<ans.size();++k)
					for (int j=0;j<D;++j)
					if (del[j][0]==ans[n-1] && del[j][1]==ans[k]
					 || del[j][0]==ans[k] && del[j][1]==ans[n-1])
					{
//						puts("!!");
						ans="";
						break;
					}
			}
		}
		
		printf("Case #%d: ",test);
		printf("[");
		for (int i=0;i<ans.size();++i)
		{
			if (i) printf(", ");
			printf("%c",ans[i]);
		}		
		printf("]\n");
	}
	return 0;
}
