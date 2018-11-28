
#include <stdio.h>
#include <stdlib.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int  N, Btn;
		char C[100];

		int  Time = 0;
		int  OrangeLastBtn = 1;
		int  OrangeLastTime = 0;
		int  BlueLastBtn = 1;
		int  BlueLastTime = 0;
		char LastColor = '-';

		scanf("%d", &N);

		for(int j=1; j<=N; j++)
		{
			scanf("%s", C);
			scanf("%d", &Btn);

		    //printf("N=%d, C=%s, B=%d\n", N, C, Btn);

			if ( C[0] != LastColor )
			{
				if ( C[0] == 'O' )
				{
					OrangeLastTime = max( BlueLastTime + 1, OrangeLastTime + abs(Btn - OrangeLastBtn) + 1);
					OrangeLastBtn = Btn;
				}
				else if ( C[0] == 'B' )
				{
					BlueLastTime = max( OrangeLastTime + 1, BlueLastTime + abs(Btn - BlueLastBtn) + 1);
					BlueLastBtn = Btn;
				}
			}
			else
			{
				if ( C[0] == 'O' )
				{
					OrangeLastTime = OrangeLastTime + abs(Btn - OrangeLastBtn) + 1;
					OrangeLastBtn = Btn;
				}
				else
				{
					BlueLastTime = BlueLastTime + abs(Btn - BlueLastBtn) + 1;
					BlueLastBtn = Btn;
				}
			}
			LastColor = C[0];

		}

		int ans;
		
		ans = max( OrangeLastTime, BlueLastTime);

		printf("Case #%d:", i);
		printf(" %d", ans);
    	printf("\n");
	}
  
	return  0;  
}

