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
#define FRV(i,v) FR( i , v.sz - 1 )
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

		vi list(N,0);
		vi slist(N,0);

		FR(j,N-1){
			int n;
			cin >> n;
			slist[j] = list [j] = n;
		}

		int steps = 0;
		SORT(slist);

		FR(j,N-1){
			if ( slist[j] != list[j] )
				steps++;
		}
		//steps <<= 1;
		ss res;

		res << steps << ".000000";
		cout << "Case #" << i << ": "<<res.str()<<endl;
	}
}
