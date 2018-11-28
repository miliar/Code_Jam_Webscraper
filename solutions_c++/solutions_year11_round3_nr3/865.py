#include<iostream>
#include<cstdio>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)

long cs=0,t,n,L,H,a[111];

bool ok(long div)
{
	long i;

	F(i,1,n)
		if(a[i]%div&&div%a[i])
			return false;

	return true;
}



int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);

	long i;

	cin >> t;

	while(t--)
	{
		cin >> n >> L >> H;

		F(i,1,n) cin >> a[i];

		F(i,L,H)
			if(ok(i))
				break;

		if(i>H) printf("Case #%d: NO\n",++cs);
		else printf("Case #%d: %ld\n",++cs,i);
	}

	return 0;
}