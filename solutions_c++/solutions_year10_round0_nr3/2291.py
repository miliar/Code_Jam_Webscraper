#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define f0(i,n) for(i=0;i<n;i++)
#define f1(i,n) for(i=1;i<=n;i++)



int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	long N, i,j,r,k,n;
	long a[100000] ;
	cin >> N;
	f1(i,N) {
	    cin>>r>>k>>n;
	    f1(j,n) cin>>a[j];
	    long start=0,SUM=0,jj=1,sum,x;
	    j=1;
	    a[0]=a[n];
	    while(j<=r){
	        sum=0;x=jj;
	        while(sum<=k){
	            sum=sum+a[jj];
	            ++jj;
	            if (sum>k) {sum=sum-a[jj-1]; --jj; break;}
	            if(jj>n)
                    jj=1;

                if (jj==x) break;
                }
	        SUM+=sum;
	        if (jj==0) jj=1;
	        ++j;
        }
		printf("Case #%d: %d\n", i,SUM);
	}

	return 0;
}
