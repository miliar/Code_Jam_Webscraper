#include <set>
#include <utility>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
set<pair<int, int> > mappings;

bool pair_cmp (pair<int, int> p1, pair<int, int> p2){
    return (p1.first == p2.first) ? p1.second < p2.second : p2.first < p2.first;
}

int pairSearch(pair<int, int> p1){
	if (mappings.find(p1) != mappings.end()) {
 	 return 0;
	} else {
 	 //not in the set, so needs to be inserted
	  mappings.insert(pair<int, int>(p1.first, p1.second));
      return 1;
	}
}


int main () {
    int t;
    cin >> t;

//io bullshit
int count = 0, A, B;
int num_digits = 0, new_number = 0;

for (int tick = 0;tick < t; ++tick) {
    cin >> A >> B;
    count = 0;
	for (int i = A; i < B; ++i){
		
		num_digits = floor(log10(i))+1;
        int old_num = i; 
		for (int j = 0; j < num_digits; ++j){

			i = i/10 + pow(10, num_digits - 1) * (i % 10);
		    if(old_num < i && i <= B)
                count+=pairSearch(pair<int, int>(old_num, i));
		}
        i = old_num;
		}
    cout << "Case #" << tick+1 << ": " << count << endl;
    mappings.clear();
}
}
