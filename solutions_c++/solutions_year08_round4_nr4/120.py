#include<iostream>
#include<vector>
using namespace std;

int K;
string str;

int main(){

	//freopen("1.in", "rt", stdin);

	freopen("D-small.in", "rt", stdin);
	freopen("D-small.out", "wt", stdout);
	//freopen("D-large.in", "rt", stdin);
	//freopen("D-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		
		cin >> K >> str;
		vector<int> v;
		int i;
		for(i = 0 ; i < K ; i++)v.push_back(i);
		
		int best = 1e9;
		do{
			string s = "";
			for(int i = 0 ; i < str.size() ; i+=K){
				for(int j = i ; j < i+K ; j++){
					int index = v[j-i]+i;
					s += str[index];
				}
			}
		
			int current = 0;
			for(int m = 0 ; m < s.size() ; m++){
				current++;
				int n = m;
				while(n < s.size() && s[n] == s[m])n++;
				m = n-1;
			}
			best = min(best, current);
					
		}while(next_permutation(v.begin(), v.end()));
		
		cout << "Case #" << t+1 << ": " << best << endl;
	}

	return 0;	
}
