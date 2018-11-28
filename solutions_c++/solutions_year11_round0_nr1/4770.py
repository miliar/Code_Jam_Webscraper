#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

int main(){


	freopen("input", "rt", stdin);
	//freopen("outA", "w", stdout);
	int cases;
	
	vector<int> seq_o;
	vector<int> seq_b;
	vector<char> seq_r;
	int time,current_o,current_b,cont_o,cont_b,cont_r,aca_b,aca_o;
	int n;
	scanf("%d",&cases);
	char rob;
	int s;
	forn(i,cases){
		time=0;
		current_o=1;
		current_b=1;
		aca_b=aca_o=0;
		seq_o.clear();
		seq_b.clear();
		seq_r.clear();
		cont_o=cont_b=cont_r=0;

		scanf("%d ",&n);
		forn(j,n){
			scanf("%c ",&rob);
			scanf("%d ",&s);		

			seq_r.push_back(rob);
		
			if(rob=='O')
				seq_o.push_back(s);
			else
				seq_b.push_back(s);
		}


		forn(k,n){


			if(seq_r[k]=='O'){

				int need = abs(seq_o[cont_o]-current_o);
				if(aca_o>=need){
					time++;
					aca_b++;
				}else{

					time+= 1 + (need-aca_o);
					aca_b+= 1 + need-aca_o;
				}
				aca_o=0;
				current_o=seq_o[cont_o++];

			}else{

				int need = abs(seq_b[cont_b]-current_b);
				if(aca_b>=need){
					time++;
					aca_o++;
				}else{

					time+= 1 + (need-aca_b);
					aca_o+= 1 + need-aca_b;
				}
				aca_b=0;
				current_b=seq_b[cont_b++];


			}




		}




		printf("Case #%d: %d\n",i+1,time);

	}




	return 0;
}
