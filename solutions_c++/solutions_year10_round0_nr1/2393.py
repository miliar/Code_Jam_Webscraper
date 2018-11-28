#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int i;
	int t, n, k;
	int isOff;

	//freopen("D:\\VC2005\\google\\2010\\ProbA\\example.txt","r",stdin);
	freopen("D:\\VC2005\\google\\2010\\ProbA\\A-large.in","r",stdin);
	freopen("D:\\VC2005\\google\\2010\\ProbA\\A-large.out","w",stdout);

	scanf("%d\n", &t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d\n", &n, &k);
		isOff=(k+1)% (int)pow(2.0,n);

		//printf("%d %d\n", n, k);
		if(isOff) printf("Case #%d: OFF\n", i);
		else printf("Case #%d: ON\n", i);
	}

	fclose(stdout);
	return 0;
}
