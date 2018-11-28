#include<string.h>
#include<iostream.h>
#include<stdio.h>
#include<conio.h>
void main()
{
	clrscr();
	char a[30][100];
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		gets(a[i]);
	}
	char convert[]="yhesocvxduiglbkrztnwjpfmaq";
	for(i=0;i<n;i++)
	{
		for(int j=0;j<strlen(a[i]);j++)
		{
			int x = int(a[i][j])-97;
			if(x!=-65)
			a[i][j] = convert[x];
		}
	}
	for(i=0;i<n;i++)
	{
		cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
	}
	getch();
}