#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T=0,c,n,k;
	scanf("%d",&c);

	while (c>0)
	{
		c--,T++;
		scanf("%d%d",&n,&k);
		k=k%(1<<n);
		bool flag=true;
		for (int i=0;i<n;i++)
			flag=(flag && ((k&(1<<i))!=0));
		if (flag)
			printf("Case #%d: ON\n",T);
		else
			printf("Case #%d: OFF\n",T);
	}

	fclose(stdin);fclose(stdout);
	return 0;
}
