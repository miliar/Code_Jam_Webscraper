#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<limits.h>
using namespace std;
bool check(char arr[5][5],char ch)
{
 int i=0,j=0,cnt=0;
 for(int i=0;i<4;i++)
 {
	cnt=0;
	for(int j=0;j<4;j++)
	{
		if(arr[i][j]==ch || arr[i][j]=='T')
		cnt++;
	}
	if(cnt==4)
        return true;
 }
 for(int j=0;j<4;j++)
 {
	cnt=0;
	for(int i=0;i<4;i++)
  	{
		if(arr[i][j]==ch || arr[i][j]=='T')
		cnt++;
	}
	if(cnt==4)
	return true;
 }
 cnt=0;
 int cnt2=0;
 for(int i=0;i<4;i++)
 {
	if(arr[i][i]==ch || arr[i][i]=='T')
	cnt++;
	if(arr[i][4-i-1]==ch || arr[i][4-i-1]=='T')
	cnt2++;
 }
 if(cnt==4)
 return true;
 if(cnt2==4)
 return true;
 return false;

}
bool checkDraw(char arr[5][5])
{
  for(int i=0;i<4;i++)
  {
	for(int j=0;j<4;j++)
	{
		if(arr[i][j]=='.')
		return false;
	}
  }
return true;
}
int main()
{
	int n;
	bool X,O,draw,nc;
	X=O=draw=nc=false;
	char arr[5][5];
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{

		for(int j=0;j<4;j++)
			scanf("%s",arr[j]);

	
		X=check(arr,'X');

		if(X)
		{
			printf("Case #%d: X won\n",i+1);

		}
		else {
			O=check(arr,'O');
			if(O)
			{
			printf("Case #%d: O won\n",i+1);
			}
			else 
			{ draw=checkDraw(arr);
				if(draw)
				{
					printf("Case #%d: Draw\n",i+1);
				}
				else  printf("Case #%d: Game has not completed\n",i+1);
			}
		}

	}
}
