#include <stdio.h>
#include <string.h>
#include <algorithm> 
using namespace std;

char s[1024];
char r[1024];
int n[5];

int main() 
{
	int c,k;
	int i,j,t,l,x;
	int min;
	char a;

	scanf("%d",&c);
	for(t=1;t<=c;t++)
	{
		scanf("%d%s",&k,s);
		for(i=0;i<k;i++) n[i]=i;

		l=min=strlen(s);
		x=l/k;

		do
		{
			for(j=0;j<l;j+=k)
			{
				for(i=0;i<k;i++)
				{
					r[j+i]=s[j+n[i]];
				}
			}
			
			j=1;
			a=r[0];
			for(i=0;i<l;i++)
			{
				if(a!=r[i])
				{
					j++;
					a=r[i];
				}
			}

			if(j<min) min=j;

		}while(next_permutation(n,n+k)); 


		printf("Case #%d: %d\n",t,min);
	}

	return 0;
}
