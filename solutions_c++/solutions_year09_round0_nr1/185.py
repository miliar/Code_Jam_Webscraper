#include <iostream>
#include <vector>
using namespace std;

char word[5100][20]={0};
char temps[1000]={0};
vector <char> s[20];
vector <char>::iterator p;
int i,j,k,n,m,l,now,sum,x;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d %d %d",&l,&n,&m);
	gets(word[0]);
	for (i=0; i<n; i++)
		gets(word[i]);
	for (i=1; i<=m; i++)
	{
		gets(temps);
		now = 0;
		sum = 0;
		for (j=0; j<l; j++)
		{
			s[j].clear();
			if (temps[now]=='(')
			{
				now++;
				while (temps[now]!=')')
					s[j].push_back(temps[now++]);
				now++;
			}
			else
				s[j].push_back(temps[now++]);
		}
		for (j=0; j<n; j++)
		{
			for (k=0; k<l; k++)
			{
				for (p=s[k].begin(); p!=s[k].end(); p++)
					if (*p==word[j][k])
						break;
				if (p==s[k].end())
					break;
			}
			if (k==l)
				sum++;
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}