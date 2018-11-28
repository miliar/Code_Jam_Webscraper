#include<iostream>
#include<algorithm>
using namespace std;

int N,K;
int main()
{
	//freopen("F:\\A-large.in","r",stdin);
	//freopen("F:\\A-large.out","w",stdout);
	int i,j,T;scanf("%d",&T);
	int CN=0;
	while(T--)
	{
		scanf("%d%d",&N,&K);
		int tt=(1<<N);
		printf("Case #%d: ",++CN);
		if(K%tt==tt-1) puts("ON");
		else puts("OFF");
	}
	//system("pause");
	return 0;
}
