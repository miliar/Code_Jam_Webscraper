#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX_N = 1000;

int caseNum, dataNum, caseno;
vector<int> v;

int num2power[21];

void bitCount(int n){
	int a=1;

	for(int a=0 ; a<21 ; a++){
		if( (n & 1<<a) == 1<<a) num2power[a]++;
	}
}



void solve(){
	cout << "Case #" << caseno << ": ";

	for(int i=0 ; i<21 ; i++) num2power[i] = 0;
	

	
	for(int i=0 ; i<v.size() ; i++){
		bitCount(v[i]);
	}

	
	for(int i=0 ; i<21 ; i++){
		if(num2power[i]%2==1){
			cout << "NO" << endl;
			return;
		}
	}

	sort(v.begin(), v.end());

	int k=0;
	for(int i=1 ; i<v.size() ; i++){
		k += v[i];
	}

	cout << k << endl;
	return;

}

int main(){

	cin >> caseNum;
	int k;

	for(caseno=1 ; caseno<=caseNum ; caseno++){
		cin >> dataNum;
		v.clear();

		for(int i=0 ; i<dataNum ; i++){
			cin >> k;
			v.push_back(k);
		}

		solve();
	}
}