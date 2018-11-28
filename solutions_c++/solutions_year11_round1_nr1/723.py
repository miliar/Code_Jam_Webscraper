#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,q,i;
	long long n,d,g,pd,pg,val;
	cin >> t;
	int ok;
	for (q=1;q<=t;++q) {
		cin >> n >> pd >> pg;
		ok = 0;
		for (d=1;d<=min(100ll,n);++d) {
			if ((d * pd) % 100==0) {
				ok = 1;
				break;
			}
		}
		if ((pg==100 && pd!=100) || (pg==0 && pd!=0))
			ok = 0;

		cout << "Case #" << q << ": ";
		if (ok)
			cout << "Possible\n";
		else cout << "Broken\n";
		
	}
	
	return 0;
}