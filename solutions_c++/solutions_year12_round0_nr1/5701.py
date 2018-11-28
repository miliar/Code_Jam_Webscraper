/*
A
Author: WANG Yuanjie
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())


int main()
{
	freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);
	int T;
	scanf("%d",&T);
	char c;
	for (int ii = 0; ii < T; ++ii) {
        printf("Case #%d: ",ii+1);
        if (ii==0) scanf("%c",&c);
		do {
			
            if (scanf("%c",&c)==EOF) break;
            
			switch ( c ) {
				case 'a' : printf("y"); break;
				case 'b' : printf("h"); break;
				case 'c' : printf("e"); break;
				case 'd' : printf("s"); break;
				case 'e' : printf("o"); break;
				case 'f' : printf("c"); break;
				case 'g' : printf("v"); break;
				case 'h' : printf("x"); break;
				case 'i' : printf("d"); break;
				case 'j' : printf("u"); break;
				case 'k' : printf("i"); break;
				case 'l' : printf("g"); break;
				case 'm' : printf("l"); break;
				case 'n' : printf("b"); break;
				case 'o' : printf("k"); break;
				case 'p' : printf("r"); break;
				case 'q' : printf("z"); break;
				case 'r' : printf("t"); break;
				case 's' : printf("n"); break;
				case 't' : printf("w"); break;
				case 'u' : printf("j"); break;
				case 'v' : printf("p"); break;
				case 'w' : printf("f"); break;
				case 'x' : printf("m"); break;
				case 'y' : printf("a"); break;
				case 'z' : printf("q"); break;
				case ' ' : printf(" "); break;
				default : 
				{
					printf("%c",c);     
				}
				
			} 
			
		} while(c!='\n');

	//	int arr[2010];
	//	printf("Case #%d: ",ii+1);
		/*for (int i = 0; i < n; ++i) {
			scanf("%d",arr+i);
			for (int j = 0; j < i; ++j) {
				if( arr[i]+arr[j] == c )
					printf("%d %d\n",j+1,i+1);
			}
		}*/
	}
	return 0;
}
