#include <cstdio>
#include <cstring>

using namespace std;

int T, C;
char s[8][8];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while (T--) {
		for (int i = 0; i < 4; i++)
			scanf("%s", s[i]);

		int ans = 0;
		int nx, no, nt;

		for (int i = 0; i < 4; i++){
			nx = no = nt = 0;
			for (int j = 0; j < 4; j++)
				if (s[i][j] == 'X') nx++;
				else if (s[i][j] == 'O') no++;
				else if (s[i][j] == 'T') nt++;
                        if (nx == 4 || nx == 3 && nt == 1) ans = 1;
			if (no == 4 || no == 3 && nt == 1) ans = 2;	
		}
		for (int i = 0; i < 4; i++){
			nx = no = nt = 0;
			for (int j = 0; j < 4; j++)
				if (s[j][i] == 'X') nx++;
				else if (s[j][i] == 'O') no++;
				else if (s[j][i] == 'T') nt++;
                        if (nx == 4 || nx == 3 && nt == 1) ans = 1;
			if (no == 4 || no == 3 && nt == 1) ans = 2;	
		}
		nx = no = nt = 0;
		for (int i = 0; i < 4; i++) 
			if (s[i][i] == 'X') nx++;
			else if (s[i][i] == 'O') no++;
			else if (s[i][i] == 'T') nt++;
		if (nx == 4 || nx == 3 && nt == 1) ans = 1;
		if (no == 4 || no == 3 && nt == 1) ans = 2;	
			
                nx = no = nt = 0;
		for (int i = 0; i < 4; i++) 
			if (s[i][3-i] == 'X') nx++;
			else if (s[i][3-i] == 'O') no++;
			else if (s[i][3-i] == 'T') nt++;
		if (nx == 4 || nx == 3 && nt == 1) ans = 1;
		if (no == 4 || no == 3 && nt == 1) ans = 2;	
		nt = 0;	
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			     if (s[i][j] == '.') nt++;
	        
	        if (ans == 0 && nt != 0) ans = 3;	
		printf("Case #%d: ", ++C);
		if (ans == 0) puts("Draw");
	        if (ans == 1) puts("X won");
		if (ans == 2) puts("O won");
	        if (ans == 3) puts("Game has not completed");
	}	
	return 0;
}
