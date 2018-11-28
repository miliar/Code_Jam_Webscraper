#include <iostream>
#define M 50
using namespace std;
int N,K;
int main()
{
	int T,cnt;
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	scanf("%d",&T);
	for (cnt=1;cnt<=T;cnt++)
	{
		int i,j;
		scanf("%d%d",&N,&K);
		int state=1<<N;
		int ans=K%state;
		if (state-ans==1)
			printf("Case #%d: ON\n",cnt);
		else 
			printf("Case #%d: OFF\n",cnt);
	}
	return 0;
}