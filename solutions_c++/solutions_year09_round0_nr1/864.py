#include <stdio.h>
#include <vector>

using namespace std;

int tree[100000][30];
vector<int>a,b;
char s[200000];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int d,n,T,t,i,j,k,x,ind;
	scanf("%d%d%d",&n,&d,&T);
	k=2;
	while(d--)
	{
		scanf("%s",&s);
		x=1;
		for(i=0;i<n;i++)
			if(tree[x][s[i]-'a'])
				x=tree[x][s[i]-'a'];
			else
			{
				tree[x][s[i]-'a']=k;
				x=k;
				k++;
			}
	}
	t=1;
	while(T--)
	{
		scanf("%s",&s);
		ind=0;
		a.push_back(1);
		for(i=0;i<n;i++)
		{
			if(s[ind]=='(')
			{
				for(ind++;s[ind]!=')';ind++)
					for(j=0;j<a.size();j++)
						if(tree[a[j]][s[ind]-'a'])
							b.push_back(tree[a[j]][s[ind]-'a']);
			}
			else
				for(j=0;j<a.size();j++)
					if(tree[a[j]][s[ind]-'a'])
						b.push_back(tree[a[j]][s[ind]-'a']);
			ind++;
			a=b;
			b.clear();
		}
		printf("Case #%d: %d\n",t,a.size());
		t++;
	}
	return 0;
}

