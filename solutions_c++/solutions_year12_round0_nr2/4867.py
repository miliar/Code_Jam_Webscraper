// BCODE.cpp: archivo de proyecto principal.

#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

int Vec[500];
int aux[500][3];

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int t,n,s,p;
	int temp;
	scanf("%d\n",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d %d %d",&n,&s,&p);
		for(int j=0;j<n;j++)
			scanf("%d",&Vec[j]);

		
		for(int j=0;j<n;j++)
		{
			temp=Vec[j];
			aux[j][0]=temp/3;
			temp=temp-aux[j][0];
			
			aux[j][1]=temp/2;
			temp=temp-aux[j][1];
			
			aux[j][2]=temp;

			
			if(aux[j][0]== aux[j][1] && aux[j][0]==aux[j][2])
				if(aux[j][0]==p-1 && p-1>0)
				{
					if(s>0)
					{
						aux[j][0]--;
						aux[j][2]++;
						s--;
					}
				}
		
			if(aux[j][1]==aux[j][2])
				if(aux[j][1]==p-1 && p-1>0)
				{
					if(s>0)
					{
						aux[j][1]--;
						aux[j][2]++;
						s--;
					}
				}


		}
		int cont=0;
		for(int j=0;j<n;j++)
		{
			if(aux[j][0]>=p || aux[j][1]>=p || aux[j][2]>=p)
			{
				cont++;
			}
		}
		printf("Case #%d: %d\n",i,cont);
	}
    return 0;
}
