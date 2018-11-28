#define mset(a) memset(a,0,sizeof(a))

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
#include <ctime>

using namespace std;

vector<string> com,opp;
vector<char> ans;

int combine(char a,char b)
{
	for(int i=0;i<com.size();i++)
	{
		if(a==com[i][0]&&b==com[i][1]||a==com[i][1]&&b==com[i][0])
			return int(com[i][2]);
	}
	return 0;
}
bool opposed(char a,char b)
{
	for(int i=0;i<opp.size();i++)
	{
		if(a==opp[i][0]&&b==opp[i][1]||a==opp[i][1]&&b==opp[i][0])
			return true;
	}
	return false;
}
int main()
{
int t;
cin>>t;
for(int tt=1;tt<=t;tt++)
{
int c,d,n;
cin>>c;
com.clear();
opp.clear();
ans.clear();
string inv;
string temp;
for(int i=0;i<c;i++)
{
	cin>>temp;
	com.push_back(temp);
}
cin>>d;
while(d--)
{
	cin>>temp;
	opp.push_back(temp);
}
cin>>n;
cin>>inv;
for(int i=0;i<inv.size();i++)
{
	ans.push_back(inv[i]);
	int p=ans.size();
	if(p<=1)
		continue;
	int cc=combine(ans[p-2],ans[p-1]);
	if(cc)
	{
		ans.pop_back();
		ans.pop_back();
		ans.push_back(char(cc));
	}
	for(int i=0;i<ans.size()-1;i++)
	{
		if(opposed(ans[i],ans[ans.size()-1]))
		{
			ans.clear();
			break;
		}
	}
}
printf("Case #%d: [",tt);
if(ans.size()>0)
{
	for(int i=0;i<ans.size()-1;i++)
		printf("%c, ",ans[i]);
	printf("%c]\n",ans[ans.size()-1]);
}
else printf("]\n");
}

return 0;
}
