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


int main(){
	freopen ("2l.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int t = in();
	for(int i=0; i<t; ++i){
		int res = 0;
		vector <int> v1, v2, v3;
		int n = in(), s = in(), p = in();
		for(int j=0; j<n; ++j){
			int a = in(), m = a % 3;

			if(!m){
				if(p <= a/3) 
					++res; 
				else
					v1.push_back (a/3);
				continue;
			}				
			if (p <= a/3+1) 
					++res; 				
			else {
				if(m == 1){
					v2.push_back (a/3+1);
				}
				else{
					v3.push_back (a/3+1);
				}
			}
			
		}
		sort(v1.rbegin(),v1.rend());
		sort(v2.rbegin(),v2.rend());
		sort(v3.rbegin(),v3.rend());
		for(int j=0; j<v1.size ();++j){
			if(v1[j] >= (p-1) && s>0 && v1[j]>0){				
				++res;
				--s;
			}
			else break;
		}
		for(int j=0; j<v3.size(); ++j){
			if(v3[j] >= (p-1) && s>0 && v3[j]>0){
				++res;
				--s;
			}
			else break;
		}
		printf("Case #%d: %d\n", i+1, res);	
	}
	return 0;
}
