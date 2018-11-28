#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <map>

using namespace std;

int main(){

	int T;
	cin >> T;
	
	for (int i = 1 ; i <=T ; i++){
		int n, s, p;
		cin >> n >> s >> p;
		vector <int> scores;
		for (int j = 0 ; j < n; j++){
			int x;
			cin >> x;
			scores.push_back(x);
		}
		sort(scores.rbegin(), scores.rend());
		int ans = 0;
		int sCount = s;
		for (int j = 0 ; j < n; j++){
			//cout << "score: " << scores[j] << endl;
			if ((scores[j]/3) >= p){
				ans++;
			} else if (scores[j]%3 == 2){	
				if ((scores[j]/3)+1 >= p){
					ans++;						
				} else if ((scores[j]/3)+2 >= p && sCount){
					ans++;
					sCount--;
				}
			} else if (scores[j]%3 == 1){
				if ((scores[j]/3)+1 >= p){
					ans++;
				} else if ((scores[j]/3)+2 >= p && sCount){
					ans++;
					sCount--;
				}
			} else if (scores[j]%3 == 0 && scores[j]){
				if ((scores[j]/3)+1 >= p && sCount){
					ans++;
					sCount--;
				}
			}
		}
			 
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
	
}
