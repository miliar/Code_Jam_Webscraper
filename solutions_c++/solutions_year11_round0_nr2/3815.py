#include <iostream>
#include <list>
#include <map>
#include <utility>
using namespace std;

bool existInList(char c, list <char> myList){ // everyone knows bruteforce is awesome! *continues to not think*
	list <char>::iterator it;
	for (it = myList.begin(); it != myList.end(); it++){
		if (*it == c) return true;
	}
	return false;
}

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++){
		map <pair<char,char>,char> combine;
		map <char,char> oppose;	
		list <char> element_list;
		list <char>::iterator it;
		int C; cin >> C;
		while (C--) { // combinable element hashmap
			char a,b,c;
			cin >> a >> b >> c;
			combine[make_pair(a,b)] = c;
			combine[make_pair(b,a)] = c;
		}
		
		int D; cin >> D;
		while (D--) { // opposing element hashmap
			char a,b;
			cin >> a >> b;
			oppose[a] = b;
			oppose[b] = a;
		}

		int N; cin >> N;
		while (N--) {
			char curr;
			cin >> curr;
			bool action = false;
			// check if there are any combining to do 
			if (!element_list.empty()){
				if (combine.find(make_pair(element_list.back(),curr)) != combine.end()){
					char temp = element_list.back();
					element_list.pop_back();
					element_list.push_back(combine[make_pair(temp,curr)]);
					action = true;
				}
			}
			// check if there is opposing in string
			if (!element_list.empty() && !action) {
				if (oppose.find(curr) != oppose.end()){
					if (existInList(oppose[curr], element_list)) { // bruteforce check for opposing elements <- LOL
						element_list.clear();
						action = true;
					}
				}
			}
			// no combine or opposing so just add to elem list
			if (!action){
				element_list.push_back(curr);
			}
		}
		
		// output
		cout << "Case #" << (1 + i) << ": [";
		for (it = element_list.begin(); it != element_list.end(); it++){
			cout << *it; it++;
			if (it != element_list.end()) cout << ", ";
			it--;
		}
		cout << "]" << endl;
	}

}
