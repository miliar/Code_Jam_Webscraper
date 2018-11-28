#include <iostream>
#include <vector>
using namespace std;

int calculate_to_power(vector<bool> &snlist){
	int to_power = 0;

	for(int i = 0; i < snlist.size(); i++){
		if(snlist[i]){
			to_power++;
		}
		else{
			break;
		}
	}

	if(to_power >= snlist.size()){
		to_power = snlist.size() - 1;
	}

	return to_power;
}

void snap_event(vector<bool> &snlist){
	int to_power = calculate_to_power(snlist);

	for(int i = 0; i <= to_power; i++){
		snlist[i] = !snlist[i];
	}
}

void initialize(vector<bool> &snlist, int n){
	for(int i = 0; i < n; i++){
		snlist.push_back(false);
	}
}

int main(){
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);

	int tcase;

	cin >> tcase;
	for(int i = 0; i < tcase; i++){
		int n;
		long long k;
		cin >> n >> k;
		
		vector<bool> snlist;
		initialize(snlist, n);
		for(long long j = 0; j < k; j++){
			snap_event(snlist);
		}

		bool flag = true;
		for(int j = 0; j < snlist.size(); j++){
			if(!snlist[j]){
				flag = false;
				break;
			}
		}

		cout << "Case #" << i + 1 <<": ";
		if(flag){
			cout << "ON";
		}
		else{
			cout << "OFF";
		}

		cout << endl;
	}

	return 0;
}