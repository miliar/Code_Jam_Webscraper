#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef struct {
	char a, b, c;
} combine;

typedef struct {
	char a, b;
} oppose;

vector<combine> cbn;
vector<oppose> opp;
vector<char> elems;

void check_combine() {
	for (int i = 0; i < elems.size(); i++) {
		for (int c = 0; c < cbn.size(); c++) {
			if ((elems[i] == cbn[c].a && i < elems.size() - 1 && elems[i+1] == cbn[c].b) || (elems[i] == cbn[c].b && i < elems.size() - 1 && elems[i+1] == cbn[c].a)) {
				elems.push_back(cbn[c].c);
				elems.erase(elems.begin() + i+1);
				elems.erase(elems.begin() + i);
			} else if ((elems[i] == cbn[c].a && i > 0 && elems[i-1] == cbn[c].b) || (elems[i] == cbn[c].b && i > 0 && elems[i-1] == cbn[c].a)) {
				elems.push_back(cbn[c].c);
				elems.erase(elems.begin() + i);
				elems.erase(elems.begin() + i-1);
			}
		}
	}
}

void check_oppose() {
	for (int o = 0; o < opp.size(); o++)
		for (int a = 0; a < elems.size(); a++)
			if (elems[a] == opp[o].a)
				for (int b = 0; b < elems.size(); b++)
					if (elems[b] == opp[o].b)
						elems.clear();
}

int main() {
	int cases;
	cin >> cases;
	
	for (int c = 1; c <= cases; c++) {
		cbn.clear();
		opp.clear();
		elems.clear();
		
		int count;
		string desc;
		
		cin >> count;
		while (count--) {
			cin >> desc;
			combine c;
			c.a = desc[0];
			c.b = desc[1];
			c.c = desc[2];
			cbn.push_back(c);
		}
		
		cin >> count;
		while (count--) {
			cin >> desc;
			oppose o;
			o.a = desc[0];
			o.b = desc[1];
			opp.push_back(o);
		}
		
		cin >> count;
		cin >> desc;
		for (int i = 0; i < desc.size(); i++) {
			/*cout << "[";
			if (!elems.empty())
			cout << elems[0];
			for (int e = 1; e < elems.size(); e++)
				cout << ", " << elems[e];
			cout << "] " << desc[i] << endl;*/
			
			elems.push_back(desc[i]);
			check_combine();
			check_oppose();
		}
		
		cout << "Case #" << c << ": [";
		if (!elems.empty())
			cout << elems[0];
		for (int i = 1; i < elems.size(); i++)
			cout << ", " << elems[i];
		cout << "]" << endl;
	}
	
	return 0;
}
