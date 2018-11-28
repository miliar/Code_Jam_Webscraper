#include<iostream>
#include<cstdio>

using namespace std;

int r;
int Test,pd,pg,a,b,g;
long long d;
int gcd(int x,int y){
	while (y!=0){
		r = x % y;
		x = y; y = r;
	}
	return x;
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> Test;
	for (int ii = 1;ii<=Test;++ii){
		printf("Case #%d: ",ii);
		cin >> d >> pd >> pg;
		if (pd != 0 &&  pg==0) {
			printf("Broken\n");
			continue;
		}
		if (pd != 100 && pg ==100) {
			printf("Broken\n");
			continue;
		}
		g = gcd(pd,100);
		b = 100/g;
		if (b>d) {
			printf("Broken\n");
			continue;
		}
		printf("Possible\n");
	}
	return 0;
}
