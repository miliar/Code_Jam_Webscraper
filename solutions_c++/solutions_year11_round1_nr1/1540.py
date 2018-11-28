
#include <stdio.h>
#include <vector>


int main(int argc, char* argv[])
{

	freopen("c:\\input.in","r",stdin);
	freopen("C:\\output.txt","w",stdout);

	int T = 0;

	scanf("%d", &T);

	for(int t = 0 ; t < T ; t++)
	{
		int N = 0 ;
		scanf("%d", &N);

		int Pd = 0;
		scanf("%d", &Pd);

		int Pg = 0;
		scanf("%d", &Pg);

		int factor2 = 0;
		int factor5 =0;
		if( Pd/4.0==Pd/4)
		{
			factor2 = 2;
		}
		else if (Pd/2.0==Pd/2)
		{
			factor2 = 1;
		}

		if( Pd/25.0==Pd/25)
		{
			factor5 = 2;
		}
		else if (Pd/5.0==Pd/5)
		{
			factor5 = 1;
		}
		
		int Dbase = 1;

		for(int i = 0 ; i < 2- factor2 ; i++)
		{
			Dbase *=2;
		}

		for(int i = 0 ; i < 2- factor5 ; i++)
		{
			Dbase *=5;
		}

		bool ret = false;

		if(Pg == 100 )
		{
			if(Pd == 100 && Dbase <= N)
				ret = true;
		}
		else if(Pg ==0)
		{
			if(Pd == 0)
				ret = true;
		}
		else{
			if(Dbase <= N) ret = true;
		}
		

		if(ret)
			printf("Case #%d: Possible\n", t+1);
		else
			printf("Case #%d: Broken\n", t+1);
	}

	return 0;
}