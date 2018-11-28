#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back

#define epr(...) fprintf(stderr, __VA_ARGS__

const int maxn = -1;
const int inf = 1e9;

char a[10][10];


int main(){
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int n, t;
    bool flag, flagX, flagO, flagX1, flagO1;
    n = 4;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++){
	for(int i = 0; i < n; i++)
	    scanf("%s", a[i]);
	scanf("\n");
	flag = 1;
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < n; j++)
		if (a[i][j] == '.')
		    flag = 0;

	flagX1 = flagO1 = 0;
	
	for(int i = 0; i < n; i++){
	    flagX = flagO = 1;
	    for(int j = 0; j < n; j++){
		if (a[i][j] != 'X' && a[i][j] != 'T')
		    flagX = 0;
		if (a[i][j] != 'O' && a[i][j] != 'T')
		    flagO = 0;	   
	    }
	    if (flagX) flagX1 = 1;
	    if (flagO) flagO1 = 1;
	}
	for(int j = 0; j < n; j++){
	    flagX = flagO = 1;
	    for(int i = 0; i < n; i++){
		if (a[i][j] != 'X' && a[i][j] != 'T')
		    flagX = 0;
		if (a[i][j] != 'O' && a[i][j] != 'T')
		    flagO = 0;	   
	    }
	    if (flagX) flagX1 = 1;
	    if (flagO) flagO1 = 1;
	}
	flagX = flagO = 1;
	for(int i = 0; i < n; i++){
	    if (a[i][i] != 'X' && a[i][i] != 'T')
		flagX = 0;
	    if (a[i][i] != 'O' && a[i][i] != 'T')
		flagO = 0;	   
	}
	if (flagX) flagX1 = 1;
	if (flagO) flagO1 = 1;
	
	flagX = flagO = 1;
	for(int i = 0; i < n; i++){
	    if (a[n - i - 1][i] != 'X' && a[n - i - 1][i] != 'T')
		flagX = 0;
	    if (a[n - i - 1][i] != 'O' && a[n - i - 1][i] != 'T')
		flagO = 0;	   
	}
	if (flagX) flagX1 = 1;
	if (flagO) flagO1 = 1;
	assert(flagX1 != 1 || flagO1 != 1);
	if (flagX1)
	    printf("Case #%d: X won\n", tt + 1);
	if (flagO1)
	    printf("Case #%d: O won\n", tt + 1);
	
	
	if (flagO1 != 1 && flagX1 != 1){
	    if (flag)
		printf("Case #%d: Draw\n", tt + 1);
	    else
		printf("Case #%d: Game has not completed\n", tt + 1);
	}
	
    }
    
    
    
    return 0;
}