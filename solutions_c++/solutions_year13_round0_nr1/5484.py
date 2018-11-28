#include <cstdio>

using namespace std;

int main()
{
	int T , i , j ;
	char ary[4][4] , symb;
	bool draw , flag;
	scanf("%d" , &T);
	for(int a=1 ; a<=T ; a++)
	{
		printf("Case #%d: ", a);
		scanf("%c" , &symb);
		draw = true;
		for(i=0 ; i<4 ; i++)
		{
			for(j=0 ; j<4 ; j++)
			{
				scanf("%c" , &ary[i][j]);
				if(ary[i][j] == '.')
					draw = false;
			}
			scanf("%c" , &symb);
		}

		
		//raw
		flag = false;
		for(i=0 ; i<4 ; i++)
		{
			flag = true;
			symb = ary[i][0];
			if(symb == 'T')
				symb = ary[i][1];
			if(symb == '.')
			{
				flag = false;
				continue;
			}
			for(j=1 ; j<4 ; j++)
			{
				if(ary[i][j] != symb && ary[i][j] != 'T' )
				{
					flag = 0;
					break;
				}
				if(ary[i][j] == '.')
				{
					flag = 0;
					break;
				}
				
			}
			if(flag)
				break;
		}
		if(flag)
		{
			printf("%c won\n" , symb);
			continue;
		}
		//column
		for(i=0 ; i<4 ; i++)
		{
			flag = true;
			symb = ary[0][i];
			if(symb == 'T')
				symb = ary[1][i];
			if(symb == '.')
			{
				flag = false;
				continue;
			}
			for(j=1 ; j<4 ; j++)
			{
				if(ary[j][i] != symb && ary[j][i] != 'T' )
				{
					flag = 0;
					break;
				}
				if(ary[j][i] == '.')
				{
					flag = 0;
					break;
				}
				
			}
			if(flag)
				break;
		}
		if(flag)
		{
			printf("%c won\n" , symb);
			continue;
		}
		//diagonal1
		flag = true;
		symb = ary[0][0];
		if(symb == 'T')
			symb = ary[1][i];
		if(symb == '.')
		{
			flag = false;
		}
		for(j=1 ; j<4 ; j++)
		{
			if(ary[j][j] != symb && ary[j][j] != 'T' )
			{
				flag = 0;
				break;
			}
			if(ary[j][j] == '.')
			{
				flag = 0;
				break;
			}
		}
		if(flag)
		{
			printf("%c won\n" , symb);
			continue;
		}
		//diagonal1
		flag = true;
		symb = ary[0][3];
		if(symb == 'T')
			symb = ary[1][2];
		if(symb == '.')
		{
			flag = false;
		}
		for(j=1 ; j<4 ; j++)
		{
			if(ary[j][3-j] != symb && ary[j][3-j] != 'T' )
			{
				flag = 0;
				break;
			}
			if(ary[j][3-j] == '.')
			{
				flag = 0;
				break;
			}
		}
		if(flag)
		{
			printf("%c won\n" , symb);
			continue;
		}
		else if(!draw)
		{
			printf("Game has not completed\n");
			continue;
		}
		else
		{
			printf("Draw\n");
		}
	}
	return 0;
}
