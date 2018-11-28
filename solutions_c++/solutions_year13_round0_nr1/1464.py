#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <cmath>
#include <cstring>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	char a[4][4];
	for(int iter=0;iter<T;iter++)
	{
		for(int i=0;i<4;i++)
			scanf("%s",a[i]);
		int flag=0,cnt=0,cl=0;
		for(int i=0;i<4 && flag==0;i++)
		{
			int count=0,f=0;			
			for(int j=0;j<4;j++)
			{
				if(a[i][j]=='O')
					count++;
				else if(a[i][j]=='X')
					count--;				
				else if(a[i][j] == 'T')
					f=1;
				else
				{
					cl=1;
					break;
				}
			}
			if(count==4 ||(count==3 && f==1))
				flag=1;
			else if(count==-4 || (count==-3 && f==1))
				flag=2;
		}
		for(int i=0;i<4 && flag==0;i++)
		{
			int count=0,f=0;			
			for(int j=0;j<4;j++)
			{
				if(a[j][i]=='O')
					count++;
				else if(a[j][i]=='X')
					count--;				
				else if(a[j][i] =='T')
					f=1;
				else
					break;

			}
			if(count==4 ||(count==3 && f==1))
				flag=1;
			else if(count==-4 || (count==-3 && f==1))
				flag=2;
		}
		int count=0,f=0;
		for(int i=0;i<4 && flag==0;i++)
		{
			
			if(a[i][i]=='O')
				count++;
			else if(a[i][i]=='X')
				count--;				
			else if(a[i][i] =='T')
				f=1;
			else
				break;
		}
		if(count==4 ||(count==3 && f==1))
			flag=1;
		else if(count==-4 || (count==-3 && f==1))
			flag=2;
		count=0,f=0;
		for(int i=0;i<4 && flag==0;i++)
		{
			
			if(a[i][3-i]=='O')
				count++;
			else if(a[i][3-i]=='X')
				count--;				
			else if(a[i][3-i] =='T')
				f=1;
			else
				break;
		}
		if(count==4 ||(count==3 && f==1))
			flag=1;
		else if(count==-4 || (count==-3 && f==1))
			flag=2;
		printf("Case #%d: ",iter+1);		
		if(flag==1)
			printf("O won\n");
		else if(flag==2)
			printf("X won\n");
		else if(cl==0)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
}
