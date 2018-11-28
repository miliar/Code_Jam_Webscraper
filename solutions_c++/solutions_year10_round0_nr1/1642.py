#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int T,N,K,tmp;
	freopen("A-large.in","rb",stdin);
	freopen("A-large.out","wb",stdout);
	scanf("%d",&T);
	for (int k=1;k<=T;k++)
	{
		scanf("%d%d",&N,&K);
		tmp=K-(1<<N)+1;
		printf("Case #%d: ",k);
		if (tmp>=0 && tmp%(1<<N)==0)
			puts("ON");
		else
			puts("OFF");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
