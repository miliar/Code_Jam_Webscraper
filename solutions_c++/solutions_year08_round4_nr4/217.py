#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int T,k,ans,len;
int num[5];
char str[1001],str1[1001];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T;++t)
	{
		scanf("%d",&k);
		scanf("%s",str);
		len = strlen(str);
		ans = len;
		for(int i = 0;i < k;++i)
			num[i] = i;
		do
		{
			int now = 0;
			while(now < len/k)
			{
				for(int i = 0;i < k;++i)
					str1[i+now*k] = str[num[i]+now*k];
				now++;
			}
			int count = 0;
			for(int i = 0;i < len-1;++i)
				if(str1[i] != str1[i+1])
					++count;
			++count;
			if(count < ans)
				ans = count;
		}while(next_permutation(num,num+k));
		printf("Case #%d: %d\n",t,ans);
	}
}