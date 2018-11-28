#include <iostream>
#include <fstream>
using namespace std;

#define C (1)
#define D (1)
#define LIMIT (C+D)

int combinations[LIMIT][3], combinationsCounter = 0;
void processList(string &a);

int main (int argc, char * const argv[]) {
    
	ifstream input(argv[1]);
	ofstream output("output.txt");
	
	int cases;
	input >> cases;
	
	
	
	int c, d, n;
	char *a;
	
	for (int i = 0; i < cases; i++) {
		input >> c;
		a = new char[3];
		for (int j = 0; j < c; j++) {
			input >> a;
			combinations[combinationsCounter][0] = a[0];
			combinations[combinationsCounter][1] = a[1];
			combinations[combinationsCounter++][2] = a[2];
		}
		delete []a;
		input >> d;
		a = new char[2];
		for (int j = 0; j < d; j++) {
			input >> a;
			combinations[combinationsCounter][0] = a[0];
			combinations[combinationsCounter][1] = a[1];
			combinations[combinationsCounter++][2] = -1;
		}
		delete[]a;
		input >> n;
		string b("");
		char v;
		for (int k = 0; k < n; k++) {
			input >> v;
			b.append(&v);
			processList(b);
		}
		string outStr("[");
		if (b.length()) {
			outStr.append(&b[0], 1);
		}
		for (int h = 1; h < b.length(); h++) {
			outStr.append(", ");
			outStr.append(&b[h], 1);
		}
		outStr.append("]");
		if (i+1 == 98) {
			cout << 5;
		}
		output << "Case #" << i+1 << ": " << outStr << endl;
		combinationsCounter = 0;
	}
    return 0;
}

void processList(string &a) {
	char lastAdded = a[a.length()-1];
	char secondLastAdded = a[a.length()-2];
	for (int s = 0; s < combinationsCounter; s++) {
		if ((combinations[s][0] == lastAdded && combinations[s][1] == secondLastAdded) || (combinations[s][1] == lastAdded && combinations[s][0] == secondLastAdded)) {
			if (combinations[s][2] != -1) {
				char c = combinations[s][2];
				a.replace((a.length()-2), 2, &c, 1);
				return;
			}
		}
	}
	
	for (int i = 0; i < a.length()-1; i++) {
			for (int s = 0; s < combinationsCounter; s++) {
				if ((combinations[s][0] == lastAdded && combinations[s][1] == a[i]) || (combinations[s][1] == lastAdded && combinations[s][0] == a[i])) {
					if (combinations[s][2] == -1) {
							//a.replace(i, a.length()-i, "");
						a.clear();
						a.append("");
						return;
					}
				}
		}
	}
}
