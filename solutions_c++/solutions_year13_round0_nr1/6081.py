#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);	
	int T;
	scanf("%d",&T);
	for (int num = 1; num <= T; num++)
	{
		scanf("%*c");
		string s[4];
		for (int i = 0; i < 4; i++)
			cin >> s[i];
		
		bool draw = true;
		bool win = true;
		
		for (int i = 0; i < 4; i++) {
			//check horisontal
			char c1 = s[i][0];			
			if (c1 == 'T') c1 = s[i][1];
			win = true;
			if (c1 != '.') {
				for (int j = 1; j < 4; j++) {
					if (s[i][j] != c1 && s[i][j] != 'T') {
						win = false;
						break;
					}
				}
			}
			else {
				win = false;
				draw = false;
			}
			
			if (win) {
				//c1 win
				printf("Case #%d: %c won\n",num,c1);
				break;
			}
			
			//check vertical
			char c2 = s[0][i];
			if (c2 == 'T') c2 = s[1][i];
			win = true;
			if (c2 != '.') {
				for (int j = 1; j < 4; j++) {
					if (s[j][i] != c2 && s[j][i] != 'T') {
						win = false;
						break;
					}
				}
			}
			else {
				win = false;
				draw = false;
			}
			
			if (win) {
				//c2 win
				printf("Case #%d: %c won\n",num,c2);
				break;
			}
		}
		
		if (win) continue;
		
		//check diagonal
		char c3 = s[0][0];
		if (c3 == 'T') c3 = s[1][1];
		win = true;
		if (c3 != '.') {
			for (int i = 1; i < 4; i++)
			{
				if (s[i][i] != c3 && s[i][i] != 'T') {
					win = false;
					break;
				}
			}
		}
		else {
			win = false;
			draw = false;
		}
		
		if (win) {
			//c3 win
			printf("Case #%d: %c won\n",num,c3);
			continue;
		}
		
		char c4 = s[0][3];
		if (c4 == 'T') c4 = s[1][2];
		win = true;
		if (c4 != '.') {
			for (int i = 1; i < 4; i++)
			{
				if (s[i][3-i] != c4 && s[i][3-i] != 'T') {
					win = false;
					break;
				}
			}
		}
		else {
			win = false;
			draw = false;
		}
		
		if (win) {
			//c4 win
			printf("Case #%d: %c won\n",num,c4);
			continue;
		}
		
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (s[i][j] == '.')
					draw = false;
		
		if (draw) {
			//draw
			printf("Case #%d: Draw\n",num);
			continue;
		}
		else {
			//game has not completed
			printf("Case #%d: Game has not completed\n",num);
			continue;
		}
		
	}
}
