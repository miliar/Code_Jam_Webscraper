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

int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-output.txt","w",stdout);
	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-output.txt","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large-output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++)
	{
		set<string>dict;
		dict.insert("");
		int M,N;
		scanf("%d %d",&N,&M);
		int i=0;
		for(i=0;i<N;i++)
		{
			string str;
			cin>>str;
			while(str.length())
			{
				dict.insert(str);
				str = str.substr(0,str.rfind('/'));
			}
		}
		int ret = 0;
		for(i=0;i<M;i++)
		{
			string str;
			cin>>str;
			while(dict.find(str)==dict.end())
			{
				ret++;
				dict.insert(str);
				str = str.substr(0,str.rfind('/'));
			}
		}
		printf("Case #%d: %d\n",Case,ret);
	}
}