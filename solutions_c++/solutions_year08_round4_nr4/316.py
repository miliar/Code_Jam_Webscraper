#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int c,o,k,i,j,n,ans,now,p[8];
	char str[1024],our[1024];
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%d%s",&k,str);
		n=strlen(str);
		for(i=0;i<k;i++)
			p[i]=i;
		ans=-1;
		do
		{
			for(i=0;i<n;i+=k)
				for(j=0;j<k;j++)
					our[i+j]=str[i+p[j]];
			now=0;
			for(i=0;i<n;i++)
				if(!i||our[i]!=our[i-1])
					now++;
			if(ans==-1||now<ans)
				ans=now;
		}while(next_permutation(p,p+k));
		printf("Case #%d: %d\n",o,ans);
	}
	return 0;
}

