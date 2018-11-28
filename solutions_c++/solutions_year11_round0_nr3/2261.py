#include<iostream>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		int N;
		cout << "Case #" << t << ": ";
		cin >> N;
		int allxor=0;
		int sum=0;
		int min = 1000000;
		for(int i=0;i<N;i++){
			int x;
			cin >> x;
			allxor = allxor^x;
			sum+=x;
			min = min>x?x:min;
		}
		if(allxor==0)
			cout << sum-min << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
