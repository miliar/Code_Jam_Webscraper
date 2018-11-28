#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <hash_map>

using namespace std;
const long long MNAX=1000;

void exchange(long long& x, long long& y){
	long long k=x;x=y;y=k;
}
void Qsort(long long* a, long long first, long long last){
	long long v, left=first, right=last;
	v=a[(left+right)/2];
	while (left<=right){
		while (a[left]<v) ++left;
		while (a[right]>v) --right;
		if (left<=right){
			exchange(a[left],a[right]);
			++left; --right;
		}
	}
	if (first<right) Qsort(a,first,right);
	if (left<last) Qsort(a,left,last);
}

long long a[MNAX+2];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	long long test;
	cin>>test;
	for (long long t=1;t<=test;++t){
		long long ans = 0;
		long long n;
		cin>>n;
		for (long long i=1;i<=n;++i) cin>>a[i];
		Qsort(a,1,n);
		long long sum = a[2];
		ans = a[2];
		for (long long i=3;i<=n;++i){
			ans ^= a[i];
			sum += a[i];
		}
		if (ans == a[1]) cout<<"Case #"<<t<<": "<<sum<<endl;
		else cout<<"Case #"<<t<<": "<<"NO"<<endl;
	}
	return 0;
}
