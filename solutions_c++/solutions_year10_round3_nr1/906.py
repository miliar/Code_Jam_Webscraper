#include<iostream>


using namespace std;


int a[1000];
int b[1000];


int main(){

	int t;
	cin >> t;

	for(int i=0;i<t;++i){
		int n;
		cin >> n;

		int result = 0;

		for(int j=0;j<n;++j){
			cin >> a[j];
			cin >> b[j];
		}

		for(int j=0;j<n;++j){
			for(int k=j+1;k<n;++k){

				//(j,k) intersect or not?
				if(a[j] < a[k] && b[j] > b[k]) result++;
				else if(a[j] > a[k] && b[j] < b[k]) result++;
			}
		}
		cout << "Case #" << i+1 << ": " << result << endl;

	}

	return 0;
}
