#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int a,j,it,T,i,n,k,e,q;
pair <int,int> p[1000000];
char s[100][100];
bool xw,prt;
int main()
{
	 freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin>>T;
	for(it=0;it<T;it++)
	{
		
		prt=false;
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>s[i][j];
		for(i=0;i<4;i++)
		{
			xw=true;
			for(j=0;j<4;j++)
				if(!(s[i][j]=='X' || s[i][j]=='T'))
					{xw=false;
					break;}
			if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": X won"<<endl;
				prt=true;
			}
		}

		for(j=0;j<4;j++)		
		{
				xw=true;
		
				for(i=0;i<4;i++)
					if(!(s[i][j]=='X' || s[i][j]=='T'))
					{xw=false;
					break;}
			if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": X won"<<endl;
				prt=true;
			}
		}


		//ghotri
		xw=true;
		for(j=0;j<4;j++)		
		{
			if(!(s[j][j]=='X' || s[j][j]=='T'))
				{
					xw=false;
					break;
				}	
		}

		if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": X won"<<endl;
				prt=true;
			}
//ghotri oonvari
		xw=true;
		for(j=0;j<4;j++)		
		{
			if(!(s[j][3-j]=='X' || s[j][3-j]=='T'))
					{xw=false;
					break;}
		}
			if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": X won"<<endl;
				prt=true;
			}
		



		///check if O wons
	for(i=0;i<4;i++)
	{
		xw=true;
		for(j=0;j<4;j++)
			if(!(s[i][j]=='O' || s[i][j]=='T'))
			{xw=false;
					break;}
			if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": O won"<<endl;
				prt=true;
			}
		}

		for(j=0;j<4;j++)		
		{
				xw=true;
		
				for(i=0;i<4;i++)
					if(!(s[i][j]=='O' || s[i][j]=='T'))
					{xw=false;
					break;}
			if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": O won"<<endl;
				prt=true;
			}
		}


		//ghotri
		xw=true;
		for(j=0;j<4;j++)		
		{
			if(!(s[j][j]=='O' || s[j][j]=='T'))
					{xw=false;
					break;}
		}
			if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": O won"<<endl;
				prt=true;
			}
		

//ghotri oonvari
		xw=true;
		for(j=0;j<4;j++)		
		{
			if(!(s[j][3-j]=='O' || s[j][3-j]=='T'))
					{xw=false;
					break;}
		}
	if(xw && !prt)
			{
				cout<<"Case #"<<it+1<<": O won"<<endl;
				prt=true;
			}
		

		int sum=0;

		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(s[i][j]=='.')
					sum++;
		if(sum==0 && !prt)
			cout<<"Case #"<<it+1<<": Draw"<<endl;
		
		if(sum!=0 && !prt)
			cout<<"Case #"<<it+1<<": Game has not completed"<<endl;
		
	}
	return 0;
}