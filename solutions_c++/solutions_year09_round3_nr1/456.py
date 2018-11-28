#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

#define MAXN 111
#define MAXC 1111

long long ans;
char data[MAXN];

void run()
{
	long long i,x,b,len=strlen(data),now=0;
	int mean[MAXC];
	memset(mean,-1,sizeof(mean));
	mean[data[0]]=1;
	for (i=1;i<len;i++)
	{
		if (mean[data[i]]==-1)
		{
			++now;
			if (now==1)
				mean[data[i]]=0;
			else
				mean[data[i]]=now;
		}
	}
	b=now+1;
	if (b==1) b++;
	x=1;
	for (i=len-1;i>=0;i--)
	{
		ans+=mean[data[i]]*x;
		x*=b;
	}
}

void ini()
{
	int i,T;
	cin>>T;
	for (i=1;i<=T;i++)
	{
		ans=0;
		scanf("%s",data);
		run();
		printf("Case #%d: ",i);
		cout<<ans<<endl;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ini();
	return 0;
}
	
	
