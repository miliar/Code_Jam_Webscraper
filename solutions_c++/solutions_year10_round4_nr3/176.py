#include <iostream>
#include <vector>
#include <cstdio>
#define MAXN 110
using namespace std;
vector<vector<bool> >t, tmpt;
int main() {
    int te;
    scanf("%d", &te);
    for(int z=1; z<=te; z++) {
	t.resize(MAXN);
	for(int i=0; i<MAXN; i++)
	    t[i].resize(MAXN,false);
	int r;
	scanf("%d", &r);
	while(r--) {
	    int X1, Y1, X2, Y2;
	    scanf("%d %d %d %d", &X1, &Y1, &X2, &Y2);
	    for(int i=X1; i<=X2; i++)
		for(int j=Y1; j<=Y2; j++)
		    t[i][j] = 1;
	}
	bool ok = false;
	int sol = 0;
	while(!ok) {
	    ok = true;
	    sol++;
	    tmpt = t;
	    for(int i=1; i<MAXN; i++)
		for(int j=1; j<MAXN; j++) {
		    if(!t[i][j] && t[i-1][j] && t[i][j-1])
			tmpt[i][j] = true;
		    if(!t[i-1][j] && !t[i][j-1])
			tmpt[i][j] = false;
		    if(tmpt[i][j])
			ok = false;
		}
	    /*for(int i=1; i<=6; i++) {
		for(int j=1; j<=6; j++) 
		    cout << t[j][i];
		cout << endl;
	    }*/
	    t = tmpt;
	    //cout << endl;
	}
	printf("Case #%d: %d\n", z, sol);
    }
    return 0;
}