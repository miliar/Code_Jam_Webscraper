#include<stdio.h>
#include<string>
#include<memory.h>
#include<math.h>
#include<iostream>
#include<istream>
#include <vector>
#define fi(a,b) for( i = a; i < b ; i++ )
#define fj(a,b) for( j = a; j < b ; j++ )
#define fk(a,b) for( k = a; k < b ; k++ )

using namespace std;

int ri()
	{ int a; 
	  scanf( "%d", &a ); 
	  return a; 
	}
char buff[10000]; 
string rs() 
	{	
		scanf( "%s", buff ); 
		return buff;
	}

typedef vector<int> vi;
typedef vector<char> vc;

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	char arr[30] = "yhesocvxduiglbkrztnwjpfmaq";
	int i=0, j, t;

	scanf("%d",&t);
	string s;
		
	getline(cin,s);
	for(i=0;i<t;i++)
	{
		getline(cin,s);
		j=0;
		while(j<=(s.length()-1))
		{
			if(s[j] == ' ') j++;
			else {
			s[j] = arr[s[j]-'a'];
			j++; }
		}
		printf("Case #%d: %s\n",i+1,s);
	}
}	
		
