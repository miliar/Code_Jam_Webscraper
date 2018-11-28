#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int T,n;
char s[10];
char c[1001];
int a[1001];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		scanf("%d",&n);
		vector<int> b,o;
		for(int i=0;i<n;i++)
		{
			scanf("%s%d",s,&a[i]);
			c[i]=s[0];
			if(s[0]=='B')
				b.push_back(a[i]);
			else
				o.push_back(a[i]);
		}
		int ans=0;
		int nowb=1;
		int nowo=1;
		int cntb=0;
		int cnto=0;
		for(int i=0;i<n;i++)
			if(c[i]=='B')
			{
				int step=abs(b[cntb]-nowb)+1;
				nowb=b[cntb++];
				ans+=step;
				if(cnto<o.size())
					nowo+=((o[cnto]>nowo)?1:-1)*(min(step,abs(o[cnto]-nowo)));
			}
			else
			{
				int step=abs(o[cnto]-nowo)+1;
				nowo=o[cnto++];
				ans+=step;
				if(cntb<b.size())
					nowb+=((b[cntb]>nowb)?1:-1)*(min(step,abs(b[cntb]-nowb)));
			}
		printf("%d\n",ans);
	}
	return 0;
}


