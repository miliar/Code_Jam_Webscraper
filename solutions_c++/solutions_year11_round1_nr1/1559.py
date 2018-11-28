#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
using namespace std;
int main()
{
	int t,i;
	int n,d,g;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	int num = 1;
	int findnum;
	for (i= 1;i <= t;i++){
		num = 100;
		scanf("%d%d%d",&n,&d,&g);
		int d1 = d;
		while (d1 % 2 == 0 && num %2 == 0){
			d1 /= 2;
			num /= 2;
		}
		while (d1 % 5 == 0 && num %5 == 0){
			d1 /= 5;
			num /= 5;
		}
		findnum = num;
		if (findnum > n || (g == 0&& d != 0) || (g == 100 && d != 100)){
			printf("Case #%d: Broken\n",i);
			continue;
		}
		else
			printf("Case #%d: Possible\n",i);
	}
	return 0;
}