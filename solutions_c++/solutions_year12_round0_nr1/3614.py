#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{
	int T,i,ind,k=0;
	int len=0;
	char G[103];
	char O[103];
	char outp[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	scanf("%d",&T);	
	getchar();
	while(T--)
	{	
		k++;
		fgets(G,102,stdin);
		len=strlen(G);
		//printf("%d\n",len);

		for(i=0;i<len;i++)
		{	
			if(G[i] != ' ')
			{
				ind = G[i]-97;
				O[i] = outp[ind];
			}
			else
				O[i] = G[i];
		}
		O[i-1]='\0';
		printf("Case #%d: %s\n",k,O);

	}
			
	return(0);
}
