#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
using namespace std;

//code of suren

int main(){
	int T ; cin >> T;
	for (int testCase = 1; testCase <= T; ++testCase) {
		int R, K , n ;
		cin >> R >> K >> n ;
		vector<int> groups(n) ;

		for (int i = 0; i < n; ++i) {
			cin >> groups[i] ;
		}
		int max_possible = accumulate(groups.begin(), groups.end(), 0);

		int pos = 0, total = 0; int ans=0;
		while(R--){
			while(total <= K){
				if(total + groups[pos % n] > K || total+groups[pos%n] > max_possible) {
					ans += total; total = 0; break;
					cout << ans << " ";
				}
				else {
					total += groups[pos % n];
					pos++;
				}
			}
		}
		cout << "Case #" << testCase << ": " << ans << endl;
	}
	return 0;
}
