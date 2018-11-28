#include<cstdio>
#include<iostream>
#include<string>

using namespace std;

int main()
{
//	freopen("a.txt","r", stdin);
//	freopen("b.txt","w", stdout);
	string t = "abcdefghijklmnopqrstuvwxyz";
	string k1 = "yhesocvxduiglbkrqtnwjpfmaz";
	string k2 = "yhesocvxduiglbkrztnwjpfmaq";
	int n;
	scanf("%d\n", &n);
	for(int i = 1; i <= n;i++)
	{
		printf("Case #%d: ", i);
		char c;
		while(1)
		{
			scanf("%c", &c);
			if(c == '\n')break;
			if(c == ' ')printf(" ");
			else{
			int index = c - 'a';
			printf("%c", k2[index]);
		}
		}
		printf("\n");
	}
	return 0;
}
