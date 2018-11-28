#include<iostream.h>
#include<conio.h>

char a[4][4];
int check(char c,char c2)
{
	if(((a[0][0]==c)||(a[0][0]==c2))&&((a[0][1]==c)||(a[0][1]==c2))&&((a[0][2]==c)||(a[0][2]==c2))&&((a[0][3]==c)||(a[0][3]==c2)))
		return 1;
	if(((a[1][0]==c)||(a[1][0]==c2))&&((a[1][1]==c)||(a[1][1]==c2))&&((a[1][2]==c)||(a[1][2]==c2))&&((a[1][3]==c)||(a[1][3]==c2)))
		return 1;
	if(((a[2][0]==c)||(a[2][0]==c2))&&((a[2][1]==c)||(a[2][1]==c2))&&((a[2][2]==c)||(a[2][2]==c2))&&((a[2][3]==c)||(a[2][3]==c2)))
		return 1;
	if(((a[3][0]==c)||(a[3][0]==c2))&&((a[3][1]==c)||(a[3][1]==c2))&&((a[3][2]==c)||(a[3][2]==c2))&&((a[3][3]==c)||(a[3][3]==c2)))
		return 1;
	
	if(((a[0][0]==c)||(a[0][0]==c2))&&((a[1][1]==c)||(a[1][1]==c2))&&((a[2][2]==c)||(a[2][2]==c2))&&((a[3][3]==c)||(a[3][3]==c2)))
		return 1;
		
	if(((a[0][0]==c)||(a[0][0]==c2))&&((a[1][0]==c)||(a[1][0]==c2))&&((a[2][0]==c)||(a[2][0]==c2))&&((a[3][0]==c)||(a[3][0]==c2)))
		return 1;
	if(((a[0][1]==c)||(a[0][1]==c2))&&((a[1][1]==c)||(a[1][1]==c2))&&((a[2][1]==c)||(a[2][1]==c2))&&((a[3][1]==c)||(a[3][1]==c2)))
		return 1;
	if(((a[0][2]==c)||(a[0][2]==c2))&&((a[1][2]==c)||(a[1][2]==c2))&&((a[2][2]==c)||(a[2][2]==c2))&&((a[3][2]==c)||(a[3][2]==c2)))
		return 1;
	if(((a[0][3]==c)||(a[0][3]==c2))&&((a[1][3]==c)||(a[1][3]==c2))&&((a[2][3]==c)||(a[2][3]==c2))&&((a[3][3]==c)||(a[3][3]==c2)))
		return 1;
		
	return 0;
}

void main()
{	clrscr();
	int t,count=0;
	cin>>t;
	for(int b=1;b<=t;b++)
	{	for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];

	    if(check('.','T'))
		if(check('X','T'))
			cout<<"Case #"<<b<<": "<<"X won\n";
		else if(check('O','T'))
			cout<<"Case #"<<b<<": "<<"O won\n";
		else
			cout<<"Case #"<<b<<": "<<"Game has not completed\n";
	    else if(check('X','T'))
		cout<<"Case #"<<b<<": "<<"X won\n";
	    else if(check('O','T'))
		cout<<"Case #"<<b<<": "<<"O won\n";
	    else
	      { for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			  if(a[i][j]=='.')
			     count++;
		if(count!=0)
		      cout<<"Case #"<<b<<": "<<"Game has not completed\n";
		else
		     cout<<"Case #"<<b<<": "<<"Draw\n";

	      }
	      count=0;
	}
}