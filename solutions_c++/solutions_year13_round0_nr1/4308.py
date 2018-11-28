#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
		freopen("A-large.in","r",stdin);
		freopen("output.txt","w",stdout);

	int t,j,i,k,p,dots,flag;
	char s[10][10];
	scanf("%d",&t);
	t=t+1;
	string dummy,s1[5];
	getline(cin,dummy);
	for(p=1;p<=t;p++)
	{
		
		 dots=0; flag=0;
		int x_r[5],o_r[5],t_r[5],x_c[5],o_c[5],t_c[5],x_d1=0,o_d1=0,t_d1=0,x_d2=0,o_d2=0,t_d2=0;
		for(i=1;i<=5;i++)
		{
			x_r[i]=0; o_r[i]=0; t_r[i]=0; x_c[i]=0; o_c[i]=0; t_c[i]=0; 
		}
		for(i=1;i<=4;i++)
		{
			cin>>s1[i];
		}
		for(i=1;i<=4;i++)
		{
			for(j=0;j<4;j++)
			{
				s[i][j+1]=s1[i][j];
				if(s[i][j+1]=='X')
				x_r[i]++;
				else if(s[i][j+1]=='O')
				o_r[i]++;
				else if(s[i][j+1]=='T')
				t_r[i]++;
				else if(s[i][j+1]=='.')
				dots++;
			}
		}
	
		for(j=1;j<=4;j++)
		{
			for(i=1;i<=4;i++)
			{
				if(s[i][j]=='X')
				x_c[j]++;
				else if(s[i][j]=='O')
				o_c[j]++;
				else if(s[i][j]=='T')
				t_c[j]++;
			}
		}
	
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(i==j)
				{
					if(s[i][j]=='X')
					x_d1++;
					else if(s[i][j]=='O')
					o_d1++;
					else if(s[i][j]=='T')
					t_d1++;
				}
				if(i+j==5)
				{
					if(s[i][j]=='X')
					x_d2++;
					else if(s[i][j]=='O')
					o_d2++;
					else if(s[i][j]=='T')
					t_d2++;
				}
			}
		}
		int fl=0;
		for(i=1;i<=4;i++)
		{
			if((x_r[i]==4 || (x_r[i]==3 && t_r[i]==1))&&fl==0)
			{ printf("Case #%d: X won\n",p); flag=1;fl=1; }
			else if((o_r[i]==4 || (o_r[i]==3 && t_r[i]==1))&&fl==0)
			{ printf("Case #%d: O won\n",p); flag=1; fl=1; }
			else if((x_c[i]==4 || (x_c[i]==3 && t_c[i]==1))&&fl==0)
			{ printf("Case #%d: X won\n",p); flag=1;fl=1; }
			else if((o_c[i]==4 || (o_c[i]==3 && t_c[i]==1))&&fl==0)
			{ printf("Case #%d: O won\n",p); flag=1;fl=1; }
		}
		if((x_d1==4 || (x_d1==3 && t_d1==1))&&fl==0)
		{ printf("Case #%d: X won\n",p); flag=1; }
		else if((o_d1==4 || (o_d1==3 && t_d1==1))&&fl==0)
		{ printf("Case #%d: O won\n",p); flag=1; }
		
		else if((x_d2==4 || (x_d2==3 && t_d2==1))&&fl==0)
		{ printf("Case #%d: X won\n",p); flag=1; }
		else if((o_d2==4 || (o_d2==3 && t_d2==1))&&fl==0)
		{ printf("Case #%d: O won\n",p); flag=1; }
		
		else if(dots>0 && flag==0&&fl==0)
		printf("Case #%d: Game has not completed\n",p);
		else if(dots==0 && flag==0&&fl==0) 
		printf("Case #%d: Draw\n",p);
					
		
	}
	return 0;
}
