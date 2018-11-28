#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int T;
	
// 	freopen("A-large.in","r",stdin);
// 	freopen("out2.txt","w",stdout);
	scanf("%d",&T);
	for (int iCase=1; iCase<=T; ++iCase)
	{
		int N,K;
		scanf("%d%d",&N,&K);
		int x = (1<<N);
		printf("Case #%d: %s\n",iCase,(K%(x)!=x-1)?"OFF":"ON");
	}
	
}
