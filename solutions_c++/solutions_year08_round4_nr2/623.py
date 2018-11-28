#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>

int n , m , a[4] , b[4];
__int64 A;

int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int cas,ca,i;
	__int64 s;
	for(scanf("%d",&cas),ca=1;ca<=cas;ca++)
	{
		printf("Case #%d: ",ca);
		scanf("%d%d%I64d" , &n , &m , &A);
		bool ok = false;
		a[0] = 0;
		b[1] = m;
		for( b[0] = 0 ; b[0] <= m && !ok ; b[0]++ )
			for( a[1] = 0 ; a[1] <= n && !ok ; a[1]++ )
				for( a[2] = 0 ; a[2] <= n && !ok ; a[2]++ )
					for( b[2] = 0 ; b[2] <= m && !ok ; b[2]++ )
					{
						a[3]=a[0],b[3]=b[0];
						s = 0;
						for(i=0;i<3;i++)
						{
							s += (a[i]*b[i+1]-a[i+1]*b[i]);
						}
						if(s < 0 ) s = -s;
						if( s == A ) 
						{
							ok = true;
							printf("%d %d %d %d %d %d\n" , a[0] , b[0] , a[1] , b[1] , a[2] , b[2]);
						}
					}
		//printf("%I64d\n" , s);
		//printf("%I64d\n" , A);
		if(!ok)printf("IMPOSSIBLE\n");

	}
}

