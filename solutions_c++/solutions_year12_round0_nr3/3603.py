#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;


int main(void)
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int i,j,k,Length;
	int A,B,T,m;
	string str,Str;
	char str1[10];
	int Count=0;
	cin>>T;
	for (i=0;i<T;i++)
	{
		Count=0;
		cin>>A;
		cin>>B;
		for ( j=A; j<B; j++ )
		{

			itoa (j,str1,10);
			str=str1;
			Length=strlen(str.c_str());		
			for ( k=1; k<Length; k++ )
			{
				
				Str=str.substr(k,Length-k)+str.substr(0,k);
				m = atoi (Str.c_str());
				if ( m>j && m<=B)
					Count +=1;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<Count<<endl;
		
	}
	
	return 0;
}