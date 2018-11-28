#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;


int main(){
	int T, X, i;
	char str[100];

	freopen("B-large.in", "r", stdin);
	freopen("B2.out", "w", stdout);
	scanf("%d", &T);
	for( X=1; X<=T; ++X){
		scanf("%s", str);

		vector<int> vi;

		for( i=0; str[i]; ++i)
			vi.push_back( str[i] - '0');

		if( next_permutation( vi.begin(), vi.end())){
			;
		}
		else {
			vi.push_back(0);
			sort(vi.begin(), vi.end());
			for( i=1; i<vi.size(); ++i){
				if( vi[i] != 0){
					swap( vi[i], vi[0]);
					break;
				}
			}
		}

		printf("Case #%d: ", X);
		for(i=0; i<vi.size(); ++i)
			printf("%d", vi[i]);
		puts("");
	}

	return 0;
}