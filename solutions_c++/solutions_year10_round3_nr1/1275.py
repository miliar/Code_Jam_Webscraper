#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <algorithm>
#define M 1010

using namespace std;

struct Point {
    int x, y;
    bool operator<(Point o) const {
	return x<o.x;
    }
} p[M];

int main(int argc, char **argv)
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int  t;
    int index = 1;
    scanf("%d", &t);
    while(t--) {
	int n;
	memset(p,0,sizeof(p));
	scanf("%d", &n);
	int i, j;
	for(i=0;i<n;i++) {
	    scanf("%d%d", &p[i].x, &p[i].y);
	}
	sort(p,p+n);
	int time = 0;
	for(i=0;i<n;i++) {
	    for(j=i+1;j<n;j++) {
		if(p[i].y>p[j].y) {
		    time++;
		}
	    }
	}
	printf("Case #%d: %d\n", index++, time);
    }
	return 0;
}
