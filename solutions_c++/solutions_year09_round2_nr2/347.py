#include <algorithm>
#include <string>
#include <stdio.h>
using namespace std;


char tmp[100];
char tmp2[100];
int len;
int main()
{
    int icase, ncase;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    scanf("%d", &ncase);
	for (icase=0; icase<ncase; ++icase) {
		scanf("%s", tmp+1);
		tmp[0] = '0';
		len = strlen(tmp);
		strcpy(tmp2, tmp);
		printf("Case #%d: ", icase+1);
		if (next_permutation(&tmp[1], &tmp[len])) 
			printf("%s\n", tmp+1);
		else {
			next_permutation(&tmp2[0], &tmp2[len]);
			printf("%s\n", tmp2);
		}
	}

        
    return 0;
}    

