#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<math.h>
#include<cmath>
#define eps 1e-11
#define INF (2<<63)-1
#define siz 500000

using namespace std;

__int64 max(__int64 a, __int64 b) {
	if(a>b) return a;
	return b;
}
__int64 min(__int64 a, __int64 b){
	if(a<b) return a;
	return b;
}

__int64 gcd(__int64 a, __int64 b)
{
	__int64 c;
	if(a==b)
		return b;
	while(a>0)
	{
		c=b%a;
		b=a;
		a=c;
	}
	return b;
}

vector<__int64> adj[siz];
__int64 t, n, m,  b, c, ct=1, tt, l;
__int64 a[10000];
__int64 dis[1009];
__int64 tot[1009];

__int64 dp(__int64 star, __int64 left)
{
	if(star==n+1)
		return 0;
	__int64 res=INF, r1=INF, r2=INF;
	if(left>0 )
	{
		r1=dp(star+1, left-1)+dis[star+1];
	}
	r2=dp(star+1, left)+dis[star+1]*2;
	res=min(r1, r2);
	return res;
}



__int64 main()
{
	freopen("bnewest.in","r",stdin);
		freopen("out5.txt","w",stdout);
	__int64 i, j, res;
	scanf("%I64d", &t);
	while(t--)
	{
		memset(tot, 0, sizeof(tot) );
		memset(dis, 0, sizeof(dis) );
		res=INF;
		m=0;
		scanf("%I64d %I64d %I64d %I64d", &l, &tt, &n, &c);
		for(i=0;i<c;i++)
			scanf("%I64d", &a[i]);
		for(i=1;i<=n;i++)
		{
			dis[i]=2*a[m];
			m++;
			if(m==c)
				m=0;
			tot[i]+=dis[i]+tot[i-1];
		}
		__int64 rrr=tot[n];
		__int64 val=INF;
		__int64 aux;
		__int64 kk=0;
		//	res=dp(0, l);
		__int64 ss;
		if(l==2)
		{
			for(i=0;i<n;i++)
			{
				kk=0;
				aux=0;
				val=0;
				ss=0;
				for(j=i+1;j<n;j++)
				{
					ss=0;
					if( ( tot[i]>=tt || ( tot[i]<tt && tot[i+1]>tt) ) && ( tot[j]>=tt || ( tot[j]<tt && tot[j+1]>tt) ))
					{
						
						if(tt<=tot[i])
						{
							aux=kk=tot[i+1]-tot[i];
							kk=(tot[i+1]-tot[i])/2;
							val=aux-kk;
							ss+=-dis[i+1]+val;
							
						}
						if(tt>tot[i])
						{
							aux=kk=tot[i+1]-tot[i];
							kk=(tot[i+1]-tt)/2;
							val=aux-kk;
							ss+=-dis[i+1]+val;
						}
						if(tt<=tot[j])
						{
							aux=kk=tot[j+1]-tot[j];
							kk=(tot[j+1]-tot[j])/2;
							val=aux-kk;
							ss+=-dis[j+1]+val;
						}
						if(tt>tot[j])
						{
							aux=kk=tot[j+1]-tot[j];
							kk=(tot[j+1]-tt)/2;
							val=aux-kk;
							ss+=-dis[j+1]+val;
						}
						
						rrr=min(rrr, tot[n]+ss);
					}
				}
			}
		}
		if(l==1)
		{
			for(i=0;i<n;i++)
			{
				if(tt<=tot[i])
				{
					aux=kk=tot[i+1]-tot[i];
					kk=(tot[i+1]-tot[i])/2;
					val=aux-kk;
					ss=tot[n]-dis[i+1]+val;
					rrr=min(rrr, ss);
				}
				if(tt>tot[i] && tt<tot[i+1] )
				{
					aux=kk=tot[i+1]-tot[i];
					kk=(tot[i+1]-tt)/2;
					val=aux-kk;
					ss=tot[n]-dis[i+1]+val;
					rrr=min(rrr, ss);
				}
			}
		}
		res=rrr;
		
		printf("Case #%I64d: %I64d\n", ct++, res);
		
	}
	
	return 0;
	
}
