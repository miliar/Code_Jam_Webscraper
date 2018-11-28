#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main()
{
	freopen("C-large.in","r", stdin);
	freopen("out.txt","w",stdout);
	int t,r,n,k;
	int g[1005];
	int s[1005];
	int next[1005];
	int l;
	scanf("%d",&t);
	for(int c = 1;c<=t;c++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(int i = 0;i<n;++i)
			scanf("%d",&g[i]);
		for(int i = 0;i<n;++i)
		{
			int sum = 0;
			int nextpos = i;
			for(int j =0;;++j)
			{
				int h = (i+j)%n;
				if((j!=0&&h ==i) || sum+g[h] > k)break;
				nextpos = h;
				sum+=g[h];
			}
			s[i] = sum;
			next[i] = nextpos;
		}
		long long res = 0;
		int cur = 0;
		for(int i = 0; i < r;++i)
		{
			res += s[cur];
			cur = (next[cur]+1)%n;
		}
		printf("Case #%d: %lld\n",c,res);
	}
	return 0;
}
