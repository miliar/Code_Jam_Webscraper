#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	bool flagB=false, flagF=false;
	int i,L,D,N;
	char a[25][10], b[500];
	scanf("%d%d%d",&L,&D,&N);
	for(i=0; i<D; i++)
		scanf("%s",a[i]);
	for(i=0; i<N; i++)
	{
		scanf("%s",b);
		int count=0, length = strlen(b);
		for(int j=0; j<D; j++)
		{
			int p=0;
			for(int k=0;k<length; k++)
			{
				if(b[k]=='(')
					flagB=true;
				else
					flagB=false;
					
				flagF=false;
				if(flagB==false)
				{
					if(b[k]==a[j][p])
					{
						p++;
						flagF=true;
					}
					else
					{
						flagF=false;
						break;
					}
				}
				else
				{
					while(b[k]!=')' && k<length)
					{
						if(b[k]==a[j][p])
						{
							if(flagF!=true)
								p++;
							flagF=true;
						}
						k++;
					}
				}
				if(flagF!=true)
					break;
				
			}
			if(flagF==true)
				count++;
			
			
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	
}
