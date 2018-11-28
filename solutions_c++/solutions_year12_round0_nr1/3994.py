# include <cstdio>
# include <iostream>
# include <algorithm>
# include <vector>
# include <cstring>
# include <cctype>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <string>

using namespace std;

char convert[]="yhesocvxduiglbkrztnwjpfmaq";
char inp[1000];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		do
		{
			cin.getline(inp,1000);
		}while(strlen(inp)==0);
		printf("Case #%d: ",t);
		for(int i=0;inp[i];i++)
			if(isalpha(inp[i]))printf("%c",convert[inp[i]-'a']);
			else printf("%c",inp[i]);
		printf("\n");
	}
	return 0;
}
