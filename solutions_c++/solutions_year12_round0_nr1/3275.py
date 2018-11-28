#include<cstdio>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	int n;
	char tab[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	scanf("%d\n",&n);
	for(int i=0; i<n; i++)
	{
		string str;
		getline(cin,str);
		printf("Case #%d: ",i+1);
		for(int j=0; j<str.length(); j++)
		{
			if(str[j]!=' ')
				printf("%c",tab[str[j]-97]); else
				printf("%c",32);
		}
		cout<<"\n";
	//	cout<<str;
	}
	//system("pause");
	return 0;
}