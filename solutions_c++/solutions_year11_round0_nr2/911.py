#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int T,a,b,n;
char ar[50][50],br[50][50];
char buf[1000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		memset(ar,-1,sizeof(ar));
		memset(br,0,sizeof(br));
		scanf("%d",&a);
		for (int i=0;i<a;i++)
		{
			scanf("%s",buf);
			int ta,tb;
			ta = buf[0]-'A';
			tb = buf[1]-'A';
			ar[ta][tb] = ar[tb][ta] = buf[2]-'A';
		}
		scanf("%d",&b);
		for (int i=0;i<b;i++)
		{
			scanf("%s",buf);
			int ta,tb;
			ta = buf[0]-'A';
			tb = buf[1]-'A';
			br[ta][tb] = br[tb][ta] = 1;
		}
		scanf("%d",&n);
		scanf("%s",buf);
		vector<int> v;
		for (int i=0;i<n;i++)
		{
			char ch = buf[i]-'A';
			if (v.size() > 0 && ar[v.back()][ch] != -1)
			{
				ch = ar[v.back()][ch];
				v.pop_back();
				v.push_back(ch);
				continue;
			}
			bool ok = 1;
			for (int j=0;j<v.size();j++)
			{
				if (br[v[j]][ch])
				{
					v.clear();
					ok=0;
					break;
				}
			}
			if (!ok)
				continue;
			v.push_back(ch);
		}
		printf("Case #%d: [",test);
		for (int i=0;i<v.size();i++)
		{
			printf("%c",(char)(v[i]+'A'));
			if (i+1 < v.size())
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}