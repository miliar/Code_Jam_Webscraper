#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;
set < int >st;
int n,m;
FILE *fp;
int main()
{
	fp=fopen("1.out","w");
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d%d",&n,&m);
		int ans=0;
		for(int i=n; i<=m; i++)
		{
			st.clear();
			int tem=i,bin;
			if(tem<10)bin=1;
			if(tem>=10)bin=10;
			if(tem>=100)bin=100;
			if(tem>=1000)bin=1000;
			if(tem>=10000)bin=10000;
			if(tem>=100000)bin=100000;
			if(tem>=1000000)bin=1000000;
			while(1)
			{
				tem=tem/10+tem%10*bin;
				if(tem>i&&tem<=m)
					st.insert(tem);
				if(tem==i)break;
			}
			ans+=st.size();
		}
		printf("Case #%d: ",t);
		printf("%d\n",ans);
		/*fprintf(fp,"Case #%d: ",t);
		fprintf(fp,"%d\n",ans);*/
	}
	return 0;
}
