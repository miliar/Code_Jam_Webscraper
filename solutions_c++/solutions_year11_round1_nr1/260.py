#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>

using namespace std;

int kasus,hari,total;
long long batas;

int main()
{
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;l++)
	{
		scanf("%I64d %d %d",&batas,&hari,&total);
		printf("Case #%d: ",l);
		
		if (!hari && (total != 100)) printf("Possible\n");
		else if (!total) printf("Broken\n");
		else if ((total == 100)&&(hari != 100)) printf("Broken\n");
		else
		{
			int whari = hari / __gcd(hari,100);
			int phari = 100 / __gcd(hari,100);
			int wtotal = total / __gcd(total,100);
			int ptotal = 100 / __gcd(total,100);
		
			if (phari > batas) printf("Broken\n");
			else printf("Possible\n");
		}
	}
	return 0;
}
