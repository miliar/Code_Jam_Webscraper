#include<iostream>
using namespace std;

bool set[5001][26];
char str[5001][16];
char ss[1000];
int l,d,n;
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	int i, j, T;
	int res,len;
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",str[i]);
	for(T=1;T<=n;T++)
	{
		res = 0;
		memset(set,0,sizeof(set));
		scanf("%s",ss);
		len = strlen(ss);
		i = 0;
		j = 0;
		while(i<len)
		{
			if(ss[i]=='(')
			{
				i++;
				while(ss[i] !=')')
				{
					set[j][ss[i]-'a'] = 1;
					i ++;
				}
				i ++;
				j ++;
			}
			else
			{
				set[j][ss[i]-'a'] = 1;
				j++;
				i++;	
			}
		}
		bool flag;
		for(i = 0;i < d;i++)
		{	
			flag = 1;
			for(j = 0;j < l; j ++)
			{
				if(!set[j][str[i][j]-'a'])
				{
					flag = 0;
					break;
				}
			}
			if(flag)
			{
				res ++;
			}
		}
	printf("Case #%d: %d\n",T,res);
	}		
	return 0;
} 
