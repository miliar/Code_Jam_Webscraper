#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {

	int cases;
	cin >> cases;
	
	int numGooglers, surprising, bestscore;
	vector<int> totalpts;
	
	for(int i = 0; i < cases; i++) {
		cin >> numGooglers >> surprising >> bestscore;
		totalpts.resize(numGooglers);
		
		for(int j = 0; j < numGooglers; j++) {
			cin >> totalpts[j];
		}
		int numAwesome = 0;
		for(int j = 0; j < totalpts.size(); j++) {
			int subtract = bestscore - 1;
			if(subtract < 0) subtract = 0;
			int score = bestscore + subtract * 2;
			
			if(score <= totalpts[j]) {
				numAwesome++;
				totalpts.erase(totalpts.begin() + j);
				j--;
				continue;
			}
		}
		for(int j = 0; j < totalpts.size() && surprising > 0; j++) {
			
			int subtract = bestscore - 2;
			if(subtract < 0) subtract = 0;
			int score = bestscore + subtract * 2;
			
			if(score <= totalpts[j]) {
				surprising--;
				numAwesome++;
				continue;
			}
		}
		
		cout << "Case #" << i + 1 << ": " << numAwesome << endl;
		
	}
	
	return 0;
}
