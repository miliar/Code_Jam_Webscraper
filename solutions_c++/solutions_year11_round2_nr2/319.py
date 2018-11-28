#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int Test;
int n,d;
double now;
double t;
pair<int,int> a[300];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>Test;
	for (int test=0;test<Test;test++){
		cin>>n>>d;
		for (int i=0;i<n;i++)
			cin>>a[i].first>>a[i].second;
		sort(a,a+n);
		now=a[0].first;
		t=0;
		a[0].second--;
		for (int i=0;i<n;i++)
			for (int j=0;j<a[i].second;j++)
				if (a[i].first+t<now+d){
					double dt=((now+d)-(a[i].first+t))/2;
					now=now+d-dt;
					t+=dt;
				}else if (a[i].first-t>now+d)
					now=a[i].first-t;
				else
					now=now+d;
		printf("Case #%d: %.8f\n",test+1,t);
	}
	return 0;
}