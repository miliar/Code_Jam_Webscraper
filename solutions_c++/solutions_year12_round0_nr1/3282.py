#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int r;
	//////////// a   b
	char c[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	scanf("%d",&r);
	string tmp;
	getline(cin,tmp);
	for(int rd=1;rd<=r;rd++)
	{
		string str;
		getline(cin,str);
		printf("Case #%i: ",rd);
		for(int i=0;i<str.length();i++)
		{
			if(str[i]>='a'&&str[i]<='z')
				printf("%c",c[str[i]-'a']);
			else
				printf("%c",str[i]);
		}
		printf("\n");
	}
	return 0;
}
