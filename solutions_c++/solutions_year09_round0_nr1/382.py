#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

set<string>ret;
vector<string>lang;


// int cc(vector<char>jilu[],int L,string str,int count)
// {
// 	if(count==L)
// 	{
// 		if(ret.find(str)!=ret.end()) return 1;
// 		return 0;
// 	}
// 	int i=0;
// 	int ans=0;
// 	for(i=0;i<jilu[count].size();i++)
// 	{
// 		ans+=cc(jilu,L,str+jilu[count][i],count+1);
// 	}
// 	return ans;
// }


int main()
{
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);

	ret.clear();
	lang.clear();

	int L,D,N;

	scanf("%d %d %d",&L,&D,&N);

	int i=0;
	char tmp[1000];
	for(i=0;i<D;i++)
	{
		scanf("%s",tmp);
		lang.push_back(tmp);
	}

	
	for(i=0;i<N;i++)
	{
		set<char>jilu[20];
		scanf("%s",tmp);
		int n = strlen(tmp);
		int j=0;
		bool inb=false;
		int count=0;
		for(j=0,count=0;j<n;j++)
		{
			if(inb)
			{
				if(tmp[j]==')')
				{
					count++;
					inb=false;
				}else
				{
					jilu[count].insert(tmp[j]);
				}
			}else
			{
				if(tmp[j]=='(')
				{
					inb=true;
				}else
				{
					jilu[count].insert(tmp[j]);
					count++;
				}
			}
		}
		int ans=0;
		for(int k=0;k<D;k++)
		{
			int tt=0;
			for(tt=0;tt<L;tt++)
			{
				if(jilu[tt].find(lang[k][tt]) == jilu[tt].end())
					break;
			}
			if(tt==L)
				ans++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}

// 	for(i=0;i<D;i++)
// 	{
// 		string str = lang[i];
// 		printf("Case #%d: %d\n",i+1,ret[str]);
// 	}
}
