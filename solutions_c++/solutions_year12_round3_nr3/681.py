#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long int LL;
typedef pair<LL,int> P;

map<pair<pair<int,int> , int> , bool> memo;
LL ans = 0;

void solve(vector<P> va, vector<P> vb, int i, int j, LL cnt){
	ans = max( ans , cnt );
	if( i == va.size() || j == vb.size() ) return;
	
	//pair<int,int> p_(i,j);
	//pair<pair<int,int>,int> pp(p_,cnt);
	//if( memo.conut( pp ) ) return;
	//memo[pp] = true;
	
	LL next_cnt;
	int type_a = va[i].second;
	int type_b = vb[j].second;
	LL num_a = va[i].first;
	LL num_b = vb[j].first;
	if( type_a == type_b ){
		if( num_a > num_b ){
			va[i].first -= num_b;
			solve( va , vb , i , j+1 , cnt + num_b );
			va[i].first += num_b;
		}else if( num_a < num_b ){
			vb[j].first -= num_a;
			solve( va , vb , i+1 , j , cnt + num_a );
			vb[j].first += num_a;
		}else{
			solve( va , vb , i+1 , j+1 , cnt + num_a );
		}
	}else{
		solve( va , vb , i+1 , j   , cnt );
		solve( va , vb , i   , j+1 , cnt );
	}
}

int main(){
	int T;
	cin >> T;
	for(int t_ = 1 ; t_ <= T ; ++t_ ){
		int N, M;
		cin >> N >> M;
		
		memo.clear();
		ans = 0;
		vector<P> va, vb;
		for(int i = 0 ; i < N ; i++ ){
			LL a;
			int A;
			cin >> a >> A;
			va.push_back( P(a,A) );
		}
		for(int i = 0 ; i < M ; i++ ){
			LL b;
			int B;
			cin >> b >> B;
			vb.push_back( P(b,B) );
		}
		solve( va , vb , 0 , 0 , 0ll );
		cout << "Case #" << t_ << ": " << ans << endl;
	}
}

