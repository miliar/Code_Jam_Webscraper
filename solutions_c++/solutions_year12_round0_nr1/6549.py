#include<iostream.h>
#include<stdio.h>
#include<ctype.h>
#include<conio.h>
void convert(char s[100])
{
	char a[26] = {121, 104, 101, 115, 111, 99, 118, 120, 100, 117, 105, 103, 108, 98, 107, 114, 122, 116, 110, 119, 106, 112, 102, 109, 97, 113};
	int temp = 0;
	for(int i = 0;s[i] != '\0';i++)
	{
		if(s[i] != ' '){
			temp = toascii(s[i]) - 97;
			s[i] = a[temp];
		}
	}
}
void main()
{
	clrscr();


	char tests[100][100];
	int n;
	cin>>n;
	for(int j = 0; j < n; j++)
	{
		gets(tests[j]);
	}
	for(int i = 0;i<n;i++)
	{
		convert(tests[i]);
	}
	for(int k = 0;k < n; k++)
	{
		cout<<"Case #"<<k+1<<": ";
		cout<<tests[k]<<endl;
	}
	getch();
}
