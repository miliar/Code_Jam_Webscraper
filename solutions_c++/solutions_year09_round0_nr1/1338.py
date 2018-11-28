#include<iostream>
#define lMax 16
#define dMax 5001
using namespace std;

int l, d, n;
bool table[lMax][26];
char map[dMax][lMax], tmp[dMax];



int main()
{
	int i, j, k, tl, ans, ttl;
	bool p;
	
	scanf("%d %d %d", &l, &d, &n);
	getchar();
	for(i=0;i<d;i++)
		gets(map[i]);
		
	for(i=1;i<=n;i++)
	{
		gets(tmp);
		ttl=strlen(tmp);
		
		memset(table, 0, sizeof(table));
		for(j=0, p=tl=0;j<ttl;j++)
		{
			if(tmp[j]>='a' && tmp[j]<='z')
				table[tl][tmp[j]-'a']=1;
			else if(tmp[j]=='(')
				p=1;
			else if(tmp[j]==')')
				p=0;
				
			if(!p)
			    tl++;
		}
		
		for(j=0, ans=0;j<d;j++)
		{
			for(k=0;k<l;k++)
			{
				if(!table[k][ map[j][k]-'a' ])
				    break;
			}
			if(k==l)
			    ans++;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
