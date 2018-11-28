#include<cstdio>
#include<cstring>

char ch[200];
char inp[1010];
char inp2[1010];
char temp[100];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("sol.txt","w",stdout);
	ch['y'] = 'a';
	ch['e'] = 'o';
	ch['q'] = 'z';
	ch['z'] = 'q';
	gets( inp );
	gets( inp2 );
	int L = strlen( inp );
	for(int c=0;c<L;c++) ch[inp[c]] = inp2[c];
	//for(int c='a';c<='z';c++) printf("%c - %c\n",c,ch[c]);
	int t;
	scanf("%d",&t); gets( temp );
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d: ",c);
		gets( inp );
		L = strlen( inp );
		for(int c=0;c<L;c++)
		{
			if( inp[c] == ' ' ) printf(" ");
			else printf("%c",ch[inp[c]]);
		}
		if( c != t ) printf("\n");
	}
}
