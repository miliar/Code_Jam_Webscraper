#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T, N, K, x;
    cin >> T;
    for( int c = 1; c <= T; c++ )
    {
        printf("Case #%d:", c);
        scanf("%d %d", &N, &K);
        
        int p = 1 << N;
        if( K % p - p + 1 == 0  ) printf(" ON");
        else printf(" OFF");
        printf("\n");
    }
	return 0;
}
