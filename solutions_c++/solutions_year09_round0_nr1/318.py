#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

char word[5010][18];
int l,d,n;
char p[600];
int flag[5010];

int main()
{
	//freopen("A-small-attempt0.in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,j,k,len;
	int count;
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",word[i]);
	for(i=1;i<=n;i++)
	{
		scanf("%s",p);
		vector<int> a,b;
		for(j=0;j<d;j++)
			a.push_back(j);
		b.clear();
		len=strlen(p);
		count=0;
		for(j=0;j<len;j++)
		{
			if(p[j]=='(')
			{
				j++;
				while(p[j]!=')')
				{
					for(k=0;k<a.size();k++)
						if(word[a[k]][count]==p[j])
							b.push_back(a[k]);
					j++;
				}
				a=b;b.clear();
			}
			else
			{
				for(k=0;k<a.size();k++)
					if(word[a[k]][count]==p[j])
						b.push_back(a[k]);
				a=b;b.clear();
			}
			count++;
		}
		memset(flag,0,sizeof(flag));
		for(k=0;k<a.size();k++)
			flag[a[k]]=1;
		count=0;
		for(k=0;k<d;k++)
			if(flag[k])
				count++;
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}