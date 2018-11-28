#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("B-small-attempt2.in");
	ofstream outf("B-small-attempt2.out");
#define cin inf
#define cout outf
#endif
template<class T> T gcd(T a,T b){ if(a<0) return gcd(-a,b);if(b<0) return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

int main(){
	int t;
	cin>>t;
	for(int i = 0;i < t;i++){
		int n,c = 0;
		cin>>n;
		//vector<string> v(n);
		vector<int> v(n);
		for(int j = 0;j < n;j++){
			cin>>v[j];
		}
		if(n == 2){
			int m = abs(v[0]-v[1]);
			c = v[0]%m;
			if(c!=0) c = m-v[0]%m;
		}
		else if(n == 3){
			sort(v.rbegin(),v.rend());
			int m1 = abs(v[0]-v[1]);
			int m2 = abs(v[1]-v[2]);
			int m = gcd<int>(m1,m2);
			c = v[0]%m;
			if(c!=0) c = m-v[0]%m;
		}
		cout<<"Case #"<<i+1<<": "<<c<<endl;	
	}
	return 0;
}