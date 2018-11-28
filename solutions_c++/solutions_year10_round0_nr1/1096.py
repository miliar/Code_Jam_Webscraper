#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;

#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("A-large.in");
	ofstream outf("A-large.out");
#define cin inf
#define cout outf
#endif


int main(){
	int t;
	cin>>t;
	for(int i = 0;i < t;i++){
		int n,k;
		cin>>n>>k;
		//int c1 = pow(2.0,(double)(n-1));
		int c2 = pow(2.0,(double)(n));
		int l = k%c2;
		string s = "OFF";
		if(l == c2-1){
			s = "ON";
		}
		cout<<"Case #"<<i+1<<": "<<s<<endl;
	}
	return 0;
}