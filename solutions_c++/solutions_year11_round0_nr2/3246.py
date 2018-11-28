#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <deque>

using namespace std;

int main() {
	int cases,inputs;

	string element,list;

	char combine;
	bool opposite;
	
	cin >> cases;
	
	for(int i = 1; i <= cases; i++ ) {
		deque<string> combines,opposites;
		deque<char> elements;
		
		cin >> inputs;
		// Get the elements that combines
		for(int k = 0; k < inputs; k++) {
			cin >> element; 
			combines.push_back(element);
		}
		
		cin >> inputs;
		// Get the opposites
		for(int k = 0; k < inputs; k++) {
			cin >> element;
			opposites.push_back(element);
		}
		
		cin >> inputs;
		cin >> list;

		// Play the game on the fly
		for(int k = 0; k < inputs; k++)	 {
			combine = '\0';
			opposite = false;

			// Search on the list if it combines
			if(elements.size() > 0) {
				for(int m = 0; m < combines.size(); m++)
					if(combines[m][0] == list[k] && combines[m][1] == elements.back()) {
						combine = combines[m][2];
						break;
					}
					else if(combines[m][1] == list[k] && combines[m][0] == elements.back()) {
						combine = combines[m][2];
						break;
					}
			}

			// If it doesnt combine so we search if it have some opposite
			for(int m = 0; m < opposites.size(); m++) {
				if(opposites[m][0] == list[k]) {
					for(int n = 0; n < elements.size(); n++) 
						if(opposites[m][1] == elements[n]) {
							opposite = true;
							break;
						}
				}			
				else if(opposites[m][1] == list[k]) {
					for(int n = 0; n < elements.size(); n++)
						if(opposites[m][0] == elements[n]) {
							opposite = true;
							break;
						}
				}
			}

			// Magicka		
			if(combine != '\0') {
				elements.pop_back();
				elements.push_back(combine);
			}
			else
				if (opposite == true)
					elements.clear();
				else
					elements.push_back(list[k]);
			
		}

		// Print the solution
		cout << "Case #" << i << ": [";
		
		for(int k = 0; k < elements.size(); k++)
				if(k != elements.size() - 1)
					cout << elements[k] << ", ";					
				else
					cout << elements[k];
					
		cout << "]" << endl;
	}
	return 0;
}
