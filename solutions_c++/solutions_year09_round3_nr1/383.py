#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>



char s[100];
int maping[1000];

void run()
{
	scanf("%s",s);
	int len = strlen(s);
	bool useZero = false;
	int number = 1;
	memset(maping,0,sizeof(maping));
	for(int i=0; i<len; i++)
	{
		if(maping[s[i]]==0)
		{
			if(i!=0 && !useZero)
			{
				maping[s[i]]=-1;
				useZero=true;
			}
			else
			{
				maping[s[i]]=number++;
			}
		}
	}
	long long res = 0;
	for(int i=0; i<len; i++)
	{
		res*=number;
		int val = maping[s[i]];
		if(val<0)val=0;
		res+=val;
	}
	printf("%lld",res);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int testCount;
	scanf("%d",&testCount);
	for(int testNumber=1; testNumber<=testCount; testNumber++)
	{
		printf("Case #%d: ",testNumber);
		run();
		printf("\n");
	}
	return 0;
}