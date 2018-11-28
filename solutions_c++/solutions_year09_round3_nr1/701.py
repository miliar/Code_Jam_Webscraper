#include<stdio.h>
#include<map>
using namespace std;
map < char , int > M;
char s[120];
unsigned __int64 now, p;
int main()
{
	int cas, id, i, nca;
	freopen("a11.in","r",stdin);
	freopen("as.txt","w",stdout);
	scanf("%d",&cas);
	nca = 0;
	while(cas--)
	{
		nca++;
		scanf("%s",s);
		id = 0;
		M.clear();
		for(i = 0; s[i] != '\0'; i++)
		{
			if (M[s[i]])
				continue;
			else
			{
				M[s[i]] = ++id;
			}
		}
		if (id == 1)
			id = 2;
		now = 0;
		p = 1;
		for(i--; i >=0; i--)
		{
			if (M[s[i]] == 2)
			{
				p*=(unsigned __int64)id;
				continue;
			}
			unsigned __int64 t = M[s[i]];
			if (t > 2)
				t--;
			now += t * p;
			p*=(unsigned __int64)id;
		}
		printf("Case #%d: %I64u\n",nca, now);
	}
}