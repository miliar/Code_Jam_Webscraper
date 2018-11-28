#include<numeric>
#include<vector>
#include<algorithm>
#include<cmath>
#include<iostream>
#define all(x) x.begin(),x.end()
using namespace std;
typedef long long ll;
ll data[50];

int main(){
	int runs;
	int cont= 1;
	cin >> runs;
	while(runs--){
		int N;
		bool rr = false;
		cin >> N;
		for(int i =0 ; i < N ; ++i){
			cin >> data[i];
			if(data[i] == 1) rr = true;
		}

		if (rr) {
			cout << "Case #" << cont++ << ": 0" <<endl;
			continue;
		}
		rr = false;
		ll dif;
		vector<ll> d ;
		d.clear();
		for(int i = 0 ; i < N ; i++)
			for(int j = 0 ; j < N ; j++){
				if(data[i] == data[j]) continue;
				dif = abs(data[j] - data[i]);
				d.push_back(dif);
			}
		ll T = d[0];		
		for(int i = 0 ; i< d.size() ; i++){
			T = __gcd(T,d[i]);
		}
		ll Y = ((data[0]/T)+1)*T - data[0];
		if (data[0]%T == 0) Y = 0;
		cout << "Case #"<<cont++<<": "<<Y << endl;		
	}
	return 0;
}