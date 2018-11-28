#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
using namespace std ;
typedef long long LL ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
string t[100] ;
bool ok(string s, int a)
{
	for(int i=a+1 ; i<s.size() ; i++) if(s[i]=='1') return false ;
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
            int n, i, j ;
            cin >> n ;
            REP(i,n) cin >> t[i] ;
            int s = 0 ;
            REP(i,n)
            {
			int best ;
			for(j=i ; j<n ; j++) if(ok(t[j], i)) {
				best = j ;
				break ;
			}
		//	cout << "best = " << best << endl ;
			for(j=best ; j>i ; j--) {
				swap(t[j], t[j-1]) ;
				s++ ;
			}
		}
	//	REP(i,n) cout << t[i] << endl ;
		cout << s << endl ;
	}           
}
