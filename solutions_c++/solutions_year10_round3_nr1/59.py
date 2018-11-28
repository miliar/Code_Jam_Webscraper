//============================================================================
// Name        : A.cpp
// Author      : Artem A. Khizha
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include <utility>
using namespace std;

bool intersects(pair<int, int> a, pair<int, int> b)   {
    return (a.first < b.first && a.second > b.second) ||
            (a.first > b.first && a.second < b.second);
}

int main() {
    int tnum;
	scanf("%d", &tnum);
	for (int ti = 1; ti <= tnum; ti++) {
	    int n;
	    scanf("%d", &n);
	    pair<int, int> w[1000];
	    for (int i = 0; i < n; i++)
	        scanf("%d%d", &w[i].first, &w[i].second);
	    int cnt = 0;
	    for (int i = 0; i < n; i++)
	        for (int j = 0; j < i; j++)
	            if (intersects(w[i], w[j]))
	                cnt++;
	    printf("Case #%d: %d\n", ti, cnt);
	}
	return 0;
}
