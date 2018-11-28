#include <iostream>
#include <conio.h>
using namespace std;

char a[4][4];
char A[4];

void input(void);
int findwinner(void);
bool xChecker(char c[4]);
bool yChecker(char c[4]);
bool gChecker(void);

void main()
{
	int index;
	cin>>index;
	int *res=new int[index];
	int counter=0;
	while(counter<index)
	{
		//if(counter>0)
		//	cout<<endl;
		input();
		res[counter]=findwinner();
		counter++;
	}
	for(int i=0;i<index;i++)
	{
		if(i>0)
			cout<<endl;
		cout<<"Case #"<<i+1<<": ";
		if(res[i]==1)
			cout<<"X won";
		else if(res[i]==2)
			cout<<"O won";
		else if(res[i]==3)
			cout<<"Game has not completed";
		else
			cout<<"Draw";
	}
}
//****************************************
void input()
{
	int i,j,k;
	for(i=0;i<4;i++)
	{
		cin>>A;
		for(j=0;j<4;j++)
			a[i][j]=A[j];
	}
}
//*****************************************
int findwinner()
{
char c[4];
int i,j;

for(i=0;i<4;i++)
{
	for(j=0;j<4;j++)
		c[j]=a[i][j];
	if(xChecker(c)==true)
		return 1;
	else if(yChecker(c)==true)
		return 2;
	//else
	//	return 4;
}

for(j=0;j<4;j++)
{
	for(i=0;i<4;i++)
		c[i]=a[i][j];
	if(xChecker(c)==true)
		return 1;
	else if(yChecker(c)==true)
		return 2;
	//else
	//	return 4;
}

for(i=0;i<4;i++)
{
	j=i;
	c[j]=a[i][j];
}
	if(xChecker(c)==true)
		return 1;
	else if(yChecker(c)==true)
		return 2;
	//else
	//	return 4;

for(i=0;i<4;i++)
{
	j=3-i;
	c[j]=a[i][j];
}
	if(xChecker(c)==true)
		return 1;
	else if(yChecker(c)==true)
		return 2;
	//else
		//return 4;

if(gChecker()==true)
		return 3;
return 4;
}
//*****************************
bool xChecker(char c[4])
{
	if( (c[0]=='X' || c[0]=='T') && (c[1]=='X' || c[1]=='T') && (c[2]=='X' || c[2]=='T') && (c[3]=='X' || c[3]=='T') )
		return true;
	return false;
}
//***************************
bool yChecker(char c[4])
{
	if( (c[0]=='O' || c[0]=='T') && (c[1]=='O' || c[1]=='T') && (c[2]=='O' || c[2]=='T') && (c[3]=='O' || c[3]=='T') )
		return true;
	return false;
}
//***************************
bool gChecker()
{
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(a[i][j]=='.')
				return true;
	return false;
}