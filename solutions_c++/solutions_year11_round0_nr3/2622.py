#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)

int n , data[1000];
int main(){
	int N;
	cin >> N;
	
	rep(NN,N){
		cin >> n;
		rep(i,n) cin >> data[i];
		sort(data,data+n,greater<int>());
		int check = 0 , sum = 0;
		rep(i,n-1)sum += data[i];
		rep(i,n) check ^= data[i];
		
		cout << "Case #"<< NN+1 << ": ";
		if(check == 0)cout << sum << endl; 
		else cout << "NO" << endl;
	}
}