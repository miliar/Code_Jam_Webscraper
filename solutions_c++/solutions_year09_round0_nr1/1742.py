#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int LEN=30, WORD=10010, CA=1010;
char word[WORD][LEN], p[WORD*LEN];
bool has[LEN][30];
int len, d, ca;

void pre()
{
	int i,j=0,lenP=strlen(p);
	memset(has,0,sizeof(has));
	for(i=0;i<lenP;++i)
	{

		if(p[i]!='(')
		{
			has[j][p[i]-'a']=true;
		}
		else
		{
			i++;
			while(i<lenP && p[i]!=')')
			{
				has[j][p[i]-'a']=true;
				i++;
			}
		}
		j++;
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d%d%d", &len, &d, &ca);
	int i,j,k;
	for(i=0;i<d;++i) scanf("%s",word[i]);
	for(k=1;k<=ca;++k)
	{
		scanf("%s",p);
		pre();
		int ans=0;
		for(i=0; i<d;++i)
		{
			for(j=0;word[i][j]!=0;++j)
			{
				if(!has[j][word[i][j]-'a'])break;
				//has[j]  ; not has[i]
			}
			if(word[i][j]==0)ans++;
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}