#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int t;
string s, g;
char tab[26]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
int main()
{
	scanf("%d", &t);
	getline(cin, s);
	for(int i=1; i<=t; i++)
	{
		getline(cin, s);
	//	cout<<s<<"\n";
		printf("Case #%d: ", i);
		for(int i=0; i<s.length(); i++)
		{
			if(s[i]==32){printf(" ");continue;}
			printf("%c", tab[s[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}
