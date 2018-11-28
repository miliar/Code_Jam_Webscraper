#include <cstdio>
#include <algorithm>

using namespace std;

struct foo{
	int _[3];
};
foo size[104857600];

void swap(int &a, int &b){
	int c = a;
	a = b;
	b = c;
}

bool cmp(const foo &x, const foo &y){
	return x._[0] < y._[0];
}

int main(){
	int c;
	scanf ("%d", &c);

	int cnt = 0;
	for (int x = 0; x <= 10000; x++)
		for (int y = 0; y <= 10000; y++){
			size[cnt]._[0] = x*y;
			size[cnt]._[1] = x>y?x:y;
			size[cnt++]._[2] = x>y?y:x;
		}
	sort(size, size+cnt, cmp);

	for (int cases = 0; cases < c; cases++){
		int n, m, a;
		scanf("%d%d%d", &n, &m, &a);

		int i, j, x1, y1, x2, y2;
		for (i=0, j=0; i<cnt && j<cnt;){
			if ((size[i]._[1] > n || size[i]._[2] > m) && (size[i]._[1] > m || size[i]._[2] > n)){
				i++;
				continue;
			}
			if ((size[j]._[1] > n || size[j]._[2] > m) && (size[j]._[1] > m || size[j]._[2] > n)){
				j++;
				continue;
			}
			int s = size[i]._[0] - size[j]._[0];
			if (s < a) {
				i++;
				continue;
			} else if (s > a) {
				j++;
				continue;
			}
			x1 = size[i]._[1];
			y2 = size[i]._[2];
			x2 = size[j]._[1];
			y1 = size[j]._[2];
			break;
		}
		if (m > n){
			swap(x1,y1);
			swap(x2,y2);
		}
		if (i>=cnt || j >= cnt)
			printf ("Case #%d: IMPOSSIBLE\n", cases+1);
		else
			printf ("Case #%d: 0 0 %d %d %d %d\n", cases+1, x1, y1, x2, y2);
	}
	return 0;
}
