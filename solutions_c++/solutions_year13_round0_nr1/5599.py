#include<iostream>
#include<math.h>
#include<stdlib.h>
using namespace std;

int main()
{
char b[4][4];
int ans[1002],i;
int T,flag=0;
cin>>T;
for(i=0;i<T;i++)
{
	for(int j=0;j<4;j++)
	for(int k=0;k<4;k++)
	cin>>b[j][k];

	for(int j=0;j<4;j++)
	{
		if((b[j][0]=='X'||b[j][0]=='T')&&(b[j][1]=='X'||b[j][1]=='T')&&(b[j][2]=='X'||b[j][2]=='T')&&(b[j][3]=='X'||b[j][3]=='T'))
		{ans[i]=1;break;}
		else if((b[j][0]=='O'||b[j][0]=='T')&&(b[j][1]=='O'||b[j][1]=='T')&&(b[j][2]=='O'||b[j][2]=='T')&&(b[j][3]=='O'||b[j][3]=='T'))
		{ans[i]=2;break;}
		else if((b[0][j]=='X'||b[0][j]=='T')&&(b[1][j]=='X'||b[1][j]=='T')&&(b[2][j]=='X'||b[2][j]=='T')&&(b[3][j]=='X'||b[3][j]=='T'))
		{ans[i]=1;break;}
		else if((b[0][j]=='O'||b[0][j]=='T')&&(b[1][j]=='O'||b[1][j]=='T')&&(b[2][j]=='O'||b[2][j]=='T')&&(b[3][j]=='O'||b[3][j]=='T'))
		{ans[i]=2;break;}
		else if((b[0][0]=='X'||b[0][0]=='T')&&(b[1][1]=='X'||b[1][1]=='T')&&(b[2][2]=='X'||b[2][2]=='T')&&(b[3][3]=='X'||b[3][3]=='T'))
		{ans[i]=1;break;}
		else if((b[0][0]=='O'||b[0][0]=='T')&&(b[1][1]=='O'||b[1][1]=='T')&&(b[2][2]=='O'||b[2][2]=='T')&&(b[3][3]=='O'||b[3][3]=='T'))
		{ans[i]=2;break;}
		else if((b[0][3]=='X'||b[0][3]=='T')&&(b[1][2]=='X'||b[1][2]=='T')&&(b[2][1]=='X'||b[2][1]=='T')&&(b[3][0]=='X'||b[3][0]=='T'))
		{ans[i]=1;break;}
		else if((b[0][3]=='O'||b[0][3]=='T')&&(b[1][2]=='O'||b[1][2]=='T')&&(b[2][1]=='O'||b[2][1]=='T')&&(b[3][0]=='O'||b[3][0]=='T'))
		{ans[i]=2;break;}
	}
	if((ans[i]!=1)&&(ans[i]!=2))
	{
		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		{if(b[j][k]=='.')ans[i]=3;}
		
		if(ans[i]!=3)
		ans[i]=4;
	}	
}

for(i=0;i<T;i++)
{
if(ans[i]==3)
cout<<"Case #"<<(i+1)<<": "<<"Game has not completed"<<"\n";
else if(ans[i]==1)
cout<<"Case #"<<(i+1)<<": "<<"X won"<<"\n";
else if(ans[i]==2)
cout<<"Case #"<<(i+1)<<": "<<"O won"<<"\n";
else
cout<<"Case #"<<(i+1)<<": "<<"Draw"<<"\n";
}
return 0;
}
