#include <iostream>
using namespace std;

int inline Xc2 (int r) {
	switch (r) {
	case 2:		return 1;		break;
	case 3:		return 3;		break;
	case 4:		return 6;		break;
	case 5:		return 10;		break;
	case 6:		return 15;		break;
	case 7:		return 21;		break;
	default:	exit(9);
	}
}

int main(int argc, char *argv[]) {
	FILE *fp;
	if((fp=fopen(argv[1],"r"))==NULL) {
		printf("Cannot open file.\n");
		exit(1);
	}

	int A, B, X, x, D, d, D10, SetSize;
	int T, i, Sol;
	fscanf_s(fp, "%d%*c", &T);
	for (i=1; i<=T; i++) {
		bool Used[1000000] = {0};
		Sol = 0;
		fscanf_s(fp, "%d%d%*c", &A, &B);

		if ( B < 10 ) {
			printf ("Case #%d: 0\n", i);
			continue;
		}
		else if ( B < 100 )		{ D = 2; D10 = 10;		}
		else if ( B < 1000 )	{ D = 3; D10 = 100;		}
		else if ( B < 10000 )	{ D = 4; D10 = 1000;	}
		else if ( B < 100000 )	{ D = 5; D10 = 10000;	}
		else if ( B < 1000000 ) { D = 6; D10 = 100000;  }
		else if ( B < 2000000 ) { D = 7; D10 = 1000000; }
		else {}

		for (X=A; X<=B; X++) {
			if (Used[X-A])	continue;
			SetSize = 1;
			Used[X-A] = 1;
			for (x=X, d=1; d<D; d++) {
				x = (x % D10) * 10 + (x / D10);
				if (x >= A && x <= B && !Used[x-A]) {
					SetSize++;
					Used[x-A] = 1;
				}
			}
			if (SetSize > 1)
				Sol += Xc2(SetSize);
		}
		printf ("Case #%d: %d\n", i, Sol);
	}
	return 0;
}