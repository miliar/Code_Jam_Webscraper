#include<algorithm>
#include<cstdio>

using namespace std;

int P[255], T[255], O[255];

inline int abs(int x) {
	return x>0 ? x : -x;
}

int single_case(int caseID) {
	int res = 0, n;
	P['O'] = P['B'] = 1;
	T['O'] = T['B'] = 0;
	O['O'] = 'B'; O['B'] = 'O';
	scanf("%d",&n);
	while (n--) {
		char robot, in[2]; int field;
		scanf("%s %d",in,&field);
		robot = in[0];
		int dist = abs(P[robot] - field);
		if ( T[robot] + dist + 1 <= T[O[robot]] )
			T[robot] = T[O[robot]] + 1;
		else
			T[robot] += dist + 1;
		P[robot] = field;
	}
	res = max(T['O'],T['B']);
	printf("Case #%d: %d\n",caseID,res);
}

int main() {
	int z;
	scanf("%d",&z);
	for(int i = 1 ; i <= z ; i++) {
		single_case(i);
	}
}
