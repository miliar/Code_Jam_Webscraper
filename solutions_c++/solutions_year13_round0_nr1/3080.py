#include<iostream>
#include<stdio.h>
using namespace std;
char x[4][4],o[4][4];
int main()
{
	freopen("test.txt","w",stdout);
	//cout<<"Welcome Jayaganesh, u have won GOOGLE CODE JAM";
	int t;
	cin>>t;
	cin.ignore();
	string c;
	int i,j,k;
	for(i=1;i<=t;i++)
	{
		bool completed=true;
		for(j=0;j<4;j++)
		{
			getline(cin,c,'\n');
			for(k=0;k<4;k++)
			{
				if(c[k]=='.')completed=false;
				if(c[k]=='T'){x[j][k]='X';o[j][k]='O';}
				else {x[j][k]=c[k];o[j][k]=c[k];}
				//cout<<o[j][k]<<" ";
			}
			//cout<<endl;
		}
		bool winx=false,wino=false;
		
		if(x[0][0]==x[1][1] && x[1][1]==x[2][2] && x[2][2]==x[3][3] && x[0][0]=='X')winx=true;
		else if(o[0][0]==o[1][1] && o[1][1]==o[2][2] && o[2][2]==o[3][3] && o[0][0]=='O')wino=true;
		for(j=0;j<4;j++)
		{
			if(x[j][0]==x[j][1] && x[j][1]==x[j][2] && x[j][2]==x[j][3] && x[j][0]=='X')winx=true;
			if(o[j][0]==o[j][1] && o[j][1]==o[j][2] && o[j][2]==o[j][3] && o[j][0]=='O')wino=true;
			if(x[0][j]==x[1][j] && x[1][j]==x[2][j] && x[2][j]==x[3][j] && x[0][j]=='X')winx=true;
			if(o[0][j]==o[1][j] && o[1][j]==o[2][j] && o[2][j]==o[3][j] && o[0][j]=='O')wino=true;
		}
		if(x[0][3]==x[1][2] && x[1][2]==x[2][1] && x[2][1]==x[3][0] && x[0][3]=='X')winx=true;
		else if(o[0][3]==o[1][2] && o[1][2]==o[2][1] && o[2][1]==o[3][0] && o[0][3]=='O')wino=true;
		cout<<"Case #"<<i<<": ";
		if(winx==true)cout<<"X won"<<endl;
		else if(wino==true)cout<<"O won"<<endl;
		else if(completed)cout<<"Draw"<<endl;
		else cout<<"Game has not completed"<<endl;
		getline(cin,c,'\n');
	}
}
