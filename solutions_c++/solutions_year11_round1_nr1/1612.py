#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <list>
#include <bitset>
#include <complex>
#include <list>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define pb push_back
#define SIZE(x) ((int)(x.size()))
#define LENGTH(x) ((int)(x.length()))
#define PI 3.14159265358979323846264338327950288

typedef long long ll;
typedef unsigned long long ull;
int TS,pd,pg,limit;

void init(){
	//freopen("AA.in", "r", stdin);
	//freopen("AA.out", "w", stdout);
	cin>>TS;
	for (int testId=1; testId<=TS; ++testId) {
		cin>>limit>>pd>>pg;
		bool can=false;
		for (int i=1; i<=limit; ++i) {
			if( (i*pd)%100 == 0 ){
				int wd=(i*pd)/100;
				if (pg==0) {
					if (wd==0) {
						can=true;
						break;
					}
				}
				else {
					if (pg==100) {
						if (wd==i) {
							can=true;
							break;
						}
					}else {
						can=true;
						break;
					}

				}
			}
		}
		if (can) {
			cout << "Case #"<<testId<<": Possible"<<endl;
		}else {
			cout << "Case #"<<testId<<": Broken"<<endl;
		}
	}
}

int main(){
	init();
	return 0;
}
