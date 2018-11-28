#include<iostream>
#include<gmpxx.h>
#include<string>
#include<vector>

using namespace std;

int main(int argc, char* argv[])
{

	int t,n;
	int x,y;
	int out=0;
	vector<int> a;
	vector<int> b;

	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		for(int j=0;j<n;j++){
			cin>>x>>y;
			a.push_back(x);
			b.push_back(y);
		}
		if(n==1) cout<<"Case #"<<i<<": 0"<<endl;
		else{
				//if(a[0]<a[1] && b[0]<b[1]) out=0;
				//if(a[0]>a[1] && b[0]>b[1]) out=0;
				if(a[0]<a[1] && b[0]>b[1]) out++;
				if(a[0]>a[1] && b[0]<b[1]) out++;
				//if(a[0]<a[1] && b[0]<b[1]) out=0;
				//if(a[0]>a[1] && b[0]>b[1]) out=0;
				//if(a[k]<a[k+1] && b[k]b[k+1]) out++;
			
		cout<<"Case #"<<i<<": "<<out<<endl;
		//a.clear();
		//b.clear();
		//out=0;
	}
		a.clear();
		b.clear();
		out=0;
		
	}
	return 0;
}
