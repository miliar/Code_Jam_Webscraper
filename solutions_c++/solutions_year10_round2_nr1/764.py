#include <stdio.h>
#include <string.h>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int T,N,M,len,ans;
char str[200];

map<string,int> mymap;

int main()
{
	int i,j,k;
	//freopen("A-large.in","r",stdin);
	//freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		mymap.clear();
		scanf("%d%d",&N,&M);
		while(N--)
		{
			scanf("%s",str);
			string t1 = string("");
			string t2;
			len = strlen(str);
			for(i = 1;i < len;i++)
			{
				t2.clear();
				for(;i < len && str[i] != '/';i++)
					t2.push_back(str[i]);
				t2.push_back('/');
				t1 += t2;
				if(mymap.find(t1) == mymap.end())
					mymap[t1] = true;
			}
		}
		ans = 0;
		while(M--)
		{
			scanf("%s",str);
			string t1 = string("");
			string t2;
			len = strlen(str);
			for(i = 1;i < len;i++)
			{
				t2.clear();
				for(;i < len && str[i] != '/';i++)
					t2.push_back(str[i]);
				t2.push_back('/');
				t1 += t2;
				if(mymap.find(t1) == mymap.end())
					mymap[t1] = true,ans++;
			}
		}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}


