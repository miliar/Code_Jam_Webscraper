#include <cstdio>
#include <algorithm>
using namespace std;

char array[50];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int nCases;
    scanf("%d", &nCases);
    for(int casenum = 1; casenum <= nCases; casenum++) {

	for(int i = 0; i < 25; i++)
	    array[i] = '0';
	scanf("%s", array+25);
	int l = strlen(array);
	next_permutation(array, array + l);
	printf("Case #%d: ", casenum);
	bool printing = false;
	for(int i = 0; i < l; i++) {
	    if(array[i] == '0') {
		if(printing)
		    printf("%c", array[i]);
	    }
	    else {
		printing = true;
		printf("%c", array[i]);
	    }
	}
	printf("\n");

    }
}
