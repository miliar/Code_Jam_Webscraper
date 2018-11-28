#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int MAXN = 5;

char mp[MAXN][MAXN];
int res, max_num, num_point;

inline int getmax(int a, int b){
	return a > b ? a : b;
}

void init(){
	memset(mp, 0, sizeof(mp));
	res = 0;
	num_point = 0;
}

int get_max_num(char x){
	int i, j;
	int res = 0, tmp;
	for(i=0; i<4; ++i){ // every row
		tmp = 0;
		for(j=0; j<4; ++j){
			if(mp[i][j] == x || mp[i][j] == 'T') tmp++;
			else tmp = 0;
			res = getmax(res, tmp);
		}
		if(res == 4) return 4;
	}
	
	for(i=0; i<4; ++i){ // every column
		tmp = 0;
		for(j=0; j<4; ++j){
			if(mp[j][i] == x || mp[j][i] == 'T') tmp++;
			else tmp = 0;
			res = getmax(res, tmp);
		}
		if(res == 4) return 4;
	}
	
	for(tmp=0, i=0; i<4; ++i){ // left up corner to right down corner 
		if(mp[i][i] == x || mp[i][i] == 'T') tmp++;
		else tmp = 0;
		res = getmax(res, tmp);
	}
	if(res == 4) return 4;

	for(tmp=0, i=0; i<4; ++i){ // right up corner to left down corner 
		if(mp[i][4-i-1] == x || mp[i][4-i-1] == 'T') tmp++;
		else tmp = 0;
		res = getmax(res, tmp);
	}
	return res;
}

int main(){
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T, cases;
	scanf("%d", &T);
	for(cases=1; cases<=T; ++cases){
		init();
		for(int i=0; i<4; ++i){
			scanf("%s", mp[i]);
			for(int j=0; j<4; ++j){
				if(mp[i][j] == '.') num_point ++;
			}
		}
		max_num = get_max_num('X');
		if(max_num == 4){
			printf("Case #%d: X won\n", cases);
		}else{
			max_num = get_max_num('O');
			if(max_num == 4){
				printf("Case #%d: O won\n", cases);
			}else if(num_point){
				printf("Case #%d: Game has not completed\n", cases);
			}else printf("Case #%d: Draw\n", cases);
		}
		
	}
	return 0;
}

