#include<iostream>
#include<map>
#include<vector>
#include<sstream>

using namespace std;

bool state[30];
int power_place;

void toggle(int n){
	for(int i=0;i<=power_place;++i){
		state[i] = !state[i];
	}
	for(int i=0;i<n;++i){
		if(!state[i]){
			power_place=i;
			break;
		}
		if(i==n-1) power_place = n;
	}
}


int main(){

	int t;
	cin >> t;

	for(int i=0;i<t;++i){
		int n,k;
		cin >> n >> k;
		if(k==0){
			cout << "Case #" << i+1 << ": " << "OFF" << endl;
			continue;
		}

		for(int j=0;j<n;++j) state[j] = false;
		power_place=0;
		for(int j=0;j<k;++j){
			toggle(n);
		}
		if(power_place==n) cout << "Case #" << i+1 << ": " << "ON" << endl;
		else cout << "Case #" << i+1 << ": " << "OFF" << endl;
	}

	return 0;
}
