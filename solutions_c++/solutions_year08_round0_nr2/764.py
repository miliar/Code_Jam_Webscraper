#include <stdio.h>
#include <algorithm>
#include <memory.h>

using namespace std;

struct NODE {
	int s, t;
	int k;
}node[400];

bool f[400];
int out[2];


bool cmp(NODE a, NODE b) {
	if (a.s == b.s) {
		return a.t < b.t;
	}
	return a.s < b.s;
}

int main() {

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int i,j,p;

	int Na,Nb,N;

	int t;

	int h,m;


	int C;

	while (scanf("%d", &C) != EOF) {



		for (p = 1; p <= C; p ++) {

			scanf("%d", &t);

			scanf("%d", &Na);
			scanf("%d", &Nb);

			for (i = 0; i < Na; i ++) {

				scanf("%d:%d", &h, &m);
				node[i].s = h * 60 + m;
				scanf("%d:%d", &h, &m);
				node[i].t = h * 60 + m;

				node[i].k = 0;
			}

			for (i = 0; i < Nb; i ++) {

				scanf("%d:%d", &h, &m);
				node[i+Na].s = h * 60 + m;
				scanf("%d:%d", &h, &m);
				node[i+Na].t = h * 60 + m;

				node[i+Na].k = 1;
			}

			sort(node, node + Na + Nb, cmp);

			memset(f,false,sizeof(f));

			int N = Na + Nb;

			out[0] = 0;
			out[1] = 0;

			for (i = 0; i < N; i ++) {
			//	printf("%d %d \n",node[i].s,node[i].t);
			}




			for (i = 0; i < N; i ++) {

			//	if (!f[i]) 
				{

				//	f[i] = true;

					if (!f[i])

					out[node[i].k] ++;

					int pre_type = node[i].k;
					int pre_s = node[i].s;
					int pre_t = node[i].t;

					for (j = i + 1; j < N; j ++) {

						if (node[j].k + pre_type == 1 && pre_t + t <= node[j].s && !f[j]) {

						//	printf("index : %d\n",j);

							f[j] = true;

							pre_type = node[j].k;

							pre_s = node[j].s;
							pre_t = node[j].t;

							break;
						}
					}
				}
			}
			printf("Case #%d: %d %d\n", p, out[0], out[1]);

		}
	}
	return 0;
}




