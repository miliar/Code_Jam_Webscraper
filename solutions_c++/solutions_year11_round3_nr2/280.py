#include <iostream>
#include <string>

using namespace std;

long long a[2000],s[2000];
int rank[2000];
long long n,t,c,l,tot,ans1,ans2;

bool com(const int aa,const int bb)
{
	return a[aa]>a[bb];
}

long long calc(int m)
{
	long long ll=l,ret=0;
	for (int i=0;i<c && ll>0;i++)
	{
		long long now=rank[i],num;
		if (n<now) num=0; else num=((n-now)/c)+1;
		if (m-1<now) num-=0; else num-=((m-1-now)/c)+1;
		if (num<=0) continue;
		else
		{
			num=min(num,ll);
			ret+=num*a[now];
			ll-=num;
		}
	}
	return ret;
}
long long calc2(long long m)
{
	return (tot*2LL*(m/c)+s[m%c]*2LL);
}

void doing()
{
	cin >> l >> t >> n >> c; s[0]=0; tot=0;
	for (int i=1;i<=c;i++)
	{
		cin >> a[i];
		s[i]=s[i-1]+a[i]; tot+=a[i];
		rank[i-1]=i;
	}
	sort(rank,rank+c,com);
	long long m=calc2(n),ans=m;
	if (t>m) ans=m;
	else
	if (t==0) ans=m-calc(1);
	else
	{
		long long ll=1,rr=n;
		while (rr-ll!=0)
		{
			long long mid=(ll+rr)/2;
			if (calc2(mid)<t) ll=mid+1;
				else rr=mid;
		}
		ans=m-calc(ll+1);
		l--;
		if (l>=0)
		ans=min(ans,m-calc(ll+1)-(calc2(ll-1LL)+a[(ll-1)%c+1]*2LL-t)/2LL);
		
	}
	cout << ans << endl;
	
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		doing();
	}
}
