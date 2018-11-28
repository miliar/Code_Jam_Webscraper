#include <cstdio>
#include <cstdlib>
#include <cstring>
#define MAX 100
int nComp;
int nOp;
char comp[26][26];
bool op[26][26];
char result[MAX+1];
char str[MAX+1];
int appear[26];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int nT,t=0;
	scanf("%d",&nT);
	while(nT--)
	{
		memset(op,0,sizeof(op));
		memset(comp,0,sizeof(comp));
		memset(appear,0,sizeof(appear));
		scanf("%d",&nComp);
		for(int i=0;i<nComp;++i)
		{
			scanf("%s",str);
			comp[str[0]-'A'][str[1]-'A']=str[2];
			comp[str[1]-'A'][str[0]-'A']=str[2];
		}
		scanf("%d",&nOp);
		for(int i=0;i<nOp;++i)
		{
			scanf("%s",str);
			op[str[0]-'A'][str[1]-'A']=true;
			op[str[1]-'A'][str[0]-'A']=true;
		}
		int len;
		int rLen=0;
		scanf("%d%s",&len,str);
		for(int i=0;i<len;++i)
		{
			result[rLen++]=str[i];
			appear[str[i]-'A']++;
			char ch;
			if(rLen>=2 && (ch=comp[result[rLen-1]-'A'][result[rLen-2]-'A'])!='\0')
			{
				appear[result[rLen-1]-'A']--;
				appear[result[rLen-2]-'A']--;
				rLen--;
				result[rLen-1]=ch;
				appear[ch-'A']++;
			}
			for(int i=0;i<26;++i)
			{
				if(appear[i] && op[result[rLen-1]-'A'][i])
				{
					rLen=0;
					memset(appear,0,sizeof(appear));
					break;
				}
			}
		}
		printf("Case #%d: ",++t);
		putc('[',stdout);
		bool first=true;
		for(int i=0;i<rLen;++i)
		{
			if(first)
				first=false;
			else
				fputs(", ",stdout);
			putc(result[i],stdout);
		}
		puts("]");
	}
}
