#include <cstdio>
#include <algorithm>
#include <string.h>
using namespace std;

#define LMAX 110

int N;
char lineIn[LMAX], lineOk[LMAX];
int map[26] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

int main () {
	
	freopen ("tong.in", "r", stdin);
	freopen ("tong.out", "w", stdout);

	scanf ("%d\n", &N);
	for (int i = 1; N; N--, i++) {
		memset (lineIn, 0, sizeof (lineIn));
		memset (lineOk, 0, sizeof (lineOk));

		fgets (lineIn, LMAX, stdin);
        
		printf ("Case #%d: ", i);

		int len = strlen ( lineIn );
		for (int i = 0; i < len; i++)
			if (lineIn[i] == ' ') printf (" ");
			else if (lineIn[i] != '\n') printf ("%c", map[ lineIn[i] - 'a' ] + 'a');   	

		printf ("\n");
	}
	 
      
	return 0;
}
