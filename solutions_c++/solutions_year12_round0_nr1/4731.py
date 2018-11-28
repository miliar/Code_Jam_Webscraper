/*---------------------------
Author		: Md. Atiqul Islam (deadlineruhe)
University 	: AIUB
E-mail  	: deadlineruhe@gmail.com
Problem Name:
Algorithm  	:
Complexity  :
Difficulty  :
-----------------------------*/
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <deque>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <algorithm>

using namespace std;
//Constant Declaration

typedef long long li;

const int SIZ = 100000;
const int INF = (1<<29);
const double EPS = 1e-11;
const double PI = acos(-1.0);
/*--------------------------*/
// some essential funtion
/*----------------------------------*/
#define BC(i) (P[i>>6] & (1<<((i>>1) & 31)))
#define BS(i) (P[i>>6] |= (1<<((i>>1) & 31)))
#define mem(P, a) memset(P, a, sizeof(P))
#define clear_v(V, n) for(i = 0; i < n; i++)V[i].clear()
/*----------------------------------*/
int MAX(int a,int b){	return a>b?a:b;  }
int MIN(int a,int b){	return a<b?a:b;  }
int GCD(int a,int b){	while( b ){b ^= a ^= b ^= a %= b;}	return a;}
/*----------------------------------*/

int main(){
	double cl = clock();
	//freopen("A.in","r",stdin);
	//freopen("A.ans","w",stdout);
	char M[200], A[200];
	M['a' - 'a'] = 'y', M['b' - 'a'] = 'h', M['c' - 'a'] = 'e', M['d' - 'a'] = 's', M['e' - 'a'] = 'o', M['f' - 'a'] = 'c';
	M['g' - 'a'] = 'v', M['h' - 'a'] = 'x', M['i' - 'a'] = 'd', M['j' - 'a'] = 'u', M['k' - 'a'] = 'i', M['l' - 'a'] = 'g';
	M['m' - 'a'] = 'l', M['n' - 'a'] = 'b', M['o' - 'a'] = 'k', M['p' - 'a'] = 'r', M['q' - 'a'] = 'z', M['r' - 'a'] = 't';
	M['s' - 'a'] = 'n', M['t' - 'a'] = 'w', M['u' - 'a'] = 'j', M['v' - 'a'] = 'p', M['w' - 'a'] = 'f', M['x' - 'a'] = 'm';
	M['y' - 'a'] = 'a', M['z' - 'a'] = 'q';
	int ind, test, i, l;
	scanf("%d", &test);
	getchar();
	for( ind = 1; ind <= test; ind++){
		gets(A);
		l = strlen( A );
		for( i = 0; i < l; i++){
			if( A[i] != ' ' ) A[i] = M[A[i] - 'a']; 
		}
		printf("Case #%d: %s\n", ind, A);
	}
	cl = clock() - cl;
	fprintf(stderr,  "Total Time: %.2f\n", cl/CLOCKS_PER_SEC);
	return 0;
	
}
