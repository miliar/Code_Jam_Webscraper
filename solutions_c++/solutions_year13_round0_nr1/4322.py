#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int t;
	// while(1)
	// {
	// 	char a;
	// 	scanf("%c%*c",&a);
	// 	printf("%c\t%d\n",a,a);
	// }
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		vector<string> v;
		string s;
		for(int i=0;i<4;i++)
		{
			cin>>s>>ws;
			v.push_back(s);
		}
		cin>>ws;
		vector<int> sum;
		for(int i=0;i<4;i++)
		{
			int a=0;
			for(int j=0;j<4;j++)
			{
				a+=v[i][j];
			}
			//printf("a=%d\n",a);
			sum.push_back(a);
		}
		for(int i=0;i<4;i++)
		{
			int a=0;
			for(int j=0;j<4;j++)
			{
				a+=v[j][i];
			}
			//printf("a=%d\n",a);
			sum.push_back(a);
		}
		int a=0;
		for(int i=0;i<4;i++)
		{
			a+=v[i][i];
		}
		//printf("a=%d\n",a);
		sum.push_back(a);
		a=0;
		for(int i=0;i<4;i++)
		{
			a+=v[i][3-i];
		}
		//printf("a=%d\n",a);
		sum.push_back(a);
		char w = 0;
		for(int i=0;i<sum.size();i++)
		{
			if(sum[i]==348||sum[i]==352)
			{
				w='X';
				break;
			}
			else if(sum[i]==321||sum[i]==316)
			{
				w='O';
				break;
			}
		}
		if(w==0)
		{
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
				{
					if(v[i][j]=='.')
						w='N';
				}
		}
		printf("Case #%d: ",c);
		if(w==0)
		{
			printf("Draw\n");
		}
		else if(w=='N')
		{
			printf("Game has not completed\n");
		}
		else if(w=='X')
		{
			printf("X won\n");
		}
		else if(w=='O')
		{
			printf("O won\n");
		}
	}
}