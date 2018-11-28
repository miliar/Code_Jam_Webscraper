#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
string str;
int N,M;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		scanf("%d%d",&M,&N);
		map<string,bool>hash;
		for(int i=0;i<M;i++)
		{
			cin>>str;
			string tmp="/";
			for(int j=1;str[j];j++)
			{
				if(str[j]=='/')
				{
					hash[tmp]=true;
				}
				tmp+=str[j];
			}
			hash[tmp]=true;
		}
		int ans=0;
		for(int i=0;i<N;i++)
		{
			cin>>str;
			str+='/';
			string tmp="/";
			for(int j=1;str[j];j++)
			{
				if(str[j]=='/')
				{
					if(!hash[tmp])ans++;
					hash[tmp]=true;
				}
				tmp+=str[j];
			}
			
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}