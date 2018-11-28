#include <iostream>
using namespace std;

int main(){
	int t, n, s, p, b;
	cin >> t;
	for(int i =1; i<=t; i++){
		b=0;
		cin >> n >> s >> p;
		for(int j= 0; j<n; j++){
			int sum, best;
			cin >> sum;
			if(sum == 0) best = 0;
			else if(sum%3 == 0){
				best = sum/3;
				if(s > 0 && (sum/3 + 1 == p)) {
					best++;
					s--;
				} 
			}
			else if(sum%3 == 1){
				best = sum/3 + 1;
			}
			else if(sum%3 == 2){
				best = sum/3 + 1;
				if(s > 0 && (sum/3 + 2 == p)){ 
					best++;
					s--;
				}
			}
			if(best >= p) b++;
		}
		cout<<"Case #"<<i<<": "<<b<<"\n";
	}
	return 0;
}

