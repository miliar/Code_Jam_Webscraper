
#include <iostream>
#include <cstring>

#define N 202

bool mygreater(int *a, int *b, int k){
	
	for(int i=0; i<k; ++i){
		if(a[i] <= b[i]){
			return false;
		}
	}
	return true;
}

int augment(int c[][N], int s, int t, int V){
	
	int anc[N];
	int que[N], head, tail;

	for(int i=0; i<N; ++i){
		anc[i] = -1;
	}

	head = tail = 0;
	anc[s] = s;
	que[tail++] = s;

	while(anc[t] == -1 && head != tail){
		for(int i=0; i<V; ++i){
			if(c[que[head]][i] && anc[i] == -1){
				anc[i] = que[head];
				que[tail++] = i;
			}
		}
		head ++;
	}

	if(anc[t] != -1){
		
		int x = t;

		while(anc[x] != x){
			c[anc[x]][x]--;
			c[x][anc[x]]++;
			x = anc[x];
		}

		return 1;
	}

	return 0;
}

int main(){
	
	using namespace std;


	int T; cin >> T;

	int raw[100][25];
	int c[N][N];

	for(int testcase=1; testcase<=T; ++testcase){
		
		int n, k; cin >> n >> k;

		for(int i=0; i<n; ++i){
			for(int j=0; j<k; ++j){
				cin >> raw[i][j];
			}
		}

		for(int i=0; i<2*n+2; ++i){
			for(int j=0; j<2*n+2; ++j){
				c[i][j] = 0;
			}
		}

		for(int i=0; i<n; ++i){
			for(int j=n; j<2*n; ++j){
				if(mygreater(raw[i], raw[j-n], k)){
					c[i][j] = 1;
				}
			}
		}	

		for(int i=0; i<n; ++i){
			c[2*n][i] = 1;
			c[i+n][2*n+1] = 1;
		}

		/*for(int i=0; i<2*n+2; ++i){
			for(int j=0; j<2*n+2; ++j){
				cout << c[i][j] << " ";
			}
			cout << endl;
		}*/

		int tmp;
		int maxflow = 0;

		while((tmp = augment(c, 2*n, 2*n+1, 2*n+2)) != 0){
			maxflow += tmp;
		}

		/*if(augment(c, 2*n, 2*n+1, 2*n+2) > 0){
			++maxflow;
		}*/

		printf("Case #%d: %d\n", testcase, n-maxflow);
	}

	return 0;
}
