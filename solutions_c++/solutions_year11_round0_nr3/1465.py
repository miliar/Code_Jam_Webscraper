/*
*  Javier Segovia
*  0.016
*/
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
#define MIN(a,b) ((a)<(b)?(a):(b))
int main(){
	int kases; cin>>kases;
	for (int k=1; k<=kases; k++) {
		int N; cin>>N;
		int total=0,ac;
		int sum=0,mini=2000000000;
		while (N--) {
			cin>>ac;
			total = total^ac;
			sum+=ac;
			mini = MIN(mini,ac);
		}
		if(total != 0) cout<<"Case #"<<k<<": NO"<<endl;
		else{
			cout<<"Case #"<<k<<": "<<sum - mini<<endl;
		}
	}
}