#include <bits/stdc++.h>

int main()
{
	int t,cdot,co,cx,ct,po,px,flag,i,j,k;
	char s[4][10];
	scanf("%d",&t);
	for(k = 1;k <=t;k++)
	{
		for(i = 0;i < 4;i++)
		{
			scanf("%s",s[i]);
		}
		po = px = 0;flag = 0;
		for(i = 0;i < 4;i++)
		{
			cdot = co = cx = ct = 0;
			for(j = 0;j < 4;j++)
			{
				if(s[i][j]=='.')
				{
					flag = 1;
				}
				switch(s[i][j])
				{
					case  '.':
						cdot++;
						break;
					case 'O':
						co++;
						break;
					case 'X':
						cx++;
						break;
					case 'T':
						ct++;
						break;
				}
				
			}
			if((co == 4) || (co==3 && ct==1))
			{
				po = 1;
				break;
			}
			if((cx == 4) || (cx==3 && ct==1))
			{
				px = 1;
				break;
			}
			
			cdot = co = cx = ct = 0;
			for(j = 0;j < 4;j++)
			{
				
				switch(s[j][i])
				{
					case  '.':
						cdot++;
						break;
					case 'O':
						co++;
						break;
					case 'X':
						cx++;
						break;
					case 'T':
						ct++;
						break;
				}
				

			}
			
			if((co == 4) || (co==3 && ct==1))
			{
				po = 1;
				break;
			}
			if((cx == 4) || (cx==3 && ct==1))
			{
				px = 1;
				break;
			}
			cdot = co = cx = ct = 0;
			for(j = 0;j < 4;j++)
			{
				switch(s[j][j])
				{
					case  '.':
						cdot++;
						break;
					case 'O':
						co++;
						break;
					case 'X':
						cx++;
						break;
					case 'T':
						ct++;
						break;
				}
				
			}
			if((co == 4) || (co==3 && ct==1))
			{
				po = 1;
				break;
			}
			if((cx == 4) || (cx==3 && ct==1))
			{
				px = 1;
				break;
			}
			cdot = co = cx = ct = 0;
			for(j = 0;j < 4;j++)
			{
				switch(s[j][3-j])
				{
					case  '.':
						cdot++;
						break;
					case 'O':
						co++;
						break;
					case 'X':
						cx++;
						break;
					case 'T':
						ct++;
						break;
				}
				
			}
			if((co == 4) || (co==3 && ct==1))
			{
				po = 1;
				break;
			}
			if((cx == 4) || (cx==3 && ct==1))
			{
				px = 1;
				break;
			}
		}
		
		if(po==1)
		{
			printf("Case #%d: O won\n",k);
		}
		else if(px==1)
		{
			printf("Case #%d: X won\n",k);
		}
		else if(flag==0)
		{
			printf("Case #%d: Draw\n",k);
		}
		else
		{
			printf("Case #%d: Game has not completed\n",k);
		}
		
		
	}
	return 0;
}
