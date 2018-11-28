#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char comb[26][26];
bool oppose[26][26];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,n,i,j,k,c,d;
	string s;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		memset(comb,0,sizeof(comb));
		memset(oppose,0,sizeof(oppose));
		cin>>c;
		while(c--)
		{
			cin>>s;
			comb[s[0]-'A'][s[1]-'A']=s[2];
			comb[s[1]-'A'][s[0]-'A']=s[2];
		}
		cin>>d;
		while(d--)
		{
			cin>>s;
			oppose[s[0]-'A'][s[1]-'A']=true;
			oppose[s[1]-'A'][s[0]-'A']=true;
		}
		cin>>n;
		cin>>s;
		string ans="";
		for(i=0;i<n;i++)
		{
			ans+=s[i];
			// combine
			k=ans.length();
			if (k>=2) 
			{
				if (comb[ans[k-1]-'A'][ans[k-2]-'A'])
				{
					ans=ans.substr(0,k-2)+comb[ans[k-1]-'A'][ans[k-2]-'A'];
					continue;
				}
			}
			for(j=0;j<k-1;j++)
				if (oppose[ans[k-1]-'A'][ans[j]-'A']) break;
			if (j<k-1) ans="";
		}
		
		printf("Case #%d: ",t);
		printf("[");
		for(i=0;i<ans.length();i++)
		{
			printf("%c",ans[i]);
			if (i<ans.length()-1) printf(", ");
		}
		printf("]\n");
	}

	return 0;
}