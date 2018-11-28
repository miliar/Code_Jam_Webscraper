#include<stdio.h>
#include<map>

using namespace std;

int main(void)
{
	freopen("E:\\A-small.in","r",stdin);
	freopen("E:\\A-small.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tcase;
	for(tcase = 1 ; tcase <= t; tcase ++)
	{
		char s[100];
		scanf("%s",s);
		map<char ,int> my;
		my[s[0]] = 1;
		bool zero = false;
		int mini = 2;
		int i;
		for(i=1;s[i];i++)
		{
			if(my.find(s[i]) != my.end())
				continue;
			if(!zero)
			{
				my[s[i]] = 0;
				zero = true;
			}
			else
			{
				my[s[i]] = mini++;
			}
		}
		long long result = 0;
		for(i=0;s[i];i++)
			result = result * mini + my[s[i]];
		printf("Case #%d: %lld\n",tcase,result);
	}
	return 0;
}