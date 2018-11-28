#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<set>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;
int N,K;
int period[35];

int main()
{
	int T;
	cin>>T;
	for(int i=0;i<=30;i++)
		period[i]=(1<<i);
	for(int i=1;i<=T;i++)
	{
		scanf("%d%d",&N,&K);
		if(K%period[N]==period[N]-1)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}