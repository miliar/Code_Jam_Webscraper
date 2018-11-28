#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

int T;
int a[101][101];
bool b[101][101];
int n;
char s[1001];
char ch;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		vector<char> V;
		printf("Case #%d: ",test);
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s",s);
			a[s[0]-'A'][s[1]-'A']=a[s[1]-'A'][s[0]-'A']=s[2];
		}
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s",s);
			b[s[0]-'A'][s[1]-'A']=b[s[1]-'A'][s[0]-'A']=true;
		}
		scanf("%d",&n);
		scanf("%c",&ch);
		for(int i=0;i<n;i++)
		{
			scanf("%c",&ch);
			char tmp=0;
			if(V.size())
				tmp=a[ch-'A'][V.back()-'A'];
			if(tmp)
				V[V.size()-1]=tmp;
			else
			{
				bool flag=false;
				for(int j=0;j<V.size();j++)
					if(b[ch-'A'][V[j]-'A'])
					{
						V.clear();
						flag=true;
						break;
					}
				if(!flag)
					V.push_back(ch);
			}
		}
		putchar('[');
		for(int i=0;i+1<V.size();i++)
			printf("%c, ",V[i]);
		if(V.size())
			putchar(V.back());
		puts("]");
	}
	return 0;
}

