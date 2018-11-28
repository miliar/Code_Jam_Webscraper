#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;

struct score{
	int a1, a2, a3, max_sc;
};
map< int , vector<score> > m;
int N, S, p, t[101];
int ans;

bool is_surprising(int a, int b, int c){
	return ( abs(c-b) == 2 || abs(c-a) == 2 || abs(b-a) == 2 )? true : false ;
}

void foo(){
	for(int i=0 ; i <= 10 ; i++ ){
		for(int j=i ; j <= 10 ; j++ ){
			for(int k=j ; k <= 10 ; k++ ){
				if( k-j <= 2 && k-i <= 2 && j-i <= 2 ){
					score sc;
					sc.a1 = i;
					sc.a2 = j;
					sc.a3 = k;
					sc.max_sc = max(i,max(j,k));
					m[i+j+k].push_back( sc );
				}
			}
		}
	}
}

score query(int num, bool flag){
	vector<score> v = m[num];
	for(int i=0 ; i < v.size() ; i++ ){
		if( is_surprising( v[i].a1 , v[i].a2 , v[i].a3 ) == flag ){
			return v[i];
		}
	}
	score sc;
	if( num == 0 ){
		sc.a1 = sc.a2 = sc.a3 = sc.max_sc = 0;
	}else if( num == 1 ){
		sc.a1 = sc.a2 = 0;
		sc.a3 = sc.max_sc = 1;
	}else if( num == 29 ){
		sc.a1 = 9;
		sc.a2 = sc.a3 = sc.max_sc = 10;
	}else if( num == 30 ){
		sc.a1 = sc.a2 = sc.a3 = sc.max_sc = 10;
	}
	return sc;
}

void solve(vector<score> v,int i){
	if( i == N ){
		int s=0, cnt=0;
		for(int j=0 ; j < v.size() ; j++ ){
			if( is_surprising( v[j].a1 , v[j].a2 , v[j].a3 ) ) s++;
			if( v[j].max_sc >= p ) cnt++;
		}
		if( s == S ){
			ans = max( ans , cnt );
			/*cout << "ans:" << cnt << endl;
			for(int j=0 ; j < v.size() ; j++ ){
				cout << v[j].a1 << " " << v[j].a2 << " " << v[j].a3 << endl;
			}
			cout << endl;
			*/
		}
		return;
	}
	
	score sc = query( t[i] , true );
	v.push_back( sc );
	solve( v , i+1 );
	v.pop_back();
	
	sc = query( t[i] , false );
	v.push_back( sc );
	solve( v , i+1 );
	v.pop_back();
}

int main(){
	foo();
	
	int T;
	cin >> T;
	for(int t_=1 ; t_ <= T ; t_++ ){	
		cin >> N >> S >> p;
		for(int i=0 ; i < N ; i++ ){
			cin >> t[i];
		}
		ans = 0;
		vector<score> v;
		solve( v , 0 );
		cout << "Case #" << t_ << ": " << ans << endl;
	}
}

