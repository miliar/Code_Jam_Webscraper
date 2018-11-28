#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std; 
int main()	
{
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
		int completed=0;
		int a[4][4]={0};
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			char c;
			cin>>c;
			if(c=='X')
			a[i][j]=1;
			else if(c=='O')
			a[i][j]=2;
			else if(c=='T')
			a[i][j]=-1;		
			}
		int flag=0,countx,counto,countt;
		
		for(int i=0;i<4;i++)
		{
			countx=0;counto=0;countt=0;
			for(int j=0;j<4;j++)
			{
				if(a[i][j]==1)
				countx++;
				else if(a[i][j]==2)
				counto++;
				else if(a[i][j]==-1)
				countt++;
			}
			if(countx==4||countx+countt==4)
			{cout<<"Case #"<<cas<<": X won\n"; completed=1;}
			else if(counto==4||counto+countt==4)
			{cout<<"Case #"<<cas<<": O won\n"; completed=1;}
			else if((countx+counto+countt)==4)
			flag=1;
			else 
			flag=0;
		}
		
		if(completed!=1)
		{
		for(int i=0;i<4;i++)
		{
			countx=0;counto=0;countt=0;
			for(int j=0;j<4;j++)
			{
				if(a[j][i]==1)
				countx++;
				else if(a[j][i]==2)
				counto++;
				else if(a[j][i]==-1)
				countt++;
			}
			if(countx==4||countx+countt==4)
			{cout<<"Case #"<<cas<<": X won\n"; completed=1;}
			else if(counto==4||counto+countt==4)
			{cout<<"Case #"<<cas<<": O won\n"; completed=1;}
			else if((countx+counto+countt)==4)
			flag=1;
			else 
			flag=0;
		}
		}
		
		if(completed!=1)
		{
				countx=0;counto=0;countt=0;
				for(int i=0;i<4;i++)
				{
					if(a[i][i]==1)
					countx++;
					else if(a[i][i]==2)
					counto++;
					else if(a[i][i]==-1)
					countt++;
					}
			if(countx==4||countx+countt==4)
			{cout<<"Case #"<<cas<<": X won\n"; completed=1;}
			else if(counto==4||counto+countt==4)
			{cout<<"Case #"<<cas<<": O won\n"; completed=1;}
			else if((countx+counto+countt)==4)
			flag=1;
			else 
			flag=0;
				
			
			}
			
			
			if(completed!=1)
		{
			
				countx=0;counto=0;countt=0;
				
				for(int i=0;i<4;i++)
				{
					if(a[i][3-i]==1)
					countx++;
					else if(a[i][3-i]==2)
					counto++;
					else if(a[i][3-i]==-1)
					countt++;
					
					}
			if(countx==4||countx+countt==4)
			{cout<<"Case #"<<cas<<": X won\n"; completed=1;}
			else if(counto==4||counto+countt==4)
			{cout<<"Case #"<<cas<<": O won\n"; completed=1;}
			else if((countx+counto+countt)==4)
			flag=1;
			else 
			flag=0;
				
			
			}
			
			if(completed==0&&flag==0)
			cout<<"Case #"<<cas<<": Game has not completed\n";
			
			if(completed==0&&flag==1)
			cout<<"Case #"<<cas<<": Draw\n";
			cas++;
		
	}

    return 0;
}
