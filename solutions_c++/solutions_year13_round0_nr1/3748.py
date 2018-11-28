#include <iostream>
#define forn(i, n) for(int i = 0; i < int(n); i++)
using namespace std;
char a[4][4];
bool won(char c){
	forn(i, 4){
		bool yes = true;
		forn(j, 4){
			if(a[i][j] != c && a[i][j] != 'T')
				yes = false;
		}
		if(yes)
			return true;
	}
	forn(i, 4){
		bool yes = true;
		forn(j, 4){
			if(a[j][i] != c && a[j][i] != 'T')
				yes = false;
		}
		if(yes)
			return true;
	}
	bool yes = true;
	forn(i, 4)
		if(a[i][i] != c && a[i][i] != 'T')
			yes = false;
	if(yes)
		return true;
	yes = true;
	forn(i, 4)
		if(a[i][4-i-1] != c && a[i][4-i-1] != 'T')
			yes = false;
	return yes;
}
bool draw(){
	bool is_draw = true;
	forn(i, 4)
		forn(j, 4){
			if(a[i][j] == '.')
				is_draw = false;
		}
	if(is_draw && !won('X') && !won('O'))
		return true;
	return false;
}
bool good(){
	int cntx = 0, cnto = 0;
	forn(i, 4)
		forn(j, 4){
			if(a[i][j] == 'X')
				cntx++;
			if(a[i][j] == 'O')
				cnto++;
		}
	if(cntx == cnto){
		return !won('X');
	}
	if(cntx == cnto + 1)
		return !won('O');
	return false;
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	forn(test, tests){
		scanf("\n");
		forn(i, 4)
			scanf("%s\n", a[i]);
		printf("Case #%d: ", test + 1);
		if(good()) {
			if(won('X')){
				puts("X won");
			}else{
				if(won('O')){
					puts("O won");
				}else{
					if(draw()){
						puts("Draw");
					}else{
						puts("Game has not completed");
					}
				}
			}
		}else
			throw;
	}
	return 0;
}