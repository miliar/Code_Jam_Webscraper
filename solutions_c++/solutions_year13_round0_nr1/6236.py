#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int i,j,k,t,te;
	char c,arr[4][4];
	cin>>t;
	for(te=0;te<t;te++)
	{
		for(i=0;i<16;)
		{
			scanf("%c",&c);
			if(c=='.'||c=='T'||c=='X'||c=='O')
				arr[i/4][(i++)%4]=c;
		}
		printf("Case #%d: ",te+1);
		k=0;
		int i3=0;
		for(i=0;i<4;i++)
		{
			int i1=0,i2=0;
			for(j=0;j<4;j++)
			{
				if(arr[i][j]=='X'||arr[i][j]=='T')
					i1++;
				if(arr[j][i]=='X'||arr[j][i]=='T')
					i2++;
			}
			if(i1==4||i2==4)
			{
				k++;
				break;
			}
			if(arr[i][i]=='X'||arr[i][i]=='T')
				i3++;
		}
		if(k==1||i3==4)
		{
			printf("X won");
			continue;
		}
		i3=0;
		for(i=0;i<4;i++)
		{
			int i1=0,i2=0;
			for(j=0;j<4;j++)
			{
				if(arr[i][j]=='O'||arr[i][j]=='T')
					i1++;
				if(arr[j][i]=='O'||arr[j][i]=='T')
					i2++;
			}
			if(i1==4||i2==4)
			{
				k++;
				break;
			}
			if(arr[i][i]=='X'||arr[i][i]=='T')
				i3++;
		}
		if(k==1||i3==4)
		{
			printf("O won");
			continue;
		}
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(arr[i][j]=='.')
					break;
		if(i!=4)
			printf("Game has not completed");
		else
			printf("Draw");
		printf("\n");
	}
	return 0;
}
