#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
using namespace std;

#define REP(i,a) for(int i=0; i<(int)(a); ++i)
#define all(c) (c).begin(), (c).end()

int main() {	
	int N, S, Q;
	string q;
	
	cin >> N;
	REP(n, N) {
		scanf("%d\n", &S);
		
		map<string, int> M;
		vector<int> min(S);	
		
		REP(i, S) { getline(cin, q); M[q] = i; }
		
		scanf("%d\n", &Q);		
		while (Q--) {
			getline(cin, q);
			min[ M[q] ] = 987654321;
			min[ M[q] ] = *min_element( all(min) ) + 1;
		}
		cout << "Case #" << n + 1 << ": " << *min_element( all(min) ) << endl;
	}
	
	return 0;
}
