#include <iostream>
#include <vector>
#include <string>

using namespace std;

int char2int(char c) {
	int ind;
	switch(c) {
		case 'Q':
			ind = 0;
			break;
		case 'W':
			ind = 1;
			break;
		case 'E':
			ind = 2;
			break;
		case 'R':
			ind = 3;
			break;
		case 'A':
			ind = 4;
			break;
		case 'S':
			ind = 5;
			break;
		case 'D':
			ind = 6;
			break;
		case 'F':
			ind = 7;
			break;
		default:
			ind = -1;
			break;
	}
	return ind;
}

int main() {
	
	int T;
	cin >> T;
	for (int z=0;z<T;z++) {
		// storage
		vector< vector<char> > baseCombine; // 8*8
		vector< vector<int> > baseClear;   // 8*8
		for (int i=0;i<8;i++) {
			vector<char> vc(8,' ');
			baseCombine.push_back(vc);
			vector<int> vcc(8,0);
			baseClear.push_back(vcc);
		}

		// read in
		int C,D,N;
		string NN;
		cin >> C;
		for (int i=0;i<C;i++) {
			string tmp;
			cin >> tmp;
			baseCombine[char2int(tmp[0])][char2int(tmp[1])] = tmp[2];
			baseCombine[char2int(tmp[1])][char2int(tmp[0])] = tmp[2];
		}
		cin >> D;
		for (int i=0;i<D;i++) {
			string tmp;
			cin >> tmp;
			baseClear[char2int(tmp[0])][char2int(tmp[1])] = 1;
			baseClear[char2int(tmp[1])][char2int(tmp[0])] = 1;
		}		
		cin >> N >> NN;
		
		// result
		vector<char> vec;

		for (unsigned int i=0;i<N;i++) {
			// copy one char
			vec.push_back(NN[i]);

			// combine if with 2 or more chars
			int sz = vec.size();
			if (sz>1) {
				char last1 = vec[sz-1];
				char last2 = vec[sz-2];
				int last11 = char2int(last1);
				int last22 = char2int(last2);
				if (last11==-1 || last22==-1) {
				} else { // two base elements at last
					char tmp = baseCombine[last22][last11];
					if (tmp == ' ') {
					} else {
						vec.pop_back();
						vec.pop_back();
						vec.push_back(tmp);
					}
				}		
			}

			sz = vec.size();
			if (sz>1) {
				char last1 = vec[sz-1];				
				int last11 = char2int(last1);
				if (last11!=-1) // last element is base element
					for (int j=2;j<=sz;j++) {// iterate through all other before last
						char last2 = vec[sz-j];
						int last22 = char2int(last2);
						if (last22!=-1) {// two base elements
							int tmp = baseClear[last22][last11];
							if (tmp==1) {// to clear
								vec.clear();
								break;
							}
						}		
					}
			}


		} // end for


		// output
		cout << "Case #" << z+1 << ": [";
		for (unsigned int i=0;i<vec.size();i++) {
			if (i==0)
				cout << vec[i];
			else
				cout << ", " << vec[i];
		}
		cout << "]" << endl;
	} // end one case
}