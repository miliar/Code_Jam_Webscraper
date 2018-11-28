/*
Author		:taser ghar
Algorithm	:	
Complexity	:	
Problem		:
Comments	:balir badh amar venge gele hai , taser ghar jeno hoibe shohai
LightOJ		:)
*/
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define inf 987654321
#define pi (2*acos(0.0))
#define eps 1e-7
using namespace std;
int max( int a, int b ) {
	if( a > b ) return a ; 
	return b;
}

struct surprising{
	int flag1, flag2, flag3, flag4;
}P[110];

int n, s, p;
int d[110];
int memo[110][110], St[110][110], cc = 0;
int f(int i, int s){
	if(s < 0) return -inf;
	if(i == n) return (s == 0)? 0:-inf;
	int &res = memo[i][s];
	int &st = St[i][s];
	if(st == cc) return res;
	st = cc;
	int r1, r2, r3, r4;
	r1 = r2 = r3 = r4 = 0;
	if(P[i].flag1) r1 = f(i + 1, s - 1) + 1;
	if(P[i].flag2) r2 = f(i + 1, s) + 1;
	if(P[i].flag3) r3 = f(i + 1, s - 1);
	if(P[i].flag4) r4 = f(i + 1, s);
	return res = max(r1, max( r2, max( r3, r4)));
}
int main(){

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
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


	return 0;
	
}
