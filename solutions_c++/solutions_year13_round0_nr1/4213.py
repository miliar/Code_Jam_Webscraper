#include <cstdio>
#include <cstring>
#include <iostream>

int main()
{
    int win[0x10000];
	memset(win, 0, sizeof win);
	int wincases[10] = {0xf, 0xf0, 0xf00, 0xf000,
						0x1111 , 0x2222, 0x8888, 0x4444,
						0x1248,
						0x8421 };
	for(int i = 0; i < (1<<16); i ++)
	{
		for(int j = 0; j < 10; j ++)
		{
			if( (i & wincases[j]) == wincases[j])
			{
				win[i] = 1;
				break;
			}
		}
	}
	int T, cases = 0;
	scanf("%d", &T);
	while(T--)
	{
		printf("Case #%d: ", ++cases);
		int x = 0, o =0;
		int count = 0;
		for(int i = 1; i < (1 << 16); i <<= 1)
		{
			char c;
			std::cin >> c;

			switch (c)
			{
				case 'O':
				  o |= i;
				  break;
				case 'X':
				  x |= i;
				  break;
				case 'T':
				  o |= i;
				  x |= i;
				break;
				default:
				  count--;
				  break;
			}
			count++;
		}
		if(win[o] == 1) printf("O won\n");
		else if(win[x] == 1) printf("X won\n");
		else if(count == 16) printf("Draw\n");
		else printf("Game has not completed\n");
	}



}
