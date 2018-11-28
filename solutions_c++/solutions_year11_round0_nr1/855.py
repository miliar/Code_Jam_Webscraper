#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
using namespace std;

int T;


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		string s;
		int x,last=0,y,p[2],t[2],n;

		cin >> n;

		p[0] = p[1] = 1;
		t[0] = t[1] = 0;
        	for(int i=0;i<n;i++){
			cin >> s >> x;
			y = s == "O";
			last = max(last , t[y] + abs(p[y] - x) ) + 1;
			t[y] = last;
			p[y] = x;
		}
		printf("Case #%d: ",_);
		cout << last << endl;
	}
	return 0;
}
