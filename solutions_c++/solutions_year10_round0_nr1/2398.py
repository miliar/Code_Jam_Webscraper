#include<iostream>
#include<cstdio>
using namespace std;

int main(void)
{
	int power[31];
	int n,k,t,m;
	int count=0;
	power[0]=1;
	for(int i=1; i<31; i++)
		power[i]=power[i-1]*2;
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		count++;
		scanf("%d %d",&n,&k);
		m=power[n];
		if(k%m==m-1)
			printf("Case #%d: ON\n",count);
		else
			printf("Case #%d: OFF\n",count);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
