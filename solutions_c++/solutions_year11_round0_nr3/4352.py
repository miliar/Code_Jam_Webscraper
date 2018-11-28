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
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <algorithm>

using namespace std;
//Constant Declaration

const int SIZ=25;
const int INF=(1<<29);
const double EPS = 1e-11;
const double PI = acos(-1.0);
/*--------------------------*/
// some essential funtion
/*----------------------------------*/
void SWAP(int &a,int &b){	int t=a;a=b;b=t;}
int MAX(int a,int b){	return a>b?a:b;  }
int MIN(int a,int b){	return a<b?a:b;  }
int GCD(int a,int b){	while(b){b ^= a ^=b ^= a %=b;}	return a;}
/*----------------------------------*/
int po(int n,int j){
	int res = 1;
	while(j--) res *= n;
	return res;
}
int b(int n,int p){
	int a,b,j = 0,res = 0;
	while(n || p){
		a = n % 2;
		b = p % 2;
		res += (a ^ b) * po(2, j++);
		n >>= 1;
		p >>= 1;
	}
	return res;
}
int main()
{
	freopen("C-small-attempt6.in","r",stdin);
	freopen("C.out","w",stdout);
	int ind, test,n,i,sum,p,s,flag,j,max,s1;
	int ar[SIZ];
	scanf("%d",&test);
	for(ind = 1; ind <= test ;ind++){
		scanf("%d", &n);
		for(i = 0,sum = 0; i < n; i++){
			scanf("%d",&ar[i]);
			sum += ar[i];
		}
		for( i = 1,max = -INF; i < (1<<n) - 1; i++){
			p = s = s1 = 0;
			for( j = 0; j < n; j++){
				if( i & (1 << j)){
					p = b(p , ar[j]);
					s1 += ar[j];
				}else{
					s = b(s , ar[j]);
				}
			}

			if( !b(p , s) ){
				max = MAX(max, MAX(s1 , sum - s1));
				//printf("%d %d\n",s1,sum - s1);
			}
		}
		if(max != -INF) printf("Case #%d: %d\n",ind,max);
		else printf("Case #%d: NO\n",ind);
	}
	return 0;
}
