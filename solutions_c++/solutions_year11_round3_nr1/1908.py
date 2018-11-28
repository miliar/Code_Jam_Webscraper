#include <stdio.h>
#include <stdlib.h>

int main()
{
	int T, N, i, j, k, O, B, bt;
	char map[60][60];
	int width, height;
	bool isCover;

	scanf(" %d", &T);

	for(i=0 ; i<T ; i++)
	{
		scanf(" %d", &height);
		scanf(" %d", &width);
		for(j=0 ; j<height ; j++)
		{
			for(k=0 ; k<width ; k++)
			{
				scanf(" %c", &map[j][k]);
			}
		}

		for(j=0 ; j<height-1 ; j++)
		{
			for(k=0 ; k<width-1 ; k++)
			{
				switch(map[j][k])
				{
				case '.':
				case '/':
				case '\\':
					break;
				case '#':
					if(map[j][k+1] == '#' && map[j+1][k] == '#')
					{
						if(map[j+1][k+1] == '#')
						{
							map[j][k] = '/';
							map[j][k+1] = '\\';
							map[j+1][k] = '\\';
							map[j+1][k+1] = '/';
						}
					}
					break;
				}
			}
		}
		
		isCover = true;
		for(j=0 ; j<height ; j++)
		{
			for(k=0 ; k<width ; k++)
			{
				if(map[j][k] == '#')
				{
					isCover = false;
					break;
				}
			}
		}

		if(isCover == false)
		{
			printf("Case #%d:\nImpossible\n", i+1);
		}
		else
		{
			printf("Case #%d:\n", i+1);
			for(j=0 ; j<height ; j++)
			{
				for(k=0 ; k<width ; k++)
				{
					printf("%c", map[j][k]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}