#include<cstdio>
#include<cstring>
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long i,j,k,l,m,n,test,cas=1,x,o,t;
	char ch[5][5];
	scanf("%ld",&test);
	while(test--)
	{
		for(i=0;i<4;i++)
			scanf("%s",ch[i]);
		for(i=0;i<4;i++)
		{
			x=o=t=0;
			for(j=0;j<4;j++)
			{
				if(ch[i][j]=='X')
					x++;
				else if(ch[i][j]=='T')
					t++;
				else if(ch[i][j]=='O')
					o++;
			}
			if(x==4||(x==3&&t==1))
			{
				x=1;
				o=0;
				break;
			}
			else if(o==4||(o==3&&t==1))
			{
				o=1;
				x=0;
				break;
			}
			else
			{
				o=x=0;
			}
		}
		if(x==1)
			printf("Case #%ld: X won\n",cas++);
		else if(o==1)
			printf("Case #%ld: O won\n",cas++);
		else
		{
				for(i=0;i<4;i++)
				{
					x=o=t=0;
					for(j=0;j<4;j++)
					{
						if(ch[j][i]=='X')
							x++;
						else if(ch[j][i]=='T')
							t++;
						else if(ch[j][i]=='O')
							o++;
					}
					if(x==4||(x==3&&t==1))
					{
						x=1;
						o=0;
						break;
					}
					else if(o==4||(o==3&&t==1))
					{
						o=1;
						x=0;
						break;
					}
					else
					{
						o=x=0;
					}
				}
				if(x==1)
					printf("Case #%ld: X won\n",cas++);
				else if(o==1)
					printf("Case #%ld: O won\n",cas++);
				else
				{
					x=o=t=0;
					for(i=0;i<4;i++)
					{
						if(ch[i][i]=='X')
							x++;
						else if(ch[i][i]=='O')
							o++;
						else if(ch[i][i]=='T')
							t++;
					}
					if(x==4||(x==3&&t==1))
					{
						printf("Case #%ld: X won\n",cas++);
					}
					else if(o==4||(o==3&&t==1))
					{
						printf("Case #%ld: O won\n",cas++);
					}
					else
					{
						x=o=t=0;
						j=0;
						for(i=3;i>=0;i--)
						{
							if(ch[j][i]=='X')
								x++;
							else if(ch[j][i]=='O')
								o++;
							else if(ch[j][i]=='T')
								t++;
							j++;
						}
						if(x==4||(x==3&&t==1))
						{
							printf("Case #%ld: X won\n",cas++);
						}
						else if(o==4||(o==3&&t==1))
						{
							printf("Case #%ld: O won\n",cas++);
						}
						else
						{
							k=0;
							for(i=0;i<4;i++)
							{
								for(j=0;j<4;j++)
								{
									if(ch[i][j]=='.')
									{
										k=1;
										break;
									}
								}
								if(k)
									break;
							}
							if(k)
								printf("Case #%ld: Game has not completed\n",cas++);
							else
								printf("Case #%ld: Draw\n",cas++);
						}

						
					}
			}	}
		}
		return 0;
	}


