#include <stdio.h>
#include <string.h>
char comb[30][30];
bool opp[30][30];
int c,d,n,stack[101],top;
int main()
{
	int i,j,repeat,ri=1;
	char s[101];
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		memset(opp,false,sizeof(opp));
		memset(comb,0,sizeof(comb));
		top=0;
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",s);
			comb[ s[0]-'A' ][ s[1]-'A' ]=comb[ s[1]-'A' ][ s[0]-'A' ]=s[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",s);
			opp[ s[0]-'A' ][ s[1]-'A' ]=opp[ s[1]-'A' ][ s[0]-'A' ]=true;
		}
		scanf("%d%s",&n,s);
		for(i=0;s[i];i++)
		{
			stack[top++]=s[i];
			if( top<2 ) continue;
			if( comb[ stack[top-1]-'A' ] [stack[top-2]-'A'] )
			{
				stack[top-2]=comb[ stack[top-1]-'A' ] [stack[top-2]-'A'];
				top--;
			}
			for(j=top-2;j>=0;j--)
				if( opp[ stack[j]-'A'] [ stack[top-1]-'A'] )
					top=0;
		}
		printf("Case #%d: [",ri++);
		for(i=0;i<top;i++)
		{
			printf("%c%s",stack[i],i==top-1?"":", ");
		}
		puts("]");
	}
	return 0;
}