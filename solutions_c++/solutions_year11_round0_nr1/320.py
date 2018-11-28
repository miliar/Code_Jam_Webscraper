#include<cstdio>
using namespace std; 

const int maxn = 102; 

int T; //testcases;
int N; //buttons;

int robot[maxn];
int time[maxn];
//int prev[maxn];
//int cost[maxn];
int button[maxn];

void input(){
	scanf("%ld", &N); 
	char c; 
	int b; 
	for (int i = 1; i <= N; i++) {
		scanf(" %c %ld", &c, &b); 
		if (c == 'O') robot[i] = 0; 
		else robot[i] = 1; 
		button[i] = b; 
	}
}

inline int abs(int a){
	return a>0?a:(-a);
}

inline int max(int a, int b){
	return a>b?a:b;
}
void work(){
	time[0] = 0; 
	button[0] = 1; 
	int lastone[2] = {0,0}; 
	for (int i = 1; i <= N; i++){
		int curRobot = robot[i];
		int k = lastone[curRobot];
		lastone[curRobot] = i;	 
		int sameRobot = time[k] + abs(button[i] - button[k]) + 1; 
		time[i] = max(sameRobot, time[i-1] + 1);
	}
}

void output(int cnt){
	printf("Case #%ld: %ld\n", cnt, time[N]);
}
int main(){
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\A-large.in", "r", stdin); // should be deleted before submit; 
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\A-large.out", "w", stdout);
	scanf("%ld", &T); 
	for (int i = 0; i < T; i++){
		input();
		work();
		output(i+1);
	}
	fclose(stdout);
}