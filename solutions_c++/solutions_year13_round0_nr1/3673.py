#include<cstdio>
using namespace std;
char s[5][5];
int c[256];
char winner = 0;
inline void test_line(int x0, int y0, int x1, int y1){
	c['T'] = c['O'] = c['X'] = 0;
	for(int i = 0; i < 4; i++){
		int x = (i * x0 + (3 - i) * x1) / 3;
		int y = (i * y0 + (3 - i) * y1) / 3;
		c[s[x][y]]++;
	}
	if(c['O']==4 || (c['O']==3 && c['T']==1)){
		winner = 'O';
	}
	if(c['X']==4 || (c['X']==3 && c['T']==1)){
		winner = 'X';
	}
}
int main(){
	int tests;
	scanf("%d",&tests);
	for(int t = 1; t <= tests; t++){
		for(int i = 0;i < 4;i++)
			scanf("%s", s[i]);
		c['.'] = 0;
		winner = 0;
		for(int i = 0; i < 4; i++){
			test_line(i, 0, i, 3);
			test_line(0, i, 3, i);
		}
		test_line(0, 0, 3, 3);
		test_line(0, 3, 3, 0);
			
		printf("Case #%d: ", t);
		if(winner)
			printf("%c won\n", winner);
		else
			printf(c['.']?"Game has not completed\n":"Draw\n");
		
	}
	return 0;
}
