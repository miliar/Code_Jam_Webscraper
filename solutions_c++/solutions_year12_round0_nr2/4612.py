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
struct surprising{
	int flag1, flag2, flag3, flag4;
}P[110];
int n, s, p;
int d[110];
int Memo[110][110], St[110][110], cc = 0;
int f(int i, int s){
	if(s < 0) return -INF;
	if(i == n) return (s == 0)? 0:-INF;
	int &res = Memo[i][s];
	int &st = St[i][s];
	if(st == cc) return res;
	st = cc;
	int r1, r2, r3, r4;
	r1 = r2 = r3 = r4 = 0;
	if(P[i].flag1) r1 = f(i + 1, s - 1) + 1;
	if(P[i].flag2) r2 = f(i + 1, s) + 1;
	if(P[i].flag3) r3 = f(i + 1, s - 1);
	if(P[i].flag4) r4 = f(i + 1, s);
	return res = MAX(r1, MAX( r2, MAX( r3, r4)));
}
int main(){
	double cl = clock();
	freopen("B_l.in","r",stdin);
	freopen("B_l.ans","w",stdout);
	int ind, test, a, b, c, i, j, res;
	int A[110];
	scanf("%d", &test);
	for( ind = 1; ind <= test; ind++){
		scanf("%d %d %d", &n, &s, &p);
		for(i = 0; i < n; i++)scanf("%d", &A[i]);
		res = 0;
		bool flag;
		for(i = 0; i < n; i++){
			P[i].flag1 = P[i].flag2 = P[i].flag3 = P[i].flag4 = 0;
			for(a = 0; a <= 10; a++){
				for(b = ((a - 2) >= 0)? a - 2 : 0; b <= 10 && abs(a - b) <= 2; b++){
					c = A[i] - a - b;
					if(abs(a - c) > 2 || abs(b - c) > 2 || c < 0) continue;
					if(a >= p || b >= p || c >= p){
						if(abs(a - b) == 2 || abs(b - c) == 2 || abs(c - a) == 2) P[i].flag1 = 1;
						else P[i].flag2 = 1;
					}else if(abs(a - b) == 2 || abs(b - c) == 2 || abs(c - a) == 2) P[i].flag3 = 1;
					else P[i].flag4 = 1;
				}
			}
		}
		cc++;
		res = f(0, s);
		printf("Case #%d: %d\n", ind, res);
	}
	cl = clock() - cl;
	fprintf(stderr,  "Total Time: %.2f\n", cl/CLOCKS_PER_SEC);
	return 0;
	
}
