#include<iostream>
#include<vector>
#include<map>
#include<fstream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<set>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int a[2222] , x[2222];
bool b[2222];

int abs(int p , int q) {
	if (p>q) return p-q;
	return q-p;
}

int main() {
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int i , j , k , tt , p1 , p2 , ans , n , add;
	char ch;
	cin >> tt;
	for (k=1; k<=tt; k++) {
		cin >> n;
		p1=p2=0;
		a[0]=0;
		ans=0;
		x[0]=1;
		add=0;
		for (i=1; i<=n; i++) {
			cin >> ch >> x[i];
			if (ch=='B') {
				a[i]=a[p1]+abs(x[i],x[p1])+1;
				b[i]=true;
				p1=i;
			}
			else {
				a[i]=a[p2]+abs(x[i],x[p2])+1;
				b[i]=false;
				p2=i;
			}
		}
		for (i=1; i<=n; i++) if (a[i]<=a[i-1]) {
			add=a[i-1]-a[i]+1;
			for (j=i; j<=n; j++) if (b[i]==b[j]) a[j]+=add;
		}
		printf("Case #%d: %d\n" , k , a[n]);
	}
	return 0;
}