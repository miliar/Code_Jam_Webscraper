#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const long long MNAX=100;

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

long long gcd(long long a, long long b)
{
	if (b==0) return a;
	else return gcd(b,a%b);
}


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long long test;
	cin>>test;
	for (long long t=1;t<=test;++t){
		bool ans = false;
		long long n,pd,pg;
		cin>>n>>pd>>pg;
		if (pd==0 && pg==0){
			ans = true;
		}
		else if (pd*pg==0){
			ans = false;
		}
		else if (pg==100 && pd!=100){
			ans = false;
		}
		else{
			long long p100 = 100;
			long long nd = gcd(pd,p100);
			pd/= nd;
			p100/= nd;

			if (n>=p100){
				ans = true;
			}
/*			for (long long i=1;i<=n;++i){
				if ((i*pd/100)==(double(i*pd)/100)){
					ans = true;
					break;
				}
			}
*/		}
		if ( ans ) cout<<"Case #"<<t<<": "<<"Possible"<<endl;
		else cout<<"Case #"<<t<<": "<<"Broken"<<endl;
	}
	return 0;
}
