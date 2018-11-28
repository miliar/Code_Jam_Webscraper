#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <map>
#include <limits.h>
#include <signal.h>

#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ROF(i, a, b) for ( i = a; i >= b; i-- )
#define ALL(v) (v).begin(), (v).end()
#define MAX(a, b) ((a) >= (b) ? (a) : (b))
#define MIN(a, b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SWAP(a, b) typeof(a) T; T=a; a=b; b=T;
#define LL long long
using namespace std;
//using namespace __gnu_cxx;
LL GCD(LL a,LL b) {
	  while (b > 0) {
		      a = a % b;    
			  //Swapping a and b	
			  a ^= b;    
			  b ^= a;	
			  a ^= b; 
	  } 
	  return a;
}
int main()
{
	int pg , pd;
	LL N;
	int test;
	cin >> test;
	LL lost1 , lost2 , x1 , y1;
	LL den1,den2;
	LL num1,num2;
	LL gc1,gc2;
	int t;
	t = 0;
	while(test--) {
	t++;
		scanf("%lld%d%d",&N,&pd,&pg);
//		cout << N << endl;	
		gc1 = GCD(pd,100);
		num1 = pd / gc1;
		den1 = 100/gc1;
		LL i = den1;
		bool f = 0;
		LL lost;
	//	cout << i << " " << N << endl;	
		
		if(pd == 0) {
			f = 1;
			if(pg == 100) {
				f = 0;
			}
		}
		else {
			if(pg == 0) {
				f = 0;
			}
			else {
				while(i <= N) {
	//			cout <<endl << i << endl;
					y1 = i;
					x1 = (num1*y1)/den1;
						
					lost = y1 -x1;
			
					if(lost > 0 && pg == 100) {
						f = 0;
						break;
					}
					f = 1;
					i = i+den1;
					break;
				} 
			}
		}
		if(f) {
			printf("Case #%d: Possible\n",t);
		}
		else {
			printf("Case #%d: Broken\n",t);	
		}
	}					
	return 0;
}
