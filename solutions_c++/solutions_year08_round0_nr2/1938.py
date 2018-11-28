#include <iostream>
#include <algorithm>

using namespace std;

static const int MAX = 220;

struct tt{
	int dir;
	int m1;
	int m2;
	int v;
} tr[MAX];

int cmp(const void* va, const void* vb){
	const tt* a = (const tt*)va;
	const tt* b = (const tt*)vb;
	if (a->m1 < b->m1) return -1;
	if (a->m1 > b->m1) return 1;
	if (a->m2 < b->m2) return -1;
	if (a->m2 > b->m2) return 1;
	if (a->dir < b->dir) return -1;
	if (a->dir > b->dir) return 1;
	return 0;
}


int main(){
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int N;
	cin >> N;
	for (int po = 0; po < N; po++){
		int NA;
		int NB;
		int T;
		cin >> T;
		cin >> NA;
		cin >> NB;
		gets((char*)tr);
		int h1,h2,m1,m2;
		for (int i = 0; i < NA; i++){
			tr[i].dir = 0;
			tr[i].v = 0;
			scanf("%02d:%02d %02d:%02d\n",&h1,&m1,&h2,&m2);
			tr[i].m1 = h1*60+m1;
			tr[i].m2 = h2*60+m2;
		}
		for (int i = NA; i < NA+NB; i++){
			tr[i].dir = 1;
			tr[i].v = 0;
			scanf("%02d:%02d %02d:%02d\n",&h1,&m1,&h2,&m2);
			tr[i].m1 = h1*60+m1;
			tr[i].m2 = h2*60+m2;
		}
		qsort(tr, NA+NB, sizeof(struct tt), cmp);
		int uns = NA + NB;
		int trains[2] = {0,0};
		int min = 0;
		int time;
		while (uns > 0){
			for (min = 0;min < NA+NB && tr[min].v;min++);
			time = tr[min].m2+T;
			int pos = tr[min].dir;
			tr[min].v = 1;
			trains[pos]++;
			pos = 1-pos;
			uns--;
			while (uns > 0){
				int h = min;
				for (; h < NA+NB && (tr[h].v || tr[h].dir != pos || tr[h].m1 < time); h++);
				if (h >= NA+NB){
					break;
				}
				tr[h].v = 1;
				time = tr[h].m2 + T;
				pos = 1-pos;
				uns--;
				min = h;
			}
		}
		cout << "Case #" << po+1 << ": " << trains[0] << " " << trains[1] << "\n";
	}
	return 0;
}
