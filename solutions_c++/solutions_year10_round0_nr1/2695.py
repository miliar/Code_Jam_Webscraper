#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
int main(){
	int kases,N,K; cin>>kases;
	for (int kas=1; kas<=kases; kas++) {
		cin>>N>>K;
		int posi = (1<<N);
		bool on=((K+1)%posi) == 0;		
		cout<<"Case #"<<kas<<": "<<(on?"ON":"OFF") <<endl;
	}
}