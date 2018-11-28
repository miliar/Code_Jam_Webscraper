#include <iostream>

using namespace std;

long long add(long long a, long long b)
{
	int k, i, s, aa, bb;
	k=1;
	s=0;
	for (i=0; i<20; i++) {
		aa=a%2;
		bb=b%2;
		s+=((aa+bb)%2)*k;
		a/=2;
		b/=2;
		k*=2;
	}
	return s;
}

int main()
{
	long long i, j, k, n, t, c, min, sum, sm;
	
	cin >> t;
	for (k=0; k<t; k++) {
		cin >> n;
		cin >> c;
		min=c;
		sum=c;
		sm=c;
		for (i=1; i<n; i++) {
			cin >> c;
			if (c < min) min=c;
			sum+=c;
			sm=add(sm,c);
		}
		if (sm>0) cout << "Case #" << k+1 << ": NO" << endl;
		if (sm==0) cout << "Case #" << k+1 << ": " << sum-min << endl;
	}
}
