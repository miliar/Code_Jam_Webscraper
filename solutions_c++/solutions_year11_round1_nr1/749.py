#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

const long maxn=10000;

long long n;
int pd,pg;

int gcd(int a,int b) {
	if (b==0) return a;
	else return gcd(b,a%b);
}

bool solve() {
	long long Td,Wd;
	if (pd==0) {
		Wd=0;
		Td=1;
	}
	else {
		int t=gcd(100,pd);
		Wd=pd/t;
		Td=100/t;
	}
	if (Td>n) return false;

	long long Wg=pg*maxn;
	long long Tg=100*maxn;
//cout<<Wd<<" "<<Td<<" *** "<<Wg<<" "<<Tg<<endl;
	if (Wd<=Wg&&Td<=Tg&&Td-Wd<=Tg-Wg) return true;
	else return false;
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>n>>pd>>pg;
		printf("Case #%d: ",++kase);
		if (solve()) cout<<"Possible"<<endl;
		else cout<<"Broken"<<endl;
	}
	return 0;
}
