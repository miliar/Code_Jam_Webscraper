#include <iostream>
using namespace std;

int mark[1000];
char s[1000];

int main()
{
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	
	int T,test=1;;
	for (scanf("%d\n",&T);test<=T;++test)
	{
		memset(mark,-1,sizeof(mark));
		gets(s);
		int cnt=0;
		for (int i=0;s[i];++i)
		if (mark[s[i]]==-1) mark[s[i]]=cnt++;
		for (int i=0;i<300;++i)
		if (mark[i]==1) mark[i]=0;
		else if (mark[i]==0) mark[i]=1;
		
		if (cnt==1) ++cnt;
		
		long long base=1,ans=0;
		for (int i=strlen(s)-1;i>=0;--i)
		{
			ans+=base*mark[s[i]];
			base*=cnt;
		}
		
		printf("Case #%d: ",test);
		cout << ans <<endl;
	}
	return 0;
}
