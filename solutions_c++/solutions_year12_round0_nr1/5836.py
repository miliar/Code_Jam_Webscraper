#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace::std;

int main()
{
	char Googlerese[26], s[101],g;
	int n,j,len;
	int i = 0;
	
	
	
	cin>>n;
	strcpy(Googlerese,"yhesocvxduiglbkrztnwjpfmaq");
	
	gets(s);

	while(i<n)
	{

		gets(s);
		cout<<"Case #"<<i+1<<": ";
		len = strlen(s);
		for(j=0;j<len;j++)
		{
			g=s[j]-96;
			if(s[j]!=32)
			{	
				if(g>=0)
				{
				cout<<Googlerese[g-1];
				}
			else	
				{
				cout<<g+96;
				}
			}
			else 
			cout<<" ";
				
		}
		cout<<endl;
		i++;	
	}
	
	return(0);
	
}		
