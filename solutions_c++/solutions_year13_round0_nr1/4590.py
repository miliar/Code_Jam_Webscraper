#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef pair<int, char> pl;

char arr[5][5];

bool test(char a, char b, char c, char d)
{
	if (a == 'T')
			return (b == c) && (b == d) && (b != '.');
	else if (b == 'T')
			return (a == c) && (a == d) && (a != '.') ;
	else if (c == 'T')
			return (a == b) && (a == d) && (a != '.');
	else if (d == 'T')
			return (a == b) && (a == c) && (a != '.');
	else		
			return (a == b) && (a == c) && (a == d) && (a != '.');
}


pl func()
{
		int i, j, state = -1;
		char ch;
		bool flag = true;

		for (i = 0; i < 4; i++) {
			
			flag = test(arr[i][0], arr[i][1], arr[i][2], arr[i][3]);

			if (!flag)
					continue;

			 ch = arr[i][0];

			 ch = (ch == 'T') ? arr[i][1] : ch;
				return pl(1, ch);
		}
								

		// for column 
		for (i = 0; i < 4; i++) {
			
			flag = test(arr[0][i], arr[1][i], arr[2][i], arr[3][i]);

			if (!flag)
					continue;

			 ch = arr[0][i];

			 ch = (ch == 'T') ? arr[1][i] : ch;
				return pl(1, ch);
		}
		
			// for diagonal
			flag = test(arr[0][0], arr[1][1], arr[2][2], arr[3][3]);

					if (flag) {
							 ch = arr[0][0];

							 ch = (ch == 'T') ? arr[1][1] : ch;
							return pl(1, ch);
					}
			

			flag = test(arr[0][3], arr[1][2], arr[2][1], arr[3][0]);

				if (flag) {
					 ch = arr[0][3];

					 ch = (ch == 'T') ? arr[1][2] : ch;
					return pl(1, ch);
				}
		
				bool full = true;

				for (i  = 0; i < 4; i++) {
						for (j = 0; j < 4; j++) {
								if (arr[i][j] == '.') {
										full = false;
										break;
								}
						}
						if (!full)
								break;
				}
					
			if (!full)
				return pl(2, ch); // incomplete

			return pl(-1, ch); 
}


int main()
{
	int test, i, j, t = 0;	
	
	int st;
	pl pa;
	char ch;

		
	scanf("%d", &test);
	getchar();

	for (t = 1; t <= test; t++) {
		
		for (i = 0; i < 4; i++) 
				scanf("%s", arr[i]);
			
		pa = func();
		st = pa.first;
		ch = pa.second;

		if (st == -1) 
				printf("Case #%d: Draw\n", t);
		else if (st == 2)
				printf("Case #%d: Game has not completed\n", t);
		else if(st == 1)
				printf("Case #%d: %c won\n", t, ch);						
		
	}


	return 0;
}
				
