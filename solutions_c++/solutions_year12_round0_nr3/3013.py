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
	while(tc--){
		long x,y,h,cnt=0;
		scanf("%ld %ld", &x, &y);
		for(long l = x; l <= y; l++){
			h = l;
			int ar[100],j=0,c=0;
			while(h > 0){
				ar[j++] = h % 10;
				h /= 10;
				c++;
			}
			int t = 0;
			char at[100];
			for(int i = c-1; i >= 0; i--)
			at[t++] = ar[i] + '0';
			for(int i = 0; i < c-1; i++){
				long s = 0,k=0;
				char rr[100] = {0};
				for(int j = i+1; j < c; j++){
					rr[k++] = at[j];
				}
				for(int j = 0; j <= i; j++){
					rr[k++] = at[j];
				}
				s = atol(rr);
				if(s >= x && s <= y && s != l){
					//printf("%ld %ld\n", l , s);
					cnt++;
				}
			}                                                                                                                                                         
		}
		printf("Case #%d: %ld\n", ++kas, cnt/2);
	}
	
	
	return 0;
} 
