/*	Martuza
 * 	Islamic University
 *  martuza.cse@gmail.com
 * */

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
 
#include <cmath>
#include <iostream>
#include <fstream>
 
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <stack>

using namespace std;
 
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
 
#define FOR(i,n) for( i = 0 ; i<(n) ; i++)
#define RFOR(i,a,b)  for( i = (a) ; i<(b) ; i++)
#define CLR(a) memset(a, 0, sizeof(a))
#define MCLR(a) memset(a, -1, sizeof(a))
#define READ(input) freopen("input", "r", stdin);
#define WRITE(output) freopen("output", "w", stdout):
#define sf scanf
#define pf printf
#define re return
 
#define all(a) a.begin(),a.end()
#define pb push_back
#define vi vector<int>
#define qi queue<int>
#define pqi priority_queue<int>
#define msi map<string, int>
 
#define i64 long long
#define pi (2.0*acos(0.0))
#define eps (1e-11)
#define inf 1e9

int main(){
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int tc,kas = 0;
	scanf("%d", &tc);
	getchar();
	while(tc--){
		long n,s,p,c=0;
		scanf("%ld %ld %ld", &n, &s, &p);
		for(int i = 0; i < n; i++){
			long x;
			scanf("%ld", &x);
			if(x == 0 && p > 0) continue;
			int d = x/3;
			int r = x%3;
			if(r == 0){
				if(d >= p)
				c++;
				else if(s > 0 && d+1 >= p){
					s--;
					c++;
				}
			}
			else if(r == 1){
				if(d+1 >= p)
				c++;
			}
			else{
				if(d+1 >= p)
				c++;
				else if(s > 0 && d+2 >= p){
					s--;
					c++;
				}
			}
		}
		printf("Case #%d: %ld\n", ++kas, c);
	}
	
	
	return 0;
} 
