#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <ctime>
#include <utility>
#include <stdexcept>

using namespace std;

int main()
{
	freopen("A-in.in", "r", stdin);
    freopen("A-out.out", "w", stdout);
    int n, s = 0;
	int a, b;
	scanf("%d", &n);
	while( n-- ) {
		scanf("%d%d", &a, &b);
		int t = (1<<a);
		t = b%t;
		printf("Case #%d: ", ++s);
		if( t == ((1<<a)-1) ) {
		    puts("ON");
		}
		else
            puts("OFF");
	}
	return 0;
}
