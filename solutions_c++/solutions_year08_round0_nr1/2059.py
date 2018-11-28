#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))
map<string,int> cid;
int d[100];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for (int ti=1;ti<=t;ti++){
		char s[105];
		cid.clear();
		int n;
		gets(s);
		sscanf(s,"%d",&n);
		for (int i=0;i<n;i++){
			gets(s);
			cid[s]=i;
			d[i]=0;
		}
		int q;
		gets(s);
		sscanf(s,"%d",&q);
		for (int i=0;i<q;i++){
			gets(s);
			int num=cid[s],mn=9999;
			for (int i=0;i<n;i++)
			if (d[i]<mn)
				mn=d[i];
			for (int i=0;i<n;i++)
			if (d[i]>mn+1)
				d[i]=mn+1;
			d[num]=10000;
		}
		int res=10000;
		for (int i=0;i<n;i++)
		if (d[i]<res)
			res=d[i];
		printf("Case #%d: %d\n",ti,res);
	}
	return 0;
}