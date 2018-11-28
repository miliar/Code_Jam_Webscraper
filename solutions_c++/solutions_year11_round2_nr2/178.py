#include<stdio.h>
#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
#include<memory.h>
#include<map>
#include<queue>

using namespace std;

int n,k,d,a[1111111],x,y;
long double l,r,c;

bool cc(long double w){
	long double pr=-1e15;
	for (int i=0;i<n;i++)if (pr+d>a[i]+w)return 0;else {
		pr=max(pr+d,a[i]-w);
	}
	return 1;
}


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int t=0;
	cin >> t;
	cout.precision(6);
	for (int e=1;e<=t;e++){
		cin >> k >> d;
		n=0;
		for (int i=0;i<k;i++){
			cin >> x >> y;
			for (int j=0;j<y;j++)a[n++]=x;
		}
		sort(a,a+n);
		l=0;
		r=1e15;
		while (r-l>1e-7){
			c=(l+r)/2;
			if (cc(c))r=c;else l=c;
		}
		cout << "Case #" << e << ": " << fixed << l << endl;
	}
	return 0;
}


