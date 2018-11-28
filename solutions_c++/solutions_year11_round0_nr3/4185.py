#include<iostream>
using namespace std;
const int INF = 1000000000;
int main(){
	int task, i, min, sum, n, now, Xor;
	freopen("C-large (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>task;
	for(int repeat = 1; repeat <= task; ++repeat){
		cin>>n;
		Xor = 0;
		sum = 0;
		min = INF;
		for(i = 0; i < n; i++){
			cin >> now;
			Xor = Xor ^ now;
			sum = sum + now;
			if(now < min)
				min = now;
		}
		if(Xor != 0){
			cout<<"Case #"<<repeat<<": NO"<<endl;
		}else{
			cout<<"Case #"<<repeat<<": "<<sum - min<<endl;
		}
	}
}
