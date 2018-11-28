#include <iostream>

#define MAXLEN 15
#define MAXWORD	5000

using namespace std;

int Len,NWord,NQuery;
char Word[MAXWORD][MAXLEN+1];
int query_map[MAXLEN][26];

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	scanf("%d %d %d ",&Len,&NWord,&NQuery);
	for(int q=0;q<NWord;q++)scanf("%s ",Word[q]);
	for(int q=1;q<=NQuery;q++)
	{
		int index;
		char buff;
		//build map
		for(index=0;index<Len;index++)
		{
			scanf("%c",&buff);
			if(buff=='(')
			{
				scanf("%c",&buff);
				while(buff!=')')
				{
					query_map[index][buff-'a']=q;
					scanf("%c",&buff);
				}
			}
			else query_map[index][buff-'a']=q;
		}
		scanf("%c",&buff);//scan newline
		//run through
		int ans=0;
		for(int w=0;w<NWord;w++)
		{
			for(index=0;index<Len&&query_map[index][Word[w][index]-'a']==q;index++);
			if(index==Len)ans++;
		}
		printf("Case #%d: %d\n",q,ans);
	}

	return 0;
}
