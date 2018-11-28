#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

int a[2000],b[2000];

bool minCmp(int a,int b)
{
	return a < b;
}
bool maxCmp(int a,int b)
{
	return a > b;
}

char str[100];
int val[100];
int op[100];

int len;

__int64 coun;

__int64 ten[20];

bool Valid(__int64 n)
{
	if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0)
		return true;
	return false;
}

void dfs(int depth) {

	if (depth == len - 1) {
		int i;

	/*	for (i = 0; i < len - 1; i ++) {
			printf("%d ",op[i]);
		}
		printf("\n");*/

		__int64 las[100];
		int top = 0;

		__int64 tv = val[len-1];
		int base = 1;

		for (i = len - 2; i >= 0; i --) {

			if (op[i] == -1) {
				las[top ++] = -tv;
				tv = val[i];
				base = 1;
			} else if (op[i] == 1) {
				las[top ++] = tv;
				tv = val[i];
				base = 1;
			} else {
				tv += val[i] * ten[base];
				base ++;
			}
		}

		las[top ++] = tv;

		__int64 ans = 0;

		for (i = 0; i < top; i ++) {
		//	printf("%d ",las[i]);
			ans += las[i];
		}
		

	//	printf("\n");



		/*

		__int64 tv = val[0];
		int base = 1;
		__int64 ans = 0;

		int i;
		


		for (i = len - 2; i >= 0; i --) {
			if (op[i] == 1) {
				ans += tv;
				tv = val[i];
				base = 1;
			} else if (op[i] == -1) {
				ans -= tv;
				tv = val[i];
				base = 1;
			} else if (op[i] == 0) {
				tv = tv + val[i] * ten[base];
			}
		}*/
		if (Valid(ans)) {
			coun ++;
		}
		return ;
	}
	int i;
	for (i = -1; i < 2; i ++) {
		op[depth] = i;
		dfs(depth + 1);
	}
}


int main()
{
	int C;
	int i;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	ten[0] = 1;

	for (i = 1; i <= 14; i ++) {
		ten[i] = ten[i-1]*10;
	}
	while (scanf("%d",&C) != EOF) {
		for (int p = 1; p <= C; p ++) {

			scanf("%s",str);

			len = strlen(str);

			for (i = 0; i < len; i ++) {
				val[i] = str[i] - '0';
			}

			coun = 0;
			dfs(0);


			printf("Case #%d: %I64d\n",p,coun);


		}
	}

	return 0;
}

