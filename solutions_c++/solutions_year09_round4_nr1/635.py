#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>

#define ll long long


using namespace std;

string a[100];
int n;
int sum;

bool check(string s, int k){
	for (int i = k+1; i < s.size(); i++)
		if (s[i] == '1'){
			return false;
		}
	return true;

}

int find_(int k){
	for (int i = k+1; i < n; i++){
		if (check(a[i], k))
			return i;
	}
	return 0;
}

void solve(int n){
	for (int i = 0; i < n; i++){
		if (!check(a[i], i)){
			int p = find_(i);
			sum += (p - i);
			for (int j = p-1; j >= i; j--)
				swap(a[j], a[j+1]);
		}
	}

}

int main(){
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		cin >> n;
		for (int i = 0; i < n; i++){
			cin >> a[i];
		}
		sum = 0;
	        solve(n);
		cout << "Case #" << t+1 << ": " << sum << endl;
	}
	return 0;
}