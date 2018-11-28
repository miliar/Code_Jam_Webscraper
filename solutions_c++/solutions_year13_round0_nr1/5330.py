#include<cstdio>

int main()
{
	int t;
	int i,j,k;
	char g[10][10];
	int res;//0:x, 1:o, 2:draw, 3:gnc
	scanf("%d",&t);
	int s[10][290]={0};
	for(i=1;i<=t;i++)
	{
		
		for(j=0;j<10;j++)
			s[j]['X']=s[j]['O']=s[j]['T']=s[j]['.']=0;
		
		
		for(j=0;j<4;j++)
		{
			scanf(" %[^\n]",&g[j]);
			//printf("%s#\n",g[j]);
			for(k=0;k<4;k++)
				s[j][g[j][k]]+=1;
		}
		
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
				s[j+4][g[k][j]]+=1;
			s[8][g[j][j]]+=1;
			s[9][g[j][3-j]]+=1;
		}
		
		res=2;
		for(j=0;j<10;j++)
		{
			if( (s[j]['X']==4) || (s[j]['X']+s[j]['T']==4) )
			{	res=0;break;}
			else if( (s[j]['O']==4) || (s[j]['O']+s[j]['T']==4) )
			{	res=1;break;}
			else if( s[j]['.'] )
			{	res=3;}
		}
		
		if(res==0)
			printf("Case #%d: X won\n",i);
		else if(res==1)
			printf("Case #%d: O won\n",i);
		else if(res==2)
			printf("Case #%d: Draw\n",i);
		else
			printf("Case #%d: Game has not completed\n",i);
		
	}
}
