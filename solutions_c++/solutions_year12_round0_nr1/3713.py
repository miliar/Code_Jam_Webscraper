#include <cstdio>

static const int acMap[] = {
								0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 	0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ,
								0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 	0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ,

								' ', 0  , 0  , 0  , 0  , 0  , 0  , 0  ,		0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ,
								0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 	0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ,

								0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 	0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ,
								0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 	0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  ,

								0  , 'y', 'h', 'e', 's', 'o', 'c', 'v', 	'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k',
								'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 	'm', 'a', 'q', 0  , 0  , 0  , 0  , 0  ,
							};

int main(void) {
	char acBuf[128];
	unsigned int t, tc = 0;
	scanf("%u\n", &t);
	while (t--) {
		char* strPtr = fgets(acBuf, sizeof(acBuf), stdin);
		while (*strPtr >= ' ') {
			*strPtr = acMap[*strPtr];
			++strPtr;
		}
		*strPtr = 0;
		printf("Case #%u: %s\n", ++tc, acBuf);
	}
	return 0;
}
