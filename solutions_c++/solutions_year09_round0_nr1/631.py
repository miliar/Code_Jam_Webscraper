#include <stdio.h>
#include <string.h>
const int Maxm=26,MaxNodes=66000,Maxl=16;
struct Node
{
	Node()
	{
		end=0;
		memset(next,-1,sizeof(next));
	}
	int end,next[Maxm];
};
int count;//m???????? count??Trie????? 
Node T[MaxNodes];
long long f[MaxNodes][Maxl];
void insert(char *str)
{
	int cnt=0;
	for (int i=0;i<strlen(str);i++)
	{
		unsigned char ch=str[i];
		if (T[cnt].next[ch-'a']==-1) T[cnt].next[ch-'a']=count++;
		cnt=T[cnt].next[ch-'a'];
		if (T[cnt].end) break;
	}
	T[cnt].end=1;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int l,d,n;
	scanf("%d%d%d\n",&l,&d,&n);
	count=1;
	char str[1001];
	for (int i=0;i<d;i++)
	{
		scanf("%s\n",str);
		insert(str);
	}
	//printf("%d\n",count);

	for (int k=1;k<=n;k++)
	{	
		int len=0;
		memset(f,0,sizeof(f));
		f[0][0]=1;
		scanf("%s\n",str);
		bool flag=false;
		for (int i=0;i<strlen(str);i++)
		{
			if (str[i]=='(') { flag=true;len++;continue;}
			if (str[i]==')') {flag=false;continue;}
			if (flag)
			{
				for (int j=0;j<count;j++)
					if (T[j].next[str[i]-'a']>=0)
						f[T[j].next[str[i]-'a']][len]+=f[j][len-1];
			}
			else
			{
				len++;
				for (int j=0;j<count;j++)
					if (T[j].next[str[i]-'a']>=0)
						f[T[j].next[str[i]-'a']][len]+=f[j][len-1];
			}
		}
		long long ans=0;
		for (int i=0;i<count;i++) ans+=f[i][l];
		printf("Case #%d: %lld\n",k,ans);
	}

	return 0;
}
