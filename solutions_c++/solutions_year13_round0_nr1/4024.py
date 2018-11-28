#include <string>
#include <iostream>
#include <cstdio>

bool is_X(char a)
{
	return (a=='X'||a=='T');
} 
bool is_O(char a)
{
	return (a=='O'||a=='T');
}

std::string tab[4];
int t;
int i, j;

int main()
{
	std::cin>>t;
	int k=1;
	while(k<=t)
	{
		for(i=0; i<4; i++)
		{
			std::cin>>tab[i];
		}

		bool checked=false;
		for(i=0; i<4; i++)
		{
			j=0;
			while(j<4)
			{
				if(is_X(tab[i][j])==false)
					break;
				j++;
			}
			if(j==4)
			{
				printf("Case #%d: X won\n", k);
				checked=true;
				break;
			}
			j=0;
			while(j<4)
			{
				if(is_O(tab[i][j])==false)
					break;
				j++;
			}
			if(j==4)
			{
				printf("Case #%d: O won\n", k);
				checked=true;
				break;
			}
		}
		if(checked==false)
		{
			for(i=0; i<4; i++)
			{
				j=0;
				while(j<4)
				{
					if(is_X(tab[j][i])==false)
						break;
					j++;
				}
				if(j==4)
				{
					printf("Case #%d: X won\n", k);
					checked=true;
					break;
				}
				j=0;
				while(j<4)
				{
					if(is_O(tab[j][i])==false)
						break;
					j++;
				}
				if(j==4)
				{
					printf("Case #%d: O won\n", k);
					checked=true;
					break;
				}
			}
			if(checked==false)
			{
				j=0;
				while(j<4)
				{
					if(is_X(tab[j][j])==false)
						break;
					j++;
				}
				if(j==4)
				{
					printf("Case #%d: X won\n", k);
					checked=true;
				}
				if(checked==false)
				{
					j=0;
					while(j<4)
					{
						if(is_O(tab[j][j])==false)
							break;
						j++;
					}
					if(j==4)
					{
						printf("Case #%d: O won\n", k);
						checked=true;
					}
				}
				if(checked==false)
				{
					j=0;
					while(j<4)
					{
						if(is_X(tab[j][3-j])==false)
							break;
						j++;
					}
					if(j==4)
					{
						printf("Case #%d: X won\n", k);
						checked=true;
					}
				}
				if(checked==false)
				{
					j=0;
					while(j<4)
					{
						if(is_O(tab[j][3-j])==false)
							break;
						j++;
					}
					if(j==4)
					{
						printf("Case #%d: O won\n", k);
						checked=true;
					}
				}
				if(checked==false)
				{
					bool is_empty=true;
					for(i=0; i<4; i++)
					{
						for(j=0; j<4; j++)
							if(tab[i][j]=='.')
							{
								is_empty=false;
								break;
							}
						
					}
					if(is_empty==true)
						printf("Case #%d: Draw\n", k);
					else
						printf("Case #%d: Game has not completed\n", k);
				}
			}
		}	

		for(int i=0; i<4; i++)
			tab[i].clear();
		k++;
	}

	return 0;
}
