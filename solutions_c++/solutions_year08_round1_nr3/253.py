#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

char resposta[][10] = {"","", "027", "143", "751", "935", "607", "903", "991", "335", "047",
						"943", "471", "055", "447", "463", "991", "095", "607", "263", "151",
						"855", "527", "743", "351", "135", "407", "903", "791", "135", "647"};

int main() {
	int T, n, teste=1;;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		printf("Case #%d: %s\n", teste++, resposta[n]);
	}
	return 0;
}

