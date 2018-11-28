#include<iostream>
using namespace std;
#include<stdio.h>

main()
{
	char *arr = "yhesocvxduiglbkrztnwjpfmaq";
	int t;
	cin>>t;
	char c;
	int count = 1;
	c=getchar();
	while(t--)
	{
	//char s[100];
	//scanf("%[^\n]",s);
	//scanf("%c",&c);
	//gets(s);
	//cout<<s;
	cout<<"Case #"<<count<<": ";
	count++;
	c=getchar();
		
		while(c != '\n')
		{	
			if(c==' ')
			cout<<' ';
			else
				cout<<arr[c-'a'];
		
			c=getchar();
		}
		cout<<endl;
	}
}
