#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	int N,n,s,p,t,count;
	cin>>N;
	for (int i=1;i<=N;i++){
		count=0;
		cout<<"Case #"<<i<<": ";
		cin>>n>>s>>p;
		for (int j=0;j<n;j++){
			cin>>t;
			if (t>(p-1)*3) {count++;continue;}
			if (t>(p-1)*3-2 && s>0 && p>1){count++;s--;continue;}
		}
		cout<<count<<endl;
	}
	return 0;
}
