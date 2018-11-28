#include <iostream>
using namespace std ;
int num[2005];
int next[1005];
int mon[1005];
int used[1005];
int mo ;
long long work(int now)
{
	int flag[1005] ;
	mo = 0 ;
	memset(flag,0,sizeof(flag)) ;
	long long cc = 0 ;
	while( flag[now]== 0 )
	{
		mo++;
		cc+=mon[now];
		flag[now]=-1;
		now=next[now];
	}
	return cc ;
}
long long dowork(int now , int r)
{
	long long cc = 0 ;
	while(r--)
	{
		cc+=mon[now];
		now=next[now];
	}
	return cc ;
}
int main()
{
	int cas ;
	freopen("A.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&cas) ;
	int cass = 1 ;
	while( cas-- )
	{
		int i,j;
		int r,k,n;
		scanf("%d %d %d",&r,&k,&n) ;
		for ( i = 0 ; i < n ; i ++ )
			scanf("%d",&num[i]) ;
		for ( i = n ; i < n*2 ; i ++ )
			num[i] = num[i-n] ;
		memset(next,-1,sizeof(next)) ;
		memset(mon,0,sizeof(mon));
		int now = 0 ;
		int st , en ;
		for ( st = 0 ; st < n ; st ++ )
		{
			now=num[st];
			for( i = st+1 ; i < n+st ; i ++ )
			{
				now+=num[i] ;
				if(now>k)
				{
					now=now-num[i];
					break;
				}
			}
			mon[st] = now;
			if(i>=n)i-=n;
			next[st] = i ;
		}
		int moo;
		long long ans = 0 , cc  ;
		now=0;
		memset(used,0,sizeof(used));
		while(r>0)
		{
			if(used[now]==-1)
			{
				cc = work(now);
				moo = r/mo ;
				ans+=cc*moo ;
				moo=r%mo ;
				cc = dowork(now,moo);
				ans+=cc;
				r=0;
				break;
			}
			ans+=mon[now];
			r--;
			used[now]=-1;
			now=next[now] ;
			
		}
		printf("Case #%d: %lld\n",cass++,ans);

	}
	return 0 ;
}