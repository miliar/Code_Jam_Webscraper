#include <iostream>
#include <algorithm>
using namespace std;

int n;
char s[100];

int main()
{
		freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int c;
	scanf("%d",&n);
	for(c=1;c<=n;c++)
	{
		//char tmp[100];
		printf("Case #%d: ",c);
		scanf("%s",s);
		
		if(next_permutation(s,s+strlen(s)))
			printf("%s\n",s);
		else
		{
			while(s[0]=='0') next_permutation(s,s+strlen(s));
			printf("%c",s[0]);
			printf("0");
			int i;
			for(i=1;i<strlen(s);i++)
				printf("%c",s[i]);
			printf("\n");
		}
	}
	return 0;
}