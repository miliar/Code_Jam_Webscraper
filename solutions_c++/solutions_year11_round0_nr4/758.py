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
bool used[MNAX+2];
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	long long test;
	cin>>test;
	for (long long t=1;t<=test;++t){
		long long ans = 0;
		long long n,i;
		cin>>n;
		for (i=1;i<=n;++i){
			cin>>a[i];
			used[i] = false;
		}

		for (i=1;i<=n;++i){
			if (a[i]!=i && !used[i]){
				int cur = i, kol = 0;
				while (!used[cur]){
					used[cur]=true;
					cur = a[cur];
					++kol;
				}
				ans +=kol;
			}
		}

		cout<<"Case #"<<t<<": "<<ans<<".000000"<<endl;
	}
	return 0;
}
