#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    //char x[26] = "ynficwlbkuomxsevpdrjgthaq";
    char x[27] = "yhesocvxduiglbkrztnwjpfmaq";
    int n;
    scanf("%d", &n);
    getchar();
    for(int i=1; i<=n; i++)
    {
	string s;
	getline(cin, s);
	printf("Case #%d: ", i);
	for(int i=0; i<s.size(); i++)
	    printf("%c", s[i] != ' ' ? x[s[i]-'a'] : ' ');
	printf("\n");
    }
    return 0;
}

