#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>

#define PB push_back
#define MP make_pair
#define ULL unsigned long long

using namespace std;

int main () {
	int cases;
	cin >> cases;
	for(int case_i = 1; case_i <= cases; case_i++){
		ULL num_other; ULL LOW; ULL HIGH;
		cin >> num_other; cin >> LOW; cin >> HIGH;
		
		ULL* others;
		others = new ULL[num_other];
		for(ULL i = 0; i < num_other; i++)
			cin >> others[i];
		
		
		cout << "Case #" << case_i << ": ";
		
		bool pos = false;
		ULL j = 0;
		for (j = LOW; j <= HIGH; j++) {
			
			ULL sum = 0;
			for(ULL i = 0; i < num_other; i++){
				ULL a1 = j % others[i];
				ULL a2 = others[i] % j;
				if( a1 == 0 ||  a2 == 0){
					sum++;
				}
			}
			if(sum == num_other){
				pos = true;
				break;
			}
		}
		
		if(pos)
			cout << j << endl;
		else
			cout << "NO" << endl;
		

		delete(others);

	}
    return 0;
}
