#include<vector>
#include<cstdio>

using namespace std;

vector<int> pow;

int main()
{
	int z, n, k;
	pow.push_back(1);
	for(int i=1;i<=30;i++)
		pow.push_back(pow.back()*2);
	scanf("%d",&z);
	for(int i=1;i<=z;i++)
	{
		scanf("%d %d", &n, &k);
		if ( (k+1)%(pow[n])==0 ) printf("Case #%d: ON\n",i);
			else printf("Case #%d: OFF\n",i);
	}
	return 0;
}
