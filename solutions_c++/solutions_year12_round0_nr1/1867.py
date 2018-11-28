#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

char mapping[27] = "yhesocvxduiglbkrztnwjpfmaq";

char buf[1 << 7];

int main() {
	int t = 1, tc;
	for(scanf("%d\n", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);

        gets(buf);

        int l = strlen(buf);
        for(int i = 0; i < l; i++)
            printf("%c", buf[i] == ' ' ? ' ' : mapping[buf[i]-'a']);

        printf("\n");
	}
	return 0;
}
