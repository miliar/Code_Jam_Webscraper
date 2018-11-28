#include<cstdio>
using namespace std;
char a[4][4];

int main()
{
int t, res;
scanf("%d", &t);
for (int k=1; k<=t; k++)
{
	int i, j;
	res = 0;
	for (i = 0; i<4; i++)
		scanf("%s", a[i]);
	bool zle = 0;
	for (i=0; i<4; i++)
	{
		zle = 0;
		for (j=0; j<4; j++)
			if(a[i][j] != 'X' && a[i][j] != 'T')
			{
				zle = 1;
				break;
			}
		if(!zle)
		{
			res  = 1;
			goto moskwa;
		}
	}
	
	for (j=0; j<4; j++)
	{
		zle = 0;
		for (i=0; i<4; i++)
			if(a[i][j] != 'X' && a[i][j] != 'T')
			{
				zle = 1;
				break;
			}
			
		if(!zle)
		{
			res  = 1;
			goto moskwa;
		}
	}
	zle = 0;
	for (i=0; i<4; i++)
		if(a[i][i] != 'X' && a[i][i] != 'T')
		{
			zle = 1;
			break;
		}
	if(!zle)
	{
		res  = 1;
		goto moskwa;
	}
	
	zle = 0;
	for (i=0; i<4; i++)
		if(a[i][3-i] != 'X' && a[i][3-i] != 'T')
		{
			zle = 1;
			break;
		}
	if(!zle)
	{
		res  = 1;
		goto moskwa;
	}
	///////////////////////////////////////
	
	
	for (i=0; i<4; i++)
	{
		zle = 0;
		for (j=0; j<4; j++)
			if(a[i][j] != 'O' && a[i][j] != 'T')
			{
				zle = 1;
				break;
			}
		if(!zle)
		{
			res  = 2;
			goto moskwa;
		}
	}
	
	for (j=0; j<4; j++)
	{
		zle = 0;
		for (i=0; i<4; i++)
			if(a[i][j] != 'O' && a[i][j] != 'T')
			{
				zle = 1;
				break;
			}
		if(!zle)
		{
			res  = 2;
			goto moskwa;
		}
	}
	
	
	
	zle = 0;
	for (i=0; i<4; i++)
		if(a[i][i] != 'O' && a[i][i] != 'T')
		{
			zle = 1;
			break;
		}
	if(!zle)
	{
		res  = 2;
		goto moskwa;
	}
	
	
	zle = 0;
	for (i=0; i<4; i++)
		if(a[i][3-i] != 'O' && a[i][3-i] != 'T')
		{
			zle = 1;
			break;
		}
	if(!zle)
	{
		res  = 2;
		goto moskwa;
	}
	
	///////////////////////////////
	
	for (i=0; i<4; i++)
		for (j=0; j<4; j++)
			if(a[i][j]=='.')
			{
				res = 4;
				goto moskwa;
			}
			
	res = 3;
	
	moskwa:;
	
	if(res==1) printf("Case #%d: X won\n", k);
	else if(res==2) printf("Case #%d: O won\n", k);
	else if(res==3) printf("Case #%d: Draw\n", k);
	else if(res==4) printf("Case #%d: Game has not completed\n", k);
	else printf("ERROR\n");
}
return 0;
}	
	
	
	
		 
