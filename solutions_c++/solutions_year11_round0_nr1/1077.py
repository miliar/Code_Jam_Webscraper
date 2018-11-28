#include<iostream>
#include<iomanip>
#include<algorithm>
#include<sstream>
#include<vector>
#include<queue>
#include<string>

using namespace std;

#define FOR(i,a,b) for ( int i = a ; i <= b ; i ++ )
#define FRD(i,a,b) for ( int i = a ; i >= b ; i -- )
#define FR(i,a) FOR(i,0,a)
#define FZ(i,a) FRD(i,a,0)
#define sz size()
#define pb push_back
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define FRV(i,v) FOR ( i , 0 , v.sz - 1 )
#define vi vector<int>
#define vf vector<float>
#define vd vector<double>
#define vs vector<string>
#define vc vector<char>

#define mp make_pair
#define ii <int,int>
#define id <int,double>
#define ss stringstream
#define MAX_INT ((1<<31)-1)

const int oo = (int) 1e9;
//const double PI = 2 * acos(0.0);
const long double eps = 1e-12;

int main(){
	int T;

	cin >> T;

	FOR(i,1,T){
		int N;
		cin >> N;
		
		vi olist,blist;
		vc order;

		FOR(n,1,N){
			char a;
			int p;
			cin >> a >> p;
			order.pb(a);
			if ( a == 'O' ) olist.pb(p); else blist.pb(p);
		}

		int t = 0;
		int o = 1, b = 1;
		int no = (olist.sz > 0 ? olist[0]:oo);
		int nb = (blist.sz > 0 ? blist[0]:oo);
		char nc = order[0];
		
		while ( order.sz > 0 ){
			t++;

			bool cb = true;
			bool co = true;

			switch(nc){
			case 'O':
				if ( no == o ){
					olist.erase(olist.begin());
					no = olist.sz > 0 ? olist[0] : oo ;
					order.erase(order.begin());
					if ( order.sz == 0 ) break;
					nc = order[0];
					co = false;
				}
				break;
			case 'B':
				if ( nb == b ){
					blist.erase(blist.begin());
					nb = blist.sz > 0 ? blist[0] : oo ;
					order.erase(order.begin());
					if ( order.sz == 0 ) break;
					nc = order[0];
					cb = false;
				}
				break;
			}

			if ( co && o != no ) o += ( o > no ? -1 : 1 );
			if ( cb && b != nb ) b += ( b > nb ? -1 : 1 );
		}
		
		ss res;
		res << t;
		cout << "Case #" << i << ": "<<res.str()<<endl;
	}
}
