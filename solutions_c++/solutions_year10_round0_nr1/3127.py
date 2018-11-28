#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<queue>
#include<stack>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#define MAXN 
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
//	freopen("in.txt","r",stdin);
//	freopen("google_1.txt","w",stdout);
#endif

	int dataset;
	scanf("%d",&dataset);
	for(int cas=1;cas<=dataset;++cas)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		k%=(1<<n);
		printf("Case #%d: ",cas);
		if(k+1==(1<<n))
			puts("ON");
		else
			puts("OFF");
	}

	return 0;
}
