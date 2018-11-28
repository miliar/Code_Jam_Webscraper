#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>

using namespace std;

string xwon ="X won";
string owon ="O won";
string draw ="Draw";
string incmp ="Game has not completed";


int main()
{

	int T,t;
	cin>>T;
	int i,j;
	for(t=1;t<=T;t++)
	{
	string a[4];
	int xT,yT;
	bool xw=false;
	bool yw=false;
	bool dr=false;
	bool inc=false;
	
	for(i=0;i<4;i++)
		cin>>a[i];
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(a[i][j]=='T')
			{
				xT=i;
				yT=j;
			}
	//Has X won
	a[xT][yT]='X';
	for(i=0;i<4;i++)
		if(a[i][0]=='X' && a[i][1]=='X' && a[i][2]=='X' && a[i][3]=='X')
		{
			xw=true;
			break;
		}
		
	for(i=0;i<4;i++)
		if(a[0][i]=='X' && a[1][i]=='X' && a[2][i]=='X' && a[3][i]=='X')
		{
			xw=true;
			break;
		}
	
	if(a[0][0]=='X' && a[1][1]=='X' && a[2][2]=='X' && a[3][3]=='X')
		{
			xw=true;
		}
	if(a[0][3]=='X' && a[1][2]=='X' && a[2][1]=='X' && a[3][0]=='X')
		{
			xw=true;
		}
		
	if(xw){
		cout<<"Case #"<<t<<": "<<xwon<<endl;
		continue;
	}
	
	
	//Has Y won
	a[xT][yT]='O';
	for(i=0;i<4;i++)
		if(a[i][0]=='O' && a[i][1]=='O' && a[i][2]=='O' && a[i][3]=='O')
		{
			yw=true;
			break;
		}
		
	for(i=0;i<4;i++)
		if(a[0][i]=='O' && a[1][i]=='O' && a[2][i]=='O' && a[3][i]=='O')
		{
			yw=true;
			break;
		}
	
	if(a[0][0]=='O' && a[1][1]=='O' && a[2][2]=='O' && a[3][3]=='O')
		{
			yw=true;
		}
	if(a[0][3]=='O' && a[1][2]=='O' && a[2][1]=='O' && a[3][0]=='O')
		{
			yw=true;
		}
		
	if(yw){
		cout<<"Case #"<<t<<": "<<owon<<endl;
		continue;
	}
	
	// Game not completed
	a[xT][yT]='T';
	
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(a[i][j]=='.')
				inc = true;
	if(inc){
		cout<<"Case #"<<t<<": "<<incmp<<endl;
		continue;
	}
	
	cout<<"Case #"<<t<<": "<<draw<<endl;
	}
return 0;
}	
