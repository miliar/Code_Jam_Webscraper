#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[1111],n;bool v[1111];
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)scanf("%d",a+i);
		int S=0;
		memset(v,0,sizeof v);
		for(int i=1;i<=n;i++)
			if(!v[i])
			{
				int s=0,j=i;
				while(!v[j])v[j]=1,j=a[j],s++;
				if(s!=1)S+=s;
			}
		printf("Case #%d: %d.000000\n",__,S);
	}
	return 0;
}

