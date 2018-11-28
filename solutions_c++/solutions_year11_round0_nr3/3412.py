#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cmath>


using namespace std;


int main() {
	freopen("C:/TestData/C-large.in","r",stdin);
	freopen("C:/TestData/A.out","w",stdout);
	int t,n,temp,xor =11 ;
	unsigned long long int sum=0,small = 9999999;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++) { 
		scanf("%d",&n);
		sum = 0 ; small = 9999999;xor = 11;
		for(int i=0;i<n;i++) {
			scanf("%d",&temp);
			if ( temp < small ) small = temp; 
			xor = xor ^ temp ;
			sum += (unsigned long long int )temp; 
		}
		xor = xor ^ 11;
		if ( xor == 0 ) cout<<"Case #"<<ti<<": "<<(sum-small)<<endl;
		else printf("Case #%d: NO\n",ti);
	}

}

