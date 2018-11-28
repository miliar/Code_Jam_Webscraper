#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<set>

using namespace std;

typedef long long LL;

#define rp(i,l,r) for ( int i=(int)(l); i<=(int)(r); ++i )
#define dp(i,l,r) for ( int i=(int)(l); i>=(int)(r); --i )

#define mn 2001000

int test;
int a,b;
int num[mn];

inline int low( int x )
{
	int a[10]; 
	int temp=x , tot=0 , mo=1;
	while ( temp>0 ) a[++tot]=temp % 10 , temp /= 10 , mo*=10 ;
	int ret=x;   mo/=10 ;
	dp( i,tot,1 ) x=x % mo * 10 + a[i] , ret=min( ret , x );
	return ret;
} // 0 - 0

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("CL.txt","w",stdout);
	cin >> test ;
	rp( T,1,test )
	{
		memset( num , 0 , sizeof num );
		cin >> a >> b ;
		LL ans=0;
		rp( i,a,b )
		{
			int t=low( i ); 
			++num[t];
		} // 0 - 0
		rp( i,1,2000000 ) ans+=(LL)num[i]*(num[i]-1)/2;
		cout << "Case #" << T << ": " << ans << endl;
	} // 0 - 0
} // 0 - 0