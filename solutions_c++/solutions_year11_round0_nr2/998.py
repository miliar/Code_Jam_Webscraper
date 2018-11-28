#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main(){
	int t, teste = 1;
	int c, d, n;
	string str;
	
	map<pair<char, char>, char>::iterator m_it;
	set<pair<char, char> >::iterator s_it;
	
	cin >> t;
	while(t--){
		map<pair<char, char>, char> combine;
		set<pair<char, char> >forbidden;
		
		pair<char, char> p;
		vector<char> elements;
		
		cin >> c;
		for(int i = 0; i < c; i++){
			cin >> str;	
			p = make_pair(min(str[0], str[1]), max(str[0], str[1]));
			combine[p] = str[2];
		}
		cin >> d;
		for(int i = 0; i < d; i++){
			cin >> str;
			p = make_pair(min(str[0], str[1]), max(str[0], str[1]));
			forbidden.insert(p);
		}
		
		cin >> n >> str;
		for(int i = 0; i < n; i++){
			bool erased = false, flag = true;
			char act = str[i];
			//cout << "act " << act << endl;
			while(flag){
				if(elements.size() == 0) break;
				
				m_it = combine.find(make_pair(min(elements.back(), act), max(elements.back(), act)));
				if(m_it != combine.end()){
					act = m_it->second;
					elements.pop_back();
					//cout << "combined" << endl;
				}
				else{
					for(int j = 0; j < elements.size() && !erased; j++){
						//cout << j << endl;
						p = make_pair(min(act, elements[j]), max(act, elements[j]));
						s_it = forbidden.find(p);
						if(s_it != forbidden.end()){
							elements.clear();
							erased = true;
							//cout << "erased" << endl;
						}
					}
					flag = false;
				}
			}
			if(!erased) elements.push_back(act);
		}
		
		cout << "Case #" << teste++ << ": [";
		for(int i = 0; i < elements.size(); i++){
			if(i > 0)
				cout << ", ";
			cout << elements[i];
		}
		cout << "]\n";
	}
	return 0;
}
		
		
		
