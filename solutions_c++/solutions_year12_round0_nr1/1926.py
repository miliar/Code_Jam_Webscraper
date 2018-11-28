#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

const char Turn[]="yhesocvxduiglbkrztnwjpfmaq";
 

void Solve(int TestNo)
{
	char str[1000];
	gets(str);
	int len=strlen(str);
	for (int i=0;i<len;++i)
		if ('a'<=str[i]&&str[i]<='z')
			str[i]=Turn[str[i]-'a'];
	printf("Case #%d: %s\n",TestNo,str);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d\n",&T);
	for (int i=1;i<=T;++i)
		Solve(i);
	return 0;
}

