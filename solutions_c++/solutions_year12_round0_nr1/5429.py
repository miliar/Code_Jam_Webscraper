#include<iostream>
#include<string>
using namespace std;
int main()
{
	char *c;
	int i,j;
	cin>>i;
	c=new char[110];
	cin.get();
	for(j=0;j<i;j++)
	{
		c=new char[110];
		cin.getline(c,110);
		int k=0;
		cout<<"Case #"<<j+1<<": ";
		while(c[k]!='\0')
		{
			switch(c[k])
			{
			
				case 'a': cout<<'y'; break;
				case 'b': cout<<'h'; break;
				case 'c': cout<<'e'; break;
				case 'd': cout<<'s'; break;
				case 'e': cout<<'o'; break;
				case 'f': cout<<'c'; break;
				case 'g': cout<<'v'; break;
				case 'h': cout<<'x'; break;
				case 'i': cout<<'d'; break;
				case 'j': cout<<'u'; break;
				case 'k': cout<<'i'; break;
				case 'l': cout<<'g'; break;
				case 'm': cout<<'l'; break;
				case 'n': cout<<'b'; break;
				case 'o': cout<<'k'; break;
				case 'p': cout<<'r'; break;
				case 'q': cout<<'z'; break;
				case 'r': cout<<'t'; break;
				case 's': cout<<'n'; break;
				case 't': cout<<'w'; break;
				case 'u': cout<<'j'; break;
				case 'v': cout<<'p'; break;
				case 'w': cout<<'f'; break;
				case 'x': cout<<'m'; break;
				case 'y': cout<<'a'; break;
				case 'z': cout<<'q'; break;
				default: cout<<c[k];
			}
			k++;
		}
	
		cout<<endl;
	}
	
	return 0;

}
