#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int nt;
	scanf("%d",&nt);
	int tmp = nt;
	while(nt--) {
		int n,k;
		scanf("%d %d",&n,&k);
		if((k+1)%(1<<n)==0)
			printf("Case #%d: ON\n",tmp-nt);
		else
			printf("Case #%d: OFF\n",tmp-nt);
	}
	return 0;
}
