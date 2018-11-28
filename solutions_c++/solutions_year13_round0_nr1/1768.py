#include<iostream>
#include<cstdio>
using namespace std;
bool check_win(char a[][4],char who)
{
	for(int i=0;i<4;i++)
	{
		int j;
		for(j=0;j<4;j++)
		{
		//	cout<<a[i][j]<<" "<<who<<endl;
			if(a[i][j]!=who && a[i][j]!='T')break;
		}
		if(j==4)return true;
		for(j=0;j<4;j++)
		{
			if(a[j][i]!=who && a[j][i]!='T')break;
		}
		if(j==4)return true;
	}
	bool flag=true;
	for(int i=0;i<4;i++)
		if(a[i][i]!=who && a[i][i]!='T')flag=false;
	if(flag)return true;
	flag=true;
	for(int i=0;i<4;i++)
		if(a[i][3-i]!=who && a[i][3-i]!='T')flag=false;
	if(flag)return true;
	return false;
}
int main()
{
	char a[4][4];
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		bool xwin=false;
		bool ywin=false;
		bool complete=true;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
				if(a[i][j]=='.')complete=false;
			}
		xwin=check_win(a,'X');
		if(!xwin)
		{
			ywin=check_win(a,'O');
			if(!ywin)
			{
				if(complete)printf("Case #%d: Draw\n",k);
				else printf("Case #%d: Game has not completed\n",k);
			}
			else printf("Case #%d: O won\n",k);
		}
		else printf("Case #%d: X won\n",k);
	}
	return 0;
}
