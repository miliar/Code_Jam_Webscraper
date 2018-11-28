#if(1)
#include<stdio.h>
#include<string.h>

int main()
{
	int delta[26]={-24,-6,-2,-15,-10,3,-15,-16,5,-11,2,5,1,12,4,-2,-9,-2,5,-3,11,6,17,11,24,9};
	int N;
	//freopen("out.txt","w",stdout);
	//freopen("in.txt","r",stdin);
	scanf("%d",&N);
	char s[2]={};
	gets(s);
	for(int j=0;j<N;j++)
	{
		char s1[102]={};
		gets(s1);
		int n=strlen(s1);
		printf("Case #%d: ",j+1);
		for(int i=0;i<n;i++)
		{
			if(s1[i]!=' ')
				printf("%c",s1[i]-delta[s1[i]-'a']);
			else
				printf("%c",s1[i]);
		}
		printf("\n");
	}
	return 0;
}
#endif