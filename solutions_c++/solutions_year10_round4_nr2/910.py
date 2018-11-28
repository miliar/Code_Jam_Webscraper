#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef unsigned long long ULL;
bool isEmp(int* a, int p, int n){
	for (int i = p; i < n; i++){
		if (a[i] > 0)
			return true;
	}
	return false;
}
int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int test = 1; test <= tests; test++){
		int p = 0;
		scanf("%d",&p);
		int prior[1024] = {0};
		int l = pow(2.,p);
		for (int i = 0; i < l; i++){
			scanf("%d",&prior[i]);
		}
		int temp;
		for (int i = l/2; i > 0; i/= 2){
			for (int j = 0; j < i; j++){
				scanf("%d",&temp);
			}
		}
		int count = 0;
		int tt = l/2;
		for (int dep = 1; dep <= p; dep++){
			for (int i = 0; i < l; i+= pow(2.,dep)){
				bool fl = true;
				for (int j = i; j < i+pow(2.,dep);j++){
					if (prior[j] < dep)
						fl = false;
				}
				if (!fl){
					count++;
				}
			}
		}
		printf("Case #%d: %d\n",test,count);
	}
	return 0;
}