#include<iostream>

using namespace std;

int main(){
	//surprising: p-2 p-2 p
	//not surprising: p-1 p-1 p
	int T;
	scanf("%d\n", &T);
	for(int q = 1; q <= T; q++){
		int n, s, p;
		cin >> n >> s >> p;
		int normal = 0;
		int surprising = 0;
		for(int i = 0; i < n; i++){
			int score;
			cin >> score;
			if(score >= 3 * p - 2) normal++; //also handles p == 0
			else if(score >= 3 * p - 4 && p >= 2) surprising++;
		}
		int ans = normal + min(surprising, s);
		printf("Case #%d: %d\n", q, ans);
	}
}
