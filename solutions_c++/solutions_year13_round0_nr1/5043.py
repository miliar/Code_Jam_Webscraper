#include <cstdio>

int main()
{
	int t;
	scanf("%d", &t);
	
	
	for(int c = 1; c<=t; c++)
	{
		char data[4][5];
		for(int i=0;i<4;i++)
			scanf(" %s", data[i]);
			
				
		bool draw = true;
		for(int i=1;i<=2;i++)
		{
			char l = i==1 ? 'X' : 'O';
			bool won = false;
			
			//Wygrana w linii poziomej
			for(int y=0;y<4;y++)
			{
				bool wonhere = true;
				for(int x = 0; x<4; x++)
				{
					if(data[y][x]!=l && data[y][x]!='T') wonhere = false;
				}
				if(wonhere) won=true;
			}
			//Wygrana w linii pionowej
			for(int x=0;x<4;x++)
			{
				bool wonhere = true;
				for(int y = 0; y<4; y++)
				{
					if(data[y][x]!=l && data[y][x]!='T') wonhere = false;
				}
				if(wonhere) won=true;
			}
			//Przekątna \x 
			bool wonhere = true;
			for(int x=0;x<4;x++)
			{				
				if(data[x][x]!=l && data[x][x]!='T') wonhere = false;
			}
			if(wonhere) won=true;
			
			//Przekątna / 
			/*bool */wonhere = true;
			for(int x=0;x<4;x++)
			{				
				if(data[x][3-x]!=l && data[x][3-x]!='T') wonhere = false;
			}
			if(wonhere) won=true;
			
			if(won)
			{
				printf("Case #%d: %c won\n", c, l);
				draw = false;
				break;
			}
		}	
		
		
		if(draw)
		{
			//Czy skonczona?
			bool complete=true;
			for(int x=0;x<4;x++)
			for(int y=0;y<4;y++)
			{
				if(data[y][x]=='.')
				{
					complete = false;
				}
			}		
			if(!complete)
			{
				printf("Case #%d: Game has not completed\n", c);
			}
			else
				printf("Case #%d: Draw\n", c);
		}
	}
}
