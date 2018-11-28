#include <stdio.h>
int main()
{
	freopen("a.in","r",stdin);
	freopen("my_a.out","w",stdout);
	int CASE,n;
	scanf("%d",&CASE);
	for(int cas=1;cas<=CASE;cas++)
	{
		int posO,posB,secondO,secondB;
		posO=posB=1;
		secondO=secondB=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			char c;
			do{scanf("%c",&c);}
			while(c!='O'&&c!='B');
			
			int p;
			scanf("%d",&p);
			
			if(c=='O')
			{
				int d=p-posO<=0?posO-p:p-posO;			
				if(secondO+d>=secondB)
				{
					secondO=secondO+d+1;
				}
				else secondO=secondB+1;
				posO=p;
			}
			else 
			{
				int d=p-posB<=0?posB-p:p-posB;			
				if(secondB+d>=secondO)
				{
					secondB=secondB+d+1;
				}
				else secondB=secondO+1;
				posB=p;
			}
		}
		printf("Case #%d: %d\n",cas,secondO>secondB?secondO:secondB);
	}
}

