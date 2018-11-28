#include <iostream>
#include <cstdio>

using namespace std;

#define see(x) cout<<#x<<" "<<x<<endl

char a[4][4];

bool isWon(char q) {
	for(int i = 0; i < 4; ++i) {
		bool flag = true;
		for(int j = 0; j < 4; ++j)
			if(a[i][j] != q && a[i][j] != 'T')
				flag = false;
		if(flag)
			return true;
	}

	for(int j = 0; j < 4; ++j) {
		bool flag = true;
		for(int i = 0; i < 4; ++i)
			if(a[i][j] != q && a[i][j] != 'T')
				flag = false;
		if(flag)
			return true;
	}

	bool flag = true;
	for(int i = 0; i < 4; ++i) {
		if(a[i][i] != q && a[i][i] != 'T')
			flag = false;
	}
	if(flag)
		return true;

	flag = true;
	for(int i = 0; i < 4; ++i) {
		if(a[i][3 - i] != q && a[i][3 - i] != 'T')
			flag = false;
	}
	if(flag)
		return true;


}


int main() {
	freopen("inputA2.txt", "r", stdin);
	freopen("outputA2.txt", "w", stdout);
	int t, T;
	char q;
	scanf("%d", &T);
	for(t = 1; t <= T; ++t) {

		bool isComplete = true;

		if(t!=1)
			scanf("%c", &q);
		for(int i = 0; i < 4; ++i) {
			scanf("%c", &q);
			for(int j = 0; j < 4; ++j) {
				scanf("%c", &a[i][j]);
				if(a[i][j] == '.')
					isComplete = false;
			}
		}

		if(isWon('X'))
			printf("Case #%d: X won\n", t);
		else if(isWon('O'))
			printf("Case #%d: O won\n", t);
		else if(isComplete)
			printf("Case #%d: Draw\n", t);
		else
			printf("Case #%d: Game has not completed\n", t);


	}

}