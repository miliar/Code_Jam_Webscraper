#include <string.h>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <bitset>
#include <cstring>
#include <queue>
#include <cmath>
#include <map>
#include <iterator>
#define EPS 1e-9
#pragma comment(linker, "/STACK:512000000")

using namespace std;



struct my{
	int b,e;
	double w;
};

bool cmp(my a, my b){
	return a.w<b.w;
}

void solve(){
	my a[10013];
	double s,r,t;
	int n,x;
	cin>>x>>s>>r>>t>>n;
	for (int i=0;i<n;i++){
		cin>>a[i].b>>a[i].e>>a[i].w;
	}
	int m=n;
	int last=0;
	for (int i=0;i<n;i++){
		if (a[i].b!=last){
			a[m].b=last;
			a[m].e=a[i].b;
			a[m].w=0;
			m++;
		}
		last=a[i].e;
	}
	if (x!=last){
		a[m].b=last;
		a[m].e=x;
		a[m].w=0;
		m++;
	}
	n=m;
	sort(a,a+n,cmp);
	double time=0.0;
	double ans=0;
	for (int i=0;i<n;i++){
		if (t>(a[i].e-a[i].b)/(a[i].w+r)){
			t-=(a[i].e-a[i].b)/(a[i].w+r);
			ans+=(a[i].e-a[i].b)/(a[i].w+r);
		}			
		else{
			if (t>0){
				ans+=t+(a[i].e-a[i].b-t*(r+a[i].w))/(s+a[i].w);
				t=-1;
			}
			else{
				ans+=(a[i].e-a[i].b)/(s+a[i].w);
			}
		}
		last=a[i].e;
	}
	cout.setf(ios::fixed);cout.precision(8);
	cout<<ans;
	cout<<endl;
	return;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for (int z=1;z<=t;z++){
		cout<<"Case #"<<z<<": ";
		solve();
	}
	return 0;
	//cout.setf(ios::fixed);cout.precision(20);
}

/*#include <string.h>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <bitset>
#include <cstring>
#include <queue>
#include <cmath>
#include <map>
#include <iterator>
#define EPS 1e-9
#pragma comment(linker, "/STACK:512000000")

using namespace std;



int b[1013],e[1013];
double w[1013];

void solve(){
	double s,r,t;
	int n,x;
	cin>>x>>s>>r>>t>>n;
	double time=0.0;
	int last=0;
	double ans=0;
	for (int i=0;i<n;i++){
		cin>>b[i]>>e[i]>>w[i];
	}
	b[n]=e[n-1];
	e[n]=x;
	w[n]=0;
	n++;
	for (int i=0;i<n;i++){
		if (t>(b[i]-last)/(r)){
			t-=(b[i]-last)/(r);
			ans+=(b[i]-last)/(r);
		}
		else{
			if (t>0){
				ans+=t+(b[i]-last-t*r)/(s);
				t=-1;
			}
			else{
				ans+=(b[i]-last)/(s);
			}
		}
		if (t>(e[i]-b[i])/(w[i]+r)){
			t-=(e[i]-b[i])/(w[i]+r);
			ans+=(e[i]-b[i])/(w[i]+r);
		}			
		else{
			if (t>0){
				ans+=t+(e[i]-b[i]-t*(r+w[i]))/(s+w[i]);
				t=-1;
			}
			else{
				ans+=(e[i]-b[i])/(s+w[i]);
			}
		}
		last=e[i];
	}
	cout.setf(ios::fixed);cout.precision(8);
	cout<<ans;
	cout<<endl;
	return;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for (int z=1;z<=t;z++){
		cout<<"Case #"<<z<<": ";
		solve();
	}
	return 0;
	//cout.setf(ios::fixed);cout.precision(20);
}*/