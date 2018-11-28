#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;


long long gcd(long long a, long long b) {
	if (!b) return a;
	else return gcd(b, a % b);
}

long long lcm(long long *a, long long left, long long right) {
	if (left == right) return a[left];
	else {
		long long mid = (left + right)/2;
		long long lVal = lcm (a, left, mid);
		long long rVal = lcm (a, mid + 1, right);
		return (lVal*rVal)/gcd(lVal, rVal);
	}
}

long long gcdArray(long long *a, long long left, long long right) {
	if (left == right) return a[left];
	else {
		long long mid = (left + right)/2;
		long long lVal = gcdArray (a, left, mid);
		long long rVal = gcdArray (a, mid + 1, right);
		return gcd(lVal, rVal);
	}
	
}
/* qsort int comparison function */ 
int int_cmp(const void *a, const void *b) 
{ 
    const long long *ia = (const long long *)a; // casting pointer types 
    const long long *ib = (const long long *)b;
    return *ia  - *ib; 
	/* integer comparison: returns negative if b > a 
	and positive if a > b */ 
} 


int main() {
	freopen("inp.txt","r", stdin);
	freopen("out.txt","w", stdout);

	long long T, N, L, H, i, j;
	long long *a;
	cin>>T;
	for (i = 0; i < T; i++) {
		cin>>N>>L>>H;
		a = new long long[N];
		for (j = 0; j < N; j++) {
			cin>>a[j];
		}
		
		long long sol = -1;
		int ok = 0;
		for (j = L; (j <= H)&&(!ok); j++) {
			int sol = 0;
			for (int k = 0; (k < N)&&(!sol); k++) {
				if ((j % a[k]!=0) && (a[k] % j!= 0)) sol = 1;
			}
			if (!sol) ok = j;
		}
		cout<<"Case #"<<(i + 1)<<": ";
		if (!ok) cout<<"NO\n";
			else cout<<ok<<"\n";
/*
		if (L == 1) cout<<"1\n";
		else {
			qsort(a, N, sizeof(long long), int_cmp);
			long long cmmmc;
		
			int ok = 0;
			for (j = N - 1; (j >= 0)&&(!ok); j--) {		
				cmmmc = lcm(a, 0, j);
				if ((L <= cmmmc) && (cmmmc <= H)){
					long long cmmdc;
					if (j + 1 <= N - 1) {
						cmmdc = gcdArray(a, j+1, N - 1);
					}
					else cmmdc = cmmmc;
					
					if (cmmdc % cmmmc == 0) ok = 2;
				}
			}
			if (ok == 2) cout <<cmmmc<<"\n";
			else cout<<"NO\n";
		}
*/		
	}

	return 0;
}
