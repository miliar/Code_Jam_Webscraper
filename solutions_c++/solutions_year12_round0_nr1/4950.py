#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<string.h>
#include<map>
#include<vector>
#define MAX 1111

using namespace std;

string map1 = "yhesocvxduiglbkrztnwjpfmaq";
char s[MAX];
char outs[MAX];

void solve()
{
    int len = strlen(s);

    for(int i=0;i<len;i++)
    {
            if(s[i]==' ')
            {
                outs[i] = ' ';
            }
            else
            {
                int val = s[i]-'a';
                outs[i] = map1[val];
            }
    }
    outs[len] = '\0';
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w+", stdout);
    int cases;
	scanf("%d\n",&cases);

	for(int i=1;i<=cases;i++)
	{
        gets(s);
        solve();
        printf("Case #%d: %s\n",i,outs);
	}

    return 0;
}

