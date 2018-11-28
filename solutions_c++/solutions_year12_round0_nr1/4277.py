#include<stdio.h>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<sstream>
#include<queue>
#include<math.h>
#include<iostream>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char m[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char str[111] , res[111] ;
	int t;
	scanf("%d\n",&t);
	for ( int tc=1 ; tc<=t ; tc++ )
	{
		gets(str);
		res[strlen(str)]='\0';
		for(int i=0 ; i<strlen(str) ; i++)
		{
			if(str[i]==' ')	res[i]=str[i];
			else	res[i]=m[str[i]-'a'];
		}
		cout << "Case #" << tc << ": " << res << endl;
	}
	//while(1);
}