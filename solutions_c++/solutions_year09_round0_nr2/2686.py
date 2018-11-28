#include<stdio.h>
	
int map [100][100],r,c;
char basin [100][100],alp ='a'-1;
int count=0;

char tocell(int x,int y)
{
	int n=10001,w=10001,e=10001,s=10001;
	if(x-1 >= 0)
		n = map[x-1][y];
	if(y-1 >= 0)
		w = map[x][y-1];
	if(y+1 < c )
		e = map[x][y+1];
	if(x+1 < r)
		s = map[x+1][y];
	//printf("\n\n map[0][0]=%d map[1][0]=%d map[2][0]=%d",map[0][0],map[1][0],map[2][0]);
	//printf("\nx=%d y=%d n=%d w=%d s=%d e=%d",x,y,n,w,s,e);
	char sel = '-';
	int min = map[x][y];
	if(n < min)
	{
		sel = 'n';
		min = n;
	}
	
	if(w < min)
	{
		sel = 'w';
		min = w;
	}
	if(e < min)
	{
		sel = 'e';
		min = e;
	}
	
	if(min > s)
	{
		sel = 's';
		min =s;
		
	}
	
	
	
	//printf("in TOCELL() x=%d y=%d n=%d w=%d s=%d e=%d returned char = %c\n",x,y,n,w,s,e,sel);
	return sel;
}

char fromcell(int x,int y)
{
	char temp;
	//printf("\nIN FROMCELL\n x=%d y=%d",x,y);
	if(x+1 < r)
	{	
		//e = map[x+1][y];
		if(basin[x+1][y]=='0' && 'n' == tocell(x+1,y))
		{
			//printf("\nreturning e\n");
			return 's';
		}
	}
	if(y+1 < c)
	{
		//s = map[x][y+1];
		if(basin[x][y+1]=='0' && 'w' == tocell(x,y+1))
			return 'e';
	}
	if(x-1 >= 0)
	{
		//w = map[x-1][y];
		if(basin[x-1][y] == '0' && 's' == tocell(x-1,y))
			return 'n';
	}
	if(y-1 >= 0)
	{
		//n = map[x][y-1];
		if(basin[x][y-1]=='0' && 'e' == tocell(x,y-1))
			return 'w';
	}
	return '-';
}

void dest(int p,int q)
{
	int flag,new_p=101,new_q =101;
	if(basin[p][q]=='0')
	{
		if(p!= 101 && q!= 101)
		{
			basin[p][q] = alp;
			count++;
			//printf("\n p=%d q=%d",p,q);
			rep:
			char a = fromcell(p,q);
		//	printf("\t a=%c\n",a);
			flag=0;
			switch(a)
			{
				case 'n': 	{
								
								new_p = p-1;
								new_q = q;
								flag =1;
								break;
							}
				case 'w':	{
								new_p = p;
								new_q = q-1;
								flag =1;
								break;
							}
				case 's':	{
								new_p =p+1;
								new_q = q;
								flag =1;
								break;
							}
				case 'e':	{
								new_p = p;
								new_q = q+1;
								flag =1;
								break;
							}
				default:	{
								new_p = 101;
								new_q = 101;
								break;
							}
			}
		//	printf("calling dest again\n");
			dest(new_p,new_q);
			if(flag==1)
			{
				//printf("\n\n YOYOYOOYOYOYOYOYOYOYO \n\n");
				goto rep;
			}
			
			
			char b = tocell(p,q);
			//printf("\t b=%c\n",b);
			switch(b)
			{
				case 'n': 	{
								new_p = p-1;
								new_q = q;
								break;
							}
				case 'w':	{
								new_p = p;
								new_q = q-1;
								break;
							}
				case 's':	{
								new_p =p+1;
								new_q = q;
								break;
							}
				case 'e':	{
								new_p = p;
								new_q = q+1;
								break;
							}
				default:	{
								new_p = 101;
								new_q = 101;
								break;
							}
			}
			dest(new_p,new_q);
		}
	}
}

int main()
{
	freopen("blarge.in","r",stdin);
	freopen("yoyo.txt","w",stdout);

	int num;
	int i,j,casenum;
	//printf("%c\n",++alp);
	scanf("%d",&num);
	//printf("START\n");
	for(casenum = 1;casenum<=num;casenum++)
	{
		alp = 'a'-1;
		count =0;
		scanf("%d",&r);
		scanf("%d",&c);
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				scanf("%d",&map[i][j]);
				basin[i][j] = '0';
				//printf("%d ",map[i][j]);
			}
			//printf("\n");
		}
		int tot = r*c;
	//	while(count<=tot)
	//	{
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
				{
					
					if(basin[i][j] == '0')
					{
					//printf("calling dest");
						alp++;
					//	printf("\n\n ALPHABET IS NOW %c",alp);
						dest(i,j);
					}
				}
			}
	//	}
		//}
		printf("Case #%d:\n",casenum);
		for(i=0;i<r;i++)
		{
			//printf("\n");
			for(j=0;j<c;j++)
			{
				printf("%c ",basin[i][j]);
			}
			if((casenum !=num) || (i!= r-1)) 
				printf("\n");
		}
	}
	return 0;
}
