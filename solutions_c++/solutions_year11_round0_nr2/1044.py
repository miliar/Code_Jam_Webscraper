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
const double PI = 2 * acos(0.0);
const long double eps = 1e-12;

void main(){
	int T;

	cin >> T;

	FOR(i,1,T){
		vector<vc> com(200,vc(200,0));
		vector<vc> opp(200,vc(200,0));
		string input;
		vc list;
		int C;
		cin >> C;

		FR(j,C-1){
			char a,b,c;
			cin >> a >> b >> c;
			com[b][a] = com[a][b] = c;
		}
		
		int D;
		cin >> D;

		FR(d,D-1){
			char a,b;
			cin >> a >> b;
			opp[b][a] = opp[a][b] = 1;
		}

		int N;
		cin >> N;
		cin >> input;

		int ind = 0;

		while ( ind < input.sz ){
			char c = input[ind];
			bool del = false;

			FRV(j,list){
				if ( list.sz == 0 ) break;
				if ( opp[c][list[j]] ){
					list.erase(ALL(list));
					del = true;
					break;
				}
			}

			if ( del ) {
				ind ++;
				continue;
			}
			char nc = (ind == input.sz - 1 ? 0 : input[ind + 1]);

			if ( com [c][nc] ){
				c = com [c][nc];
				ind++;
			}

			list.pb(c);

			ind ++;
		}

		ss res;
		res<<"[";
		bool f = true;
		FRV(k,list){
			if ( list.sz == 0 ) break;
			if ( !f ) res <<", ";
			f = false;
			res << list[k];
		}
		res<<"]";
		cout << "Case #" << i << ": "<<res.str()<<endl;
	}
}