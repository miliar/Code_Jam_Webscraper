#include<algorithm>
#include<bitset>
#include<cassert>
#include<cmath>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<fstream>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>
#include<climits>
#define LL long long
using namespace std;


int main (){
	int testCase; scanf("%d",&testCase); int idd=1;
	while( testCase-- ){
		int n;scanf("%d",&n);
		int a[n],xr=0,sum=0;
		for(int i=0;i<n;i++){  scanf("%d",&a[i]); xr=xr xor a[i]; sum+=a[i];}
		sort(a,a+n);
		if( xr==0 ) printf("Case #%d: %d\n",idd++,sum-a[0]);
		else printf("Case #%d: NO\n",idd++);
	}
	return 0;
}
//~vish ( vikas.cse.nitt@gmail.com )
