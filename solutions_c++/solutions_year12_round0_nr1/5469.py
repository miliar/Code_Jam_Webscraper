#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<cstring>
using namespace std;
int main()
{
	int cases;int k=1;
	char array[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	scanf("%d",&cases);
	char ch=getchar();
	while(cases--)
	{
		string g="";
		getline(cin,g);
		string s="";
		for(int i=0;i<g.length();i++)
			if(g[i]==' ') s+=' ';
			else s+=array[g[i]-'a'];
		cout<<"Case #"<<k<<": "<<s<<endl;
		k++;
	}
	return 0;
}
		
		