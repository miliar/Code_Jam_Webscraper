#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-10)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

int main(void){
	int T;
	scanf("%d",&T);
	for(int casenum=1;casenum<=T;casenum++){
		int i;
		int n;
		scanf("%d",&n);
		int ans=n;
		for(i=1;i<=n;i++){
			int a;
			scanf("%d",&a);
			if(i==a)ans--;
		}
		printf("Case #%d: %.10lf\n",casenum,(double)ans);
	}
	return 0;
}
