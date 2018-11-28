#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<complex>
#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>


using namespace std;

int n;

int go[12000];
int main()
{
	freopen("C:\\GGGG\\ooo.txt","w",stdout);
	int i,j,k;
	int c,h1,g;
	int l,h;
	scanf("%d",&h1);
	for (c=1;c<=h1;c++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for (i=0;i<n;i++)scanf("%d",go+i);
		printf("Case #%d: ",c);
		for (i=l;i<=h;i++)
		{
			for (j=0;j<n;j++)
			{
				if (go[j]%i==0)continue;
				if (i%go[j]==0)continue;
				break;
			}
			if (j==n)
			{
				printf("%d\n",i);
				break;
			}
		}
		if (i==h+1)printf("%s\n","NO");
	}
	return 0;
}
			
						
	
