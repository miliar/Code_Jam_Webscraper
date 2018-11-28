#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<set>


using namespace std;

#define ps system("PAUSE")
//#define N 1001
typedef long long int  longlong;

int a[1001],b[1001];

int main() { 
	int t,n,ic;
	freopen("C:/TestData/A-large.in","r",stdin);freopen("C:/TestData/A.out","w",stdout);
	scanf("%d",&t);

	for(int ti=1;ti<=t;ti++) {
		scanf("%d",&n);
		ic = 0;
		for(int i=0;i<n;i++) {
			scanf("%d%d",&a[i],&b[i]);
			for(int j=0;j<i;j++) {
				if( (a[j] - a[i]) * (b[j]-b[i]) < 0 ) 
					ic++;
			}
		}
		printf("Case #%d: %ld\n",ti,ic);
	}
	return 0;	
}