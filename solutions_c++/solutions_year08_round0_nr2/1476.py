#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

void readt(int c,vector<int>&a,vector<int>&b){
	for(int i=0;i<c;i++){
		char x1,x2,w,x3,x4;
		cin>>x1>>x2>>w>>x3>>x4;
		a.push_back(x1*600+x2*60+x3*10+x4);
		cin>>x1>>x2>>w>>x3>>x4;
		b.push_back(x1*600+x2*60+x3*10+x4);
	}
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());
}

int ans(int t,vector<int>&a,vector<int>&b){
	int r=0;
	for(vector<int>::iterator i=a.begin(),j=b.begin();i!=a.end();i++)
		if(j==b.end()||*i<*j+t)
			r++;
		else
			j++;
	return r;
}

int main(){
	int n;
	cin>>n;
	for(int c=1;c<=n;c++){
		int t,na,nb;
		cin>>t>>na>>nb;
		vector<int> aa,ab,ba,bb;
		readt(na,aa,ab);
		readt(nb,bb,ba);
		cout<<"Case #"<<c<<": "<<ans(t,aa,ba)<<" "<<ans(t,bb,ab)<<endl;
	}
}