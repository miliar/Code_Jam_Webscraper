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
vector<int> t[110] ;
bool mozna_nalozyc(vector<int> a, vector<int> b)
{
	for(int i=0 ; i<a.size() ; i++)
		if(a[i] <= b[i]) return false ;
	return true ;
}
main()
{
      ios_base::sync_with_stdio(0) ;
      int C ;
      cin >> C ;
      for(int test=1 ; test<=C ; test++)
      {
            cout << "Case #" << test << ": " ;
            int i, j, b, n, k, x ;
            cin >> n >> k ;
            REP(i,n)
		{
			vector<int> a ;
			REP(j,k) {
				cin >> x ;
				a.push_back(x) ;
			}
			t[i] = a ;
		}
		sort(t,t+n) ;
		int odp = 10000000 ;
	for(int ile=0 ; ile<200 ; ile++)
	{
		vector< vector<int> > a ;
		REP(i,n)
		{
			for(j=0 ; j<a.size() ; j++)
				if(mozna_nalozyc(t[i], a[j])) {
					a[j] = t[i] ;
					break ;
				}
			if(j==a.size()) a.push_back(t[i]) ;
			random_shuffle(ALL(a)) ;
		}
		odp = min(odp, (int)a.size()) ;
	}
	cout <<  odp << endl ;
	}           
}
