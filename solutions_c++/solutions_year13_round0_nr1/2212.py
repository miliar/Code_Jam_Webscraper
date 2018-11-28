#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int i, j;
	char a[5][5];
	char b[150];
	int f, t;
	int h = 1;
	scanf ("%d", &t);
	while (t--) {
		getchar ();
		f = 3;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				a[i][j] = getchar ();
			}
			getchar ();
		}

		for (i = 0; i < 4; i++) {
			b['O'] = 0;
			b['X'] = 0;
			b['T'] = 0;
			b['.'] = 0;
			for (j = 0; j < 4; j++) {
				b[a[i][j]]++;
			}
			if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
				f = 0;
				break;
			} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
				f = 1;
				break;
			} else if (b['.'] > 0) {
				f = 2;
			}
		}	
		if (f > 1) {
			for (i = 0; i < 4; i++) {
                		b['O'] = 0;
                		b['X'] = 0;
                		b['T'] = 0;
               			b['.'] = 0;
                		for (j = 0; j < 4; j++) {
                       			b[a[j][i]]++;
                		}
               			if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
					f = 0;
					break;
				} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
					f = 1;
					break;
				} else if (b['.'] > 0) {
					f = 2;
				}
        		}
		}
		if (f > 1) {
                	b['O'] = 0;
                	b['X'] = 0;
                	b['T'] = 0;
                	b['.'] = 0;
	                for (j = 0; j < 4; j++) {
        	                b[a[j][j]]++;
                	}
                	if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
				f = 0;
			} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
				f = 1;
			} else if (b['.'] > 0) {
				f = 2;
			}
        	}	
		if (f > 1) {
                	b['O'] = 0;
                	b['X'] = 0;
                	b['T'] = 0;
                	b['.'] = 0;
	                for (j = 0; j < 4; j++) {
	                        b[a[j][3 - j]]++;
        	        }
                	if ((b['O'] == 4) || (b['O'] == 3 && b['T'] == 1)) {
				f = 0;
			} else if ((b['X'] == 4) || (b['X'] == 3 && b['T'] == 1)) {
				f = 1;
			} else if (b['.'] > 0) {
				f = 2;
			}
        	}
		if (!f) {
			printf ("Case #%d: O won\n", h++);	
		} else if (f == 1) {
			printf ("Case #%d: X won\n", h++);
		} else if (f == 2) {
			printf ("Case #%d: Game has not completed\n", h++);
		} else {
			printf ("Case #%d: Draw\n", h++);
		}
	}

	return 0;
}
