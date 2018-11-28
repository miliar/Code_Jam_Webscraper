#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <string>
#include <sstream>
#include <cassert>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<string> VS;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
#define ALL(A) (A).begin(),(A).end()
#define SIZE(A) (int)(A).size()
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

/*
A diamond of size k is 2k-1 lines of digits, 0-9, separated by single spaces, organized in the following way:

    * Line i (1 ≤ i ≤ k) contains k-i spaces, then i digits separated by single spaces.
    * Line i (k < i < 2k) contains i-k spaces, then 2k-i digits separated by single spaces.

An elegant diamond of size k is a diamond of size k with the following two symmetry properties:

    * Horizontal symmetry: Let ci be the number of digits on line i.
    The jth digit on line i (where j=1 for the first digit) must be the same as the ci+1-jth digit.
    * Vertical symmetry:
    The jth digit on line i (where i=1 for the first line) must be the same as the jth digit on line 2k-i.

A diamond of size k can be enhanced by adding digits to it. The result of enhancing a diamond of size k has the following properties:

    * The result is a diamond of size ≥ k.
    * The original diamond is part of the result. In other words, there exist some X and some Y such that, for all values of i and j such that there's a jth digit on the ith line of the original, the j+Xth digit on the i+Yth line of the result is the same as the jth digit on the ith line of the original.

The cost of enhancing a diamond is equal to the number of digits in the result of the enhancement, minus the number of digits in the original diamond.

*/

vector<int> input[300];
vector<int> diamond[300];
int k, n;

int check(int X,int Y,int j) {
	int m = 2 * j - 1;
    FOR(i,1,m) {
        diamond[i].clear();
        int q = i > j ? 2 * j - i : i;
        REP(p,q) diamond[i].PB(-1);
    }

    FOR(i,1,n) {
    	//int odd = X + Y > (j - k) ? X + Y - (j - k) : 0;
        REP(p,SIZE(input[i])) 
        {
        	int a = i;
        	int b = p + max(a-k,0);
        	int c = a + X + Y;
        	int d = b + Y - max(c-j,0);
        	
        	//printf("%d %d (%d %d)-> (%d %d) %d %d\n",i,p,X,Y,a,b,c,d);
		
			assert(!(d>SIZE(diamond[c])||d < 0));
		
            diamond[c][d] = input[i][p];
        }
    }
/*
	FOR(i,1,m)
	{
		REP(p,SIZE(diamond[i]))
			printf("%d ",diamond[i][p]);
		printf("\n");
	}cout << endl;
	*/
	
    FOR(i,1,m) {
        int ci = SIZE(diamond[i]);
        REP(p,ci) {
        	//printf("%d %d (%d %d) | (%d %d)\n",i,p,i,ci-1-p,m+1-i,p);
        	if ( diamond[i][p] == -1) continue;
            if ( diamond[i][p] != diamond[i][ci-1-p] && diamond[i][ci-1-p] != -1 ) return 0;
            if ( diamond[i][p] != diamond[m+1-i][p] && diamond[m+1-i][p] != -1 ) return 0;
        }
    }
    
    return 1;
}

void solve(int test_number) {
    scanf("%d",&k);
    n = 2 * k - 1;

    FOR(i,1,n) {
        input[i].clear();
        int m = i > k ? 2 * k - i : i;

        FOR(j,1,m) {
            int x;
            scanf("%d",&x);
            input[i].PB(x);
        }
    }

	int res = 1<<30;
	
	int lo = k;
	int hi = 2*k+1;
	
	while(lo <= hi)
	{
		int mid = lo + hi;
		mid /= 2;
	
    FOR(j,k,1000) {
        int m = 2 * j - 1;

        FOR(x,0,j-k)
        FOR(y,0,j-k) {
			if( check(x,y,j) )
			{
				res = j * j - k * k;
				goto koniec;
			}
        }

    }
	koniec:;
    printf("Case #%d: %d",test_number,res);
    cout << endl;
}





int main() {
    int number_of_tests;
    scanf("%d",&number_of_tests);
    FOR(test_number,1,number_of_tests) solve(test_number);
    return 0;
}





/*

#define MMAX(X,Y) ((X) = max((X),(typeof(X))(Y)))
#define MMIN(X,Y) ((X) = min((X),(typeof(X))(Y)))

#define BITCNT(X) (__builtin_popcount(X))
#define BIT(X,Y) ((X)&(1<<(Y)))
#define FBIT(X) (__builtin_ctz(X))
#define LBIT(X) (31 - __builtin_clz(X))

void solve(int testNum) {
	printf("Case #%d:",testNum);
}

int main() {
	int tests;
	scanf("%d",&tests);
	FOR(test,1,tests) solve(test);
	return 0;
}
*/















