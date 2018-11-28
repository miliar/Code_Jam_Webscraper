#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

const int MAXSIZE = 105;

struct Schedule{
	int start, end;
};

int numOfCase, kase;
int T, NA, NB;
Schedule train[2][MAXSIZE];
bool mark[2][MAXSIZE];

int cmp(const void *a, const void *b)
{
	Schedule *aa = (Schedule *)a;
	Schedule *bb = (Schedule *)b;
	if (aa->start == bb->start)
		return aa->end - bb->end;
	return aa->start - bb->start;
}

int main()
{
	scanf("%d", &numOfCase);
	for (kase = 1; kase <= numOfCase; kase++)
	{
		int i, j, k;
		scanf("%d%d%d", &T, &NA, &NB);
		for (i = 0; i < NA; i++){
			int hour, mint;
			scanf("%d:%d", &hour, &mint);
			train[0][i].start = hour * 60 + mint;
			scanf("%d:%d", &hour, &mint);
			train[0][i].end = hour * 60 + mint;
		}
		for (i = 0; i < NB; i++){
			int hour, mint;
			scanf("%d:%d", &hour, &mint);
			train[1][i].start = hour * 60 + mint;
			scanf("%d:%d", &hour, &mint);
			train[1][i].end = hour * 60 + mint;
		}
		qsort(train[0], NA, sizeof(Schedule), cmp);
		qsort(train[1], NB, sizeof(Schedule), cmp);

		memset(mark, 0, sizeof(mark));
		int cnt[2];
		cnt[0] = cnt[1] = 0;
		while (1){
			int ab;
			// choose a train a/b.
			// if no train can be chosen, then break;
			if (NA == 0){
				ab = 1;
				k = 0; while (mark[1][k] && k < NB) k++;
				if (k >= NB) break;
			}
			else if (NB == 0){
				ab = 0;
				k = 0; while (mark[0][k] && k < NA) k++;
				if (k >= NA) break;
			}
			else{
				i = 0; while (mark[0][i] && i < NA) i++;
				j = 0; while (mark[1][j] && j < NB) j++;
				if ( i >= NA && j >= NB) break;
				if (i >= NA){
					ab = 1; k = j;
				}
				else if (j >= NB){
					ab = 0; k = i;
				}
				else{
					if (train[0][i].start <= train[1][j].start){
						ab = 0; k = i;
					}
					else{
						ab = 1; k = j;
					}
				}
			}

			int num[2];
			num[0] = NA;
			num[1] = NB;
			mark[ab][k] = true;
			cnt[ab]++;
			while (1){
				int ba = 1 - ab;
				int time = train[ab][k].end + T;
				bool found = false;
				for (int l = 0; l < num[ba]; l++)
					if (!mark[ba][l] && train[ba][l].start >= time){
						k = l;
						found = true;
						break;
					}
				if (found){
					ab = ba;
					mark[ab][k] = true;
				}
				else{
					break;
				}
			}
		}
		cout << "Case #" << kase << ": " << cnt[0] << " " << cnt[1] << endl;
	}
return 0;
}

