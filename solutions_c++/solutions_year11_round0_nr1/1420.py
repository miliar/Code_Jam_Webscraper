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


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,n,i,j,k;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n;
		string s;
		vector<int>push[2];
		vector<int>num;
		for(i=0;i<n;i++)
		{
			cin>>s>>j;
			if (s[0]=='O')
			{
				push[0].push_back(j);
				num.push_back(0);
			}
			else 
			{
				push[1].push_back(j);
				num.push_back(1);
			}
		}
		int ans=0,x[2]={1,1},ind[2]={0,0};
		for(i=0;i<n;i++)
		{
			for(j=0;;j++)
			{
				bool finish=false;
				if (x[num[i]]==push[num[i]][ind[num[i]]]) finish=true;
				for(k=0;k<2;k++)
					if (push[k].size()>ind[k])
					{
						if (x[k]<push[k][ind[k]]) ++x[k];
						if (x[k]>push[k][ind[k]]) --x[k];
					}
				if (finish) break;
			}
			ind[num[i]]++;
			ans+=j+1;
		}
		printf("Case #%d: %d\n",t,ans);
	}

	return 0;
}