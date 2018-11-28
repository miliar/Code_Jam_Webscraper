#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

#define MAXP 1002

#define SZ(x) ((int)(x).size())

using namespace std;

vector<int> prim;
char isPrim[MAXP];

void precomp(){
	prim.push_back(2);
	for (int i = 3; i < MAXP; i += 2)
		if ( !isPrim[i] ){
			prim.push_back(i);
			for (int j = i<<1; j < MAXP; j += i)
				isPrim[j] = 1;
		}
}

int main(){
	precomp();

	int tcc, tc;
	tcc = 0;
	for(cin >> tc; tc; --tc){
		int a, b, p;
		cin >> a >> b >> p;

		int pL = -1;
		for (int i = 0; i < SZ(prim); i++)
			if ( prim[i] >= p ){
				pL = i;
				break;
			}

		vector<int> moj_set;
		for (int i = a; i <= b; i++)
			moj_set.push_back(i - a);

		for (int i = a; i <= b; i++)
			for (int j = i + 1; j <= b; j++){
				if ( moj_set[i - a] == moj_set[j - a] ) continue;
				char ok = 0;

				for (int k = pL; k < SZ(prim) && !ok; k++)
					if ( !(i % prim[k]) && !(j % prim[k]) ) ok = 1;

				if ( ok ){
					int t = max(moj_set[i - a], moj_set[j - a]);
					int r = min(moj_set[i - a], moj_set[j - a]);

					for (int k = 0; k < SZ(moj_set); k++)
						if ( moj_set[k] == t ) moj_set[k] = r;
				}
			}

		set<int> sol;
		for (int i = 0; i < SZ(moj_set); i++)
			sol.insert(moj_set[i]);

		printf("Case #%d: %d\n", ++tcc, SZ(sol));
	}
	return 0;
}
