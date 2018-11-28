#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

main()
{
	int t, i, j;
	char g[101];
	char c;
	char lookup[]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	cin>>t;
	while((c=getchar())!='\n');
	for(i=0; i<t; i++)
	{
		gets(g);
		cout<<"Case #"<<(i+1)<<": ";
		for(j=0; j<strlen(g); j++)
		{
			if(g[j]==' ')
				cout<<" ";
			else
				cout<<lookup[g[j]-'a'];
		}
		cout<<endl;
	}
}
