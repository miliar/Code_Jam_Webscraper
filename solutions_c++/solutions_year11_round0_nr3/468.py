#include <stdio.h>
#include <string>


int main(void)
{

    FILE *f;
	f=fopen("C-large.in","r");

	int time=0;
	int tc;
	fscanf(f,"%d\n",&tc);
	for(int t=0;t<tc;t++)
	{
		int c;
		fscanf(f,"%d\n",&c);

		int xor=0;
		__int64 add=0;
		int smallest=0x3fffFFFF;
		for(int i=0;i<c;i++)
		{
			int v;
			fscanf(f,"%d ",&v);
			if (v<smallest) smallest = v;
            xor ^= v;
			add += v;
			if (add<0 || add>0x3ffffFFF)
			{
				printf("ERROR\n");
				return 2;
			};
		};


		int fin=0;
		if (xor!=0)
		{
			printf("Case #%d: NO\n",t+1,0);
            
		}
		else
		{
			printf("Case #%d: %lld\n",t+1,add-smallest);
		};
	};





	return 1;
};