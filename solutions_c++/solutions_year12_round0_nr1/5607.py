#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,N,K,CASE=0;
	int i,j,k,p;
	char S[200], G[200];
	int x,y;

	char mapping[26] = {'y' , 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);


	gets(G);
	sscanf(G,"%d",&T);

	while(T--)
	{
		CASE++;

		gets(G);

		for(i=0; G[i]; i++)
		{
			if(G[i] == ' ')
				S[i] = G[i];
			else
				S[i] = mapping[G[i]-'a'];
		}
		S[i] = 0;


		printf("Case #%d: %s\n",CASE, S);

	}




}