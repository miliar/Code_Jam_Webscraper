#include <stdio.h>
#include <string.h>

int main(int argc , char * argv[])
{
	int T;
	scanf("%d",&T);
	for(int t = 0;t<T;t++)
	{
		char ** ar = new char * [4];
		for(int i = 0;i<4;i++)
		{
			ar[i] = new char [4];
		}

		for(int i1 = 0;i1 < 4;i1++)
		{
			scanf("%s",ar[i1]);
		}

		/*for(int i = 0;i<4;i++)
		{
			for(int f = 0;f<4;f++)
			{
				printf("%c ",ar[i][f]);
			}
			printf("\n");
		}*/

		int r = 4,c = 4;
		bool haveT = false;
		for(int chai = 0;chai<4;chai++)
		{
			for(int chaf = 0;chaf<4;chaf++)
			{
				if(ar[chai][chaf] == 'T')
				{
					haveT = true;
					r = chai;
					c = chaf;
				}
			}
		}

		
		if(haveT == true)
		{
			bool end = false;
			for(int tes = 0;tes<2;tes++)
			{
				if(tes == 0)
				{
					ar[r][c] = 'O';
				}
				if(tes == 1)
				{
					ar[r][c] = 'X';
				}
				if(end == false)
				{
						for(int row = 0;row<4;row++) //row
						{
							if(ar[row][0] == ar[row][1] && ar[row][1] == ar[row][2] && ar[row][2] == ar[row][3] && ar[row][0] != '.' && end == false)
							{
								end = true;
								printf("Case #%d: %c won\n",(t+1),ar[row][0]);
							}
						}
						for(int se = 0;se < 4;se++) //col
						{
							if(ar[0][se] == ar[1][se] && ar[1][se] == ar[2][se] && ar[2][se] == ar[3][se] && ar[0][se] != '.' && end == false)
							{
								end = true;
								printf("Case #%d: %c won\n",(t+1),ar[0][se]);
							}
						}
						//dia
						if(ar[0][0] == ar[1][1] && ar[1][1] == ar[2][2] && ar[2][2] == ar[3][3] && ar[0][0] != '.' && end == false)
						{
							end = true;
							printf("Case #%d: %c won\n",(t+1),ar[0][0]);
						}
						if(ar[0][3] == ar[1][2] && ar[1][2] == ar[2][1] && ar[2][1] == ar[3][0] && ar[0][3] != '.' && end == false)
						{
							end = true;
							printf("Case #%d: %c won\n",(t+1),ar[0][3]);
						}
						if(end == false)
						{
							bool foup = false;
							for(int fou = 0;fou<4;fou++)
							{
								for(int fo = 0;fo<4;fo++)
								{
									if(ar[fou][fo] == '.')
									{
										foup = true;
									}
								}
							}
							if(foup == true && tes == 1)
							{
								printf("Case #%d: Game has not completed\n",(t+1));
								end = true;
							}
						}
						if(end == false && tes == 1)
						{
							printf("Case #%d: Draw\n",(t+1));
						}
				}
			}
		}
		if(haveT == false)
		{
			bool end = false;
			for(int row = 0;row<4;row++) //row
			{
				if(ar[row][0] == ar[row][1] && ar[row][1] == ar[row][2] && ar[row][2] == ar[row][3] && ar[row][0] != '.' && end == false)
				{
					end = true;
					printf("Case #%d: %c won\n",(t+1),ar[row][0]);
				}
			}
			for(int se = 0;se < 4;se++) //col
			{
				if(ar[0][se] == ar[1][se] && ar[1][se] == ar[2][se] && ar[2][se] == ar[3][se] && ar[0][se] != '.' && end == false)
				{
					end = true;
					printf("Case #%d: %c won\n",(t+1),ar[0][se]);
				}
			}
			//dia
			if(ar[0][0] == ar[1][1] && ar[1][1] == ar[2][2] && ar[2][2] == ar[3][3] && ar[0][0] != '.' && end == false)
			{
				end = true;
				printf("Case #%d: %c won\n",(t+1),ar[0][0]);
			}
			if(ar[0][3] == ar[1][2] && ar[1][2] == ar[2][1] && ar[2][1] == ar[3][0] && ar[0][3] != '.' && end == false)
			{
				end = true;
				printf("Case #%d: %c won\n",(t+1),ar[0][3]);
			}
			if(end == false)
			{
				bool foup = false;
				for(int fou = 0;fou<4;fou++)
				{
					for(int fo = 0;fo<4;fo++)
					{
						if(ar[fou][fo] == '.')
						{
							foup = true;
						}
					}
				}
				if(foup == true)
				{
					printf("Case #%d: Game has not completed\n",(t+1));
					end = true;
				}
			}
			if(end == false)
			{
				printf("Case #%d: Draw\n",(t+1));
			}
		}
	}

	return 0;
}