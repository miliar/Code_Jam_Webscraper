#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <typeinfo>
#include <set>
#include <cctype>
#include <locale>
#include <utility>
#include <map>
#include <iterator>
#include <cstring>
using namespace std;

const double eps = 1e-6; 

int in() {
	int a;
	scanf("%d", &a);
	return a;
}

double din() {
	double a;
	scanf("%lf", &a);
	return a;
}

int gcd(int a, int b) {
	while(b){
		a%=b;
		swap(a,b);
	}
	return a;
}

int lcm(int a, int b) {
	return a / gcd(a, b) * b;
}

int nextn (int a, int b){
    int i = a%10;
    a /= 10;
    a += i * pow(10, b-1.);
    return a;
}

int main(){
	freopen("3.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t = in();
	for(int i = 0; i < t; ++i){
		int a = in(), b = in(), s = 0, n = a, res = 0;
		while(n > 0){
			++s;
			n /= 10;
		}
		for(int j = a; j <= b; ++j){
			int c = j;
			set <int> r;
			for(int k = 1; k < s; ++k){
				n = nextn(c,s);
				if (n > j && n >= a && n <= b) 
					r.insert (n);
				c = n;
			}
			res += (int)r.size();
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}
