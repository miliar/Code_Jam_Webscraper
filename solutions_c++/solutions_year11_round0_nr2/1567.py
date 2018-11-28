#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <utility>
#include <map>

using namespace std;

int main(){
	int test;
	cin >> test;

	// Intitialization of elements
	map <char, int> element;
	pair <char, int> el;
	
	el.first = 'Q';
	el.second = 0;
	element.insert (el);
	
	el.first = 'W';
	el.second = 1;
	element.insert (el);

	el.first = 'E';
	el.second = 2;
	element.insert (el);

	el.first = 'R';
	el.second = 3;
	element.insert (el);

	el.first = 'A';
	el.second = 4;
	element.insert (el);

	el.first = 'S';
	el.second = 5;
	element.insert (el);

	el.first = 'D';
	el.second = 6;
	element.insert (el);

	el.first = 'F';
	el.second = 7;
	element.insert (el);

	for (int z = 0; z < test; z++){
		int C, D, N;
		

		vector <list <pair <char, char> > > concor(8); 
		vector <list <char> > discor (8);
		vector <int> count(8);

		string x;

		cin >> C;
		for (int i = 0; i < C; i++){
			cin >> x;
			pair <char, char> temp;
			temp.first = x[1];
			temp.second = x[2];
			concor[ element.find(x[0])->second ].push_back(temp);

			temp.first = x[0];
			concor[ element.find(x[1])->second ].push_back(temp);
		}
 
		cin >> D;
		for (int i = 0; i < D; i++){
			cin >> x;
			discor[ element.find(x[0])->second ].push_back (x[1]);
			discor[ element.find(x[1])->second ].push_back (x[0]);
		}

		cin >> N;
		cin >> x;
		int s = x.size();
		string soln;
		
		for (int i = 0; i < s; i++){
			int index = element [x[i]];

			// If solution has been discorded
			if (soln.empty()){
				soln.push_back (x[i]);
				continue;
			}

			// Check Concor
			char last = soln[soln.size() - 1];
	
			list <pair<char, char> > :: iterator cit;
			for (cit = concor[index].begin(); cit != concor[index].end(); cit++){
				if (cit->first == last){
					soln[soln.size() - 1] = cit->second;
					break;
				}
			}
			if (cit != concor[index].end()){
				continue;
			}
		

			//Check Discor
			int t = soln.size();
			int j;
			for (j = 0; j < t; j++){
				list <char> :: iterator dit;
				for (dit = discor[index].begin(); dit != discor[index].end(); dit ++){
					if (soln[j] == *(dit)){
						soln.clear();
						break;
					}
				}
				if (dit != discor[index].end()){
					break;
				}
			}

			if (j == t){
				soln.push_back (x[i]);
			}
		}

		// Output
		cout << "Case #" << z+1 << ": [";
		for (int k = 0; k < soln.size(); k++){
			cout << soln[k];
			if (k != soln.size() - 1){
				cout << ", ";
			}
			
		}
		cout << "]";

		if (z != test){
			cout << endl;
		}
	}
}