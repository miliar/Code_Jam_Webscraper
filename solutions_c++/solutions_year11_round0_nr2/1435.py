#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) {
    //ifstream in("..//..//sample.in.txt");
	//ifstream in("..//..//B-small-attempt3.in.txt");
	ifstream in("..//..//B-large.in.txt");
	
	if (!in) {
		cout << "Input file cannot be opened";
		return 1;
	}
	
	ofstream out("output.txt");
	if (!out) {
		cout << "Output file cannot be opened";
		in.close();
		return 1;
	}
	
	int T;
	in >> T;
	
	for (int t = 0; t < T; t++) {
		int C, D, N;
		in >> C;
		char combine1[C], combine2[C], combineResult[C];
		for (int c = 0; c < C; c++) {
			in >> combine1[c] >> combine2[c] >> combineResult[c];
			cout << combine1[c] << " + " << combine2[c] << " = " << combineResult[c] << endl;
		}
		
		in >> D;
		char oppose1[D], oppose2[D];
		for (int d = 0; d < D; d++) {
			in >> oppose1[d] >> oppose2[d];
			cout << oppose1[d] << " x " << oppose2[d] << endl;
		}
		
		in >> N;
		char invokeList[N];
		for (int n = 0; n < N; n++) {
			in >> invokeList[n];
			cout << invokeList[n] << " ";
		}
		cout << endl << endl;
		
		vector<char> finalList;
		char prevElement = invokeList[0];
		for (int n = 1; n < N; n++) {
			cout << invokeList[n] << " ";
			
			if (prevElement == ' ') {
				prevElement = invokeList[n];
				continue;
			}
			
			char currElement = invokeList[n];
			
			bool combined = false;
			// determine if combination is possible
			for (int c = 0; c < C; c++) {
				if ((prevElement == combine1[c] && currElement == combine2[c]) ||
					(prevElement == combine2[c] && currElement == combine1[c])) {
					prevElement = combineResult[c];
					combined = true;
					break;
				}
			}
			if (combined)
				continue;
			
			bool opposed = false;
			// determine if opposition is possible
			for (int d = 0; d < D; d++) {
				char otherOpposeElement = ' ';
				if (currElement == oppose1[d]) {
					otherOpposeElement = oppose2[d];
				}
				else if (currElement == oppose2[d]) {
					otherOpposeElement = oppose1[d];
				}
				if (otherOpposeElement == ' ') {
					continue;
				}
				
				if (prevElement == otherOpposeElement)
					opposed = true;
				for (int i = 0; i < finalList.size(); i++) {
					if (finalList[i] == otherOpposeElement) {
						opposed = true;
					}
				}
			}
			if (opposed)
			{
				finalList.clear();
				prevElement = ' ';
				cout << "<clear>";
				continue;
			}
			
			finalList.push_back(prevElement);
			prevElement = currElement;
			
			
			cout << "Case " << (t + 1) << ": [";
			for (int i = 0; i < finalList.size(); i++) {
				cout << finalList[i];
				if (i != finalList.size() - 1)
					cout << ", ";
			}
			cout << "]" << endl;
		}
		if (prevElement != ' ')
			finalList.push_back(prevElement);
		
		out << "Case #" << (t + 1) << ": [";
		for (int i = 0; i < finalList.size(); i++) {
			out << finalList[i];
			if (i != finalList.size() - 1)
				out << ", ";
		}
		out << "]" << endl;
		
		cout << "Case #" << (t + 1) << ": [";
		for (int i = 0; i < finalList.size(); i++) {
			cout << finalList[i];
			if (i != finalList.size() - 1)
				cout << ", ";
		}
		cout << "]" << endl << endl << endl;
	}
	
	in.close();
	out.close();
	
    return 0;
}
