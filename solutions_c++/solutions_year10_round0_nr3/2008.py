#include<iostream>
using namespace std;
#define ll long long 
const int max_n = 1010 ;
ll p[max_n+max_n];
ll ars[max_n+max_n];
int visited[max_n];
int memo[max_n];
int R , K , n ;
int f ( int index ){
	int & ret = memo[index] ;
	if ( ret != -1 ) return ret;
	ll sum = 0 ;
//	cerr << "call " << index << " ";
	for ( int i=0 ; i<n ; i++ )
		if ( sum + p[index+i] <= K ){
			sum+=p[index+i] ;
		}
		else {
		//	cerr <<"ret = " << i  << endl;
			return ret = i ;
		}
//	cerr << "ret = " << n << endl;
	return ret = n;
}
ll cap ( int a , int b ){
	--b;
	if ( a == 0 ) return ars[b] ;
	return ars[b] - ars[a-1] ;
}
int main (){
	int tc;
	cin >> tc;
	for ( int caseno = 1 ; caseno<=tc ; caseno ++ ){
		cin >> R >> K >> n;
		for ( int i=0 ; i<n ; i++ ) cin >> p[i];
		for ( int i=0 ; i<n ; i++ ) p[i+n] = p[i] ;
		for ( int i=0 ; i<n ; i++ ) visited[i] = memo[i] = -1 ;
		for ( int i=0 ; i<n+n ; i++ ){
			if ( i == 0 ) ars[i] = p[i];
			else ars[i] = ars[i-1] + p[i] ;
		}
		int cur = 0;
		int from = -1 , to = -1 ;
		for ( int level = 0 ; level < R ; level ++ ){
//			cerr << "level = " << level << "==> cur =" << cur << endl;
			visited[cur] = level ;
			int next = (cur+f ( cur ))%n ;
			if ( visited[next] == -1 ){
				cur = next;
			}
			else{
//				cerr << "found loop" << endl;
				from = visited[next] ;
				to = level;
				break ;
			}
		}
		ll answer = 0;
		for ( int i=0 ; i<n ; i++ ){
			if ( visited[i] == -1 ) continue ;
			if ( from == -1 && to == -1 )
				answer += cap(i,i+f(i));
			else{
				if ( visited[i] < from )
					answer += cap(i,i+f(i));
				else{
					ll cycle = to - from + 1;
					ll cnt = (R - from)/cycle;
					if ( (R-from)%cycle >= visited[i]-from+1 )
						cnt++;
					answer += cnt*cap(i,i+f(i));
				}
			}
		}
		cout << "Case #" << caseno << ": " << answer << endl;
	}
}
