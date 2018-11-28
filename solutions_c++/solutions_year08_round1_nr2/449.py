#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int main()
{
	int n, n2=0;
	scanf("%d\n",&n);
	while (n--) {
		int N, M;
		scanf("%d\n%d\n",&N,&M);
		int arr[M][N];
		int ans[N];
		for (int i=0; i<M; i++)
			for (int j=0; j<N; j++)
				arr[i][j] = -1;
		for (int i=0; i<N; i++) ans[i] = 0;
		for (int i=0; i<M; i++) {
			int T;
			scanf("%d",&T);
			for (int j=0; j<T; j++) {
				int X, Y;
				scanf("%d %d",&X,&Y);
				if (arr[i][X-1]==-1) {
					arr[i][X-1] = Y;
				} else {
					cerr << "huh" << endl;
					arr[i][X-1] = 2;
				}
			}
		}
		//
		int zzz = 1;
		while (zzz) {
			zzz = 0;
			for (int i=0; i<M; i++) {
				int type = 1;
				int mal = -1;
				for (int j=0; j<N; j++) {
					if (arr[i][j]==2) {
						type = 0;
						break;
					}
					if (arr[i][j]==0) {
						if (ans[j]==0) {
							type = 0;
							break;
						}
					}
					if (arr[i][j]==1) {
						mal = j;
					}
				}
				if (type==1) {
					if (mal==-1)
						cerr << "huh2" << endl;
					if (mal!=-1 && ans[mal]==0) {
						ans[mal] = 1;
						zzz = 1;
					}
				}
			}
		}
		//
		int impossible = 0;
		for (int i=0; i<M; i++) {
			int imp = 1;
			for (int j=0; j<N; j++) {
				if (arr[i][j]==2) {
					imp = 0;
					break;
				}
				if (arr[i][j]==ans[j]) {
					imp = 0;
					break;
				}
			}
			if (imp==1) {
				impossible = 1;
				break;
			}
		}
		// print result
		if (impossible) {
			printf("Case #%d:",++n2);
			printf(" IMPOSSIBLE\n");
		} else {
			printf("Case #%d:",++n2);
			for (int i=0; i<N; i++) {
				printf(" %d",ans[i]);
			}
			printf("\n");
		}
	}
	return 0;
}

