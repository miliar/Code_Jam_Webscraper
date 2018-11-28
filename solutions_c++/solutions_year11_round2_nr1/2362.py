#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int many;
string R[105];
struct data {
	int Win,Game;
	double now;
} WP[105],OWP[105],OOWP[105];

void input()
{
	scanf("%d",&many);
	for(int i=0;i<many;i++){
		cin >> R[i];
		for(int j=0;j<many;j++){
			if(R[i][j] == '.') continue;
			else if(R[i][j] == '1') WP[i].Win ++ ; 
			WP[i].Game ++;
		}
		WP[i].now = (double)WP[i].Win / WP[i].Game;
	}
}
void owp()
{
	double sum,A;
	int a,b;
	for(int i=0;i<many;i++){
		sum = 0;
		for(int j=0;j<many;j++){
			if(R[i][j] == '.') continue;
			a = WP[j].Win - 1;
			if(R[i][j] == '1') a ++ ;
			b = WP[j].Game - 1;
			if(b == 0) continue;
			sum += (double)a/b;
		}
		A = double(1)/WP[i].Game;
		OWP[i].now = sum * A;
	}
}
void oowp()
{
	double sum,A;
	for(int i=0;i<many;i++){
		sum = 0;
		for(int j=0;j<many;j++){
			if(R[i][j] == '.') continue;
			sum += OWP[j].now;
		}
		A = double(1)/WP[i].Game;
		OOWP[i].now = sum * A;
	}
}
void clean()
{
	for(int i=0;i<many;i++){
		OOWP[i].Game = OOWP[i].Win = OWP[i].Game = OWP[i].Win = WP[i].Game = WP[i].Win = 0;
	}
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		input();
		owp();
		oowp();
		printf("Case #%d:\n",i);
		for(int i=0;i<many;i++){
			double ans = 0.25 * WP[i].now + 0.5 * OWP[i].now + 0.25 * OOWP[i].now;
			cout << ans << endl;
		}
		clean();
	}
	return 0;
}