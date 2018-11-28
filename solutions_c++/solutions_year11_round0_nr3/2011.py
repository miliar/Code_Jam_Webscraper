#include<iostream>
#include<complex>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<memory.h>
using namespace std;
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for (int k=0; k<t; k++){
		int n,a=0,sum=0,MIN=9999999;
		cin>>n;
		for (int i=0; i<n; i++){
			int x;
			cin>>x;
			MIN=min(MIN,x);
			sum+=x;
			a=a^x;
		}
		cout<<"Case #"<<k+1<<": ";
		if (a==0)
			cout<<sum-MIN<<endl;
		else
			cout<<"NO"<<endl;
	}
	
    return 0;
}

