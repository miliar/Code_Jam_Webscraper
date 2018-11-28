#include<iostream>
#include<algorithm>
#include<numeric>
#include<stdlib.h>
#include<stdio.h>
#include<queue>
#include<list>
#include<stack>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<math.h>
#include<limits>
#include<cmath>
#include<string>
#include<fstream>
#include<sstream>
#include<stdio.h>
#include<time.h>
#include<string.h>
#include<complex>
#include<iterator>
using namespace std;

int main(){
	freopen("C:\\Documents and Settings\\zgmcn\\×ÀÃæ\\in.txt","r",stdin);
	freopen("C:\\Documents and Settings\\zgmcn\\×ÀÃæ\\out.txt","w",stdout);
	int t, n, a[41];
	scanf("%d",&t);
	char s[41];
	for(int r=1; r<=t; r++){
		scanf("%d",&n);
		for(int i=0,j; i<n; i++){
			scanf("%s",s);
			for(j=n-1; j>=0; j--) if( s[j]=='1') break;
			a[i] = j;
		}
		int num = 0;
		for(int i=0,j; i<n; i++){
			for(j=i; j<n; j++) if( a[j]<=i ) break;
			for(int k=j-1; k>=i; k--){ swap( a[k], a[k+1] ); num++; }
		}
		printf("Case #%d: %d\n",r,num);
	}
	return 0;
}