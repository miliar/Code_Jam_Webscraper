#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<fstream.h>
void main()
{
	clrscr();
	int t;
	cin>>t;
	ofstream myfile;
	myfile.open ("example.txt");
	char a[26]={"abcdefghijklmnopqrstuvwxyz"},b[26]={"ynficwlbkuomxsevzpdrjgthaq"},c[1000]={NULL};
	for(int k=0;k<t;k++)
	{
		gets(c);
		for(int i=0;i<strlen(c);i++)
		{
			for(int j=0;j<26;j++)
			{
				if(c[i]==b[j])
				{
					c[i]=a[j];
					break;
				}
			}
		}
		myfile<<"Case #"<<k+1<<": "<<c<<endl;
	}
	getch();
}