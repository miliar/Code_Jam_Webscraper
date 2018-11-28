#include <iostream>
#include <map>
using namespace std;

int query[1024];
bool check[1024];

int main()
{
	int T;
	int S, Q;

	scanf("%d", &T);
	for ( int t=0 ; t<T ; ++t ) {
		map<string,int> idx;
		char eng[128];
		scanf("%d", &S);
		gets(eng); // '\n'
		for ( int i=0 ; i<S ; ++i ) {
			gets(eng);
			idx[eng] = i;
		}

		scanf("%d", &Q);
		gets(eng); // '\n'
		for ( int i=0 ; i<Q ; ++i ) {
			gets(eng);
			query[i] = idx[eng];
		}

		memset(check, 0, sizeof(check));
		int cnt = 0;
		int res = 0;
		for ( int i=0 ; i<Q ; ++i ) {
			if ( !check[ query[i] ] ) {
				check[ query[i] ] = true;
				++cnt;
			}
			if ( cnt == S ) {
				memset(check, 0, sizeof(check));
				check[ query[i] ] = true;
				cnt = 1;
				res++;
			}
		}

		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}
