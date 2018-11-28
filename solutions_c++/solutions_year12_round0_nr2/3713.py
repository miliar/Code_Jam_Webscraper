#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#define MAX 105

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		int N, S, p;
		scanf("%d%d%d", &N, &S, &p);
		vector <int> v(N);
		for (int i = 0; i < N; i++)
			scanf("%d", &v[i]);
		sort(v.rbegin(), v.rend());
		if(p == 0){
			printf("Case #%d: %d\n", t, N);
			continue;
		}
		int cnt = 0;
		for (int i = 0; i < N; i++){
			if(v[i] == 0)
				continue;
			if(v[i]/3 >= p){
				cnt++;
			}
			else if(v[i]%3 >= 1 && v[i]/3 + 1 >= p){
				cnt++;
			}
			else if(S > 0 && v[i]%3 == 2 && v[i]/3 + 2 >= p){
				cnt++;
				S--;
			}
			else if(S > 0 && v[i]/3 + 1 >= p){
				S--;
				cnt++;
			}
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
