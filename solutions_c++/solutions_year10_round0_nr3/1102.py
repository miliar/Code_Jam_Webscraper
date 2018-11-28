#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;

#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("C-small-attempt0.in");
	ofstream outf("C-small-attempt0.out");
#define cin inf
#define cout outf
#endif


int main(){
	int t;
	cin>>t;
	for(int i = 0;i < t;i++){
		int r,k,n;
		cin>>r>>k>>n;
		vector<int> q(n,0);
		vector<int> qr(n,0);
		vector<int> qn(n,0);
		int sum = 0;
		for(int j = 0;j < n;j++){
			cin>>q[j];
			sum+=q[j];
		}
		if(sum <= k){
			cout<<"Case #"<<i+1<<": "<<sum*r<<endl;
		}
		else{
		for(int j = 0;j < n;j++){
			int tmp = 0;
			for(int j1 = j;;j1 = (++j1)%n){
				tmp+=q[j1];
				if(tmp > k){
					qn[j] = j1%n;
					qr[j] = tmp-=q[j1];
					//cout<<j<<":"<<qn[j]<<endl;
					break;
				}
			}
		}
		int c = 0,next = 0;
		for(int j = 0;j < r;j++){
			c+=qr[next];
			next = qn[next];
		}
		cout<<"Case #"<<i+1<<": "<<c<<endl;
		}
	}
	return 0;
}