#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cmath>
using namespace std ;
typedef long long LL ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
struct punkt
{
	double x,y, r;
} t[100] ;
double kwa(double x)
{
	return x*x ;
}
double odl(punkt a, punkt b)
{
	return sqrt(kwa(a.x-b.x)+kwa(a.y-b.y)) ;
}
main()
{
      ios_base::sync_with_stdio(0) ;
      int C ;
      cin >> C ;
      for(int test=1 ; test<=C ; test++)
      {
            cout << "Case #" << test << ": " ;
            int i, j, a, b, n ;
            cin >> n ;
            double odp = 1000000000 ;
            REP(i,n) cin >> t[i].x >> t[i].y >> t[i].r ;
            if(n==1) {
			cout << t[0].r << endl ;
			continue ;
		}
            if(n==2) {
			cout << min((odl(t[0],t[1])+t[i].r+t[j].r)/2, max(t[0].r, t[1].r)) << endl ;
			continue ;
		}
		
            for(i=0 ; i<n ; i++)
            	for(j=i+1 ; j<n ; j++)
            	{
				for(int k=0 ; k<n ; k++)
				{
					if(k==i || k==j) continue ;
			//		cout << max(t[k].r, odl(t[i],t[j])+t[i].r+t[j].r) << endl ;
					odp = min(odp, max(t[k].r, odl(t[i],t[j])+t[i].r+t[j].r)) ;
				}
			}
		
		cout.setf(ios::fixed) ;
		cout.precision(7) ;	
            cout << odp/2 << endl ;
            
      }           
}
