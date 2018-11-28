#include <cstdio>

int abs(int a) {
	if(a<0)
		return -a;
	return a;
}

int max(int a, int b){
	if(a>b) return a;
	return b;
}

int main() {


	char robot[100];
	int pos[100];


	int T, N, R, P;
	scanf("%d ", &T);
	for(int i=0; i<T; ++i) {
		scanf("%d ", &N);
		for(int j=0; j<N; ++j) {
			scanf("%c %d ", &robot[j], &pos[j]);
		}
		

		int erg = 0;
		int p[2], t[2];
		p[0] = 1; p[1] = 1;
		t[0] = 0; t[1] = 0;
		int time = 0;
		for(int j=0; j<N; ++j) {
			int num = 0;
			if(robot[j]=='O')
				num = 1;

			int timetogo = 1+abs(pos[j]-p[num]);
			time = max(t[num]+timetogo, time+1);
			p[num] = pos[j];
			t[num] = time;
		}
		
		printf("Case #%d: %d\n", i+1, time);
	
	}

	





	return 0;
}

