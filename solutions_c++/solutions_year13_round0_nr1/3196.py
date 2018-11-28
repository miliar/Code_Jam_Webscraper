#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;
int map[6][6];
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("out.txt","w",stdout);
	int f, n,i,j,dian,time=1,x,o,t;
	cin>>n;
	char ch;
	while(n--)
	{
		f=2;dian=0;x=o=0;
		memset(map,-1,sizeof(map));
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>ch;
				if(ch=='O')map[i][j]=0;
				else if(ch=='.'){map[i][j]=3;dian=1;}
				else if(ch=='X'){map[i][j]=1;x++;}
				else if(ch=='T'){map[i][j]=5;o++;}
			}
		}
/*for(i=1;i<=4;i++)
	for(j=1;j<=4;j++)
	{
		cout<<map[i][j]<<" ";
		if(j==4)cout<<endl;
	}
*/
	//	cout<<x<<" "<<o<<" "<<dian<<endl;
	//	if(x<3&&o<3){printf("Case #%d: Draw\n",time++);continue;}
		

		for(i=1;i<=4;i++)
		{	x=o=t=0;
			for(j=1;j<=4;j++)
			{
				if(map[i][j]==0)o++;
				if(map[i][j]==1)x++;
				if(map[i][j]==5)t++;
			}	
			if(o>0&&x>0);
			else if(o==4||(o==3&&t==1))f=0;
			else if(x==4||(x==3&&t==1))f=1;
			
		}
	
	//	cout<<i<<endl;
	
		
			for(j=1;j<=4;j++)
			{	x=o=t=0;
				for(i=1;i<=4;i++)
				{
				if(map[i][j]==0)o++;
				if(map[i][j]==1)x++;
				if(map[i][j]==5)t++;
				}	
			
				if(o>0&&x>0);
				else if(o==4||(o==3&&t==1))f=0;
				else if(x==4||(x==3&&t==1))f=1;
			}
	
		if(f!=0&&f!=1)
		{
			t=o=x=0;
			for(i=1,j=1;i<=4;i++,j++)
			{	
				if(map[i][j]==0)o++;
				if(map[i][j]==1)x++;
				if(map[i][j]==5)t++;
			}
			
			if(o>0&&x>0);
			else if(o==4||(o==3&&t==1))f=0;
			else if(x==4||(x==3&&t==1))f=1;
			t=x=o=0;
			for(i=4,j=1;i>=1;i--,j++)
			{
				if(map[i][j]==0)o++;
				if(map[i][j]==1)x++;
				if(map[i][j]==5)t++;
			}
			if(o>0&&x>0);
			else if(o==4||(o==3&&t==1))f=0;
			else if(x==4||(x==3&&t==1))f=1;
		
		}
		if(f==1)
			printf("Case #%d: X won\n",time++);
		else if(f==0)
			printf("Case #%d: O won\n",time++);
		else if(dian==0)
			printf("Case #%d: Draw\n",time++);		
		else printf("Case #%d: Game has not completed\n",time++);

	}return 0;
}
