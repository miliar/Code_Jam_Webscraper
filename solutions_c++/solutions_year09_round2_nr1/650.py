#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

struct tree {
	double weight;
	string feature;
};

typedef vector <struct tree> Tree;
typedef vector <string> Animal;
Tree v;


tree read_tree (int i) {
	double w;
	string f;
	tree a;
	char c;

	cin >> c;
	if (c == '(') {
		cin >> w;
		cin >> c;
		if(c != ')') {
			f.clear();
			while(c!='\n') {
				f.push_back(c);
				c=getchar();
			}
			a.feature = f;
			a.weight = w;
			v[i] = a;
			read_tree(2*i);
			read_tree(2*i+1);
			cin >> c;
		}
		else {
			f.clear();
			a.feature = f;
			a.weight = w;
			v[i] = a;
		}
	}
	
	return a;

}

double prob (Animal a) {
	int i=1;
	double p=1;

	while(1) {
		p *= v[i].weight;
		if(!v[i].feature.empty()) {
			if(find(a.begin(), a.end(), v[i].feature) != a.end())
				i = 2*i;
			else
				i = 2*i+1;
		}
		else {
			return p;
		}
	}
}

int main () {
	int t, T;
	int A;
	tree aux;
	Animal a;
	string name, s;
	char c;
	int i, j, n;
	double p;

	cin >> T;

	for(t=1; t<=T; t++) {

		cin >> i;
		v.clear();
		aux.feature.clear();
		aux.weight = -1;
		for(i=0; i<100000; i++)
			v.push_back(aux);
		read_tree(1);
//for(i=1; i<20; i++) cout << v[i].feature << " = " << v[i].weight << endl;
		
		cout << "Case #" << t << ":" << endl;

		cin >> A;
//cout << A << endl;
		for (i=0; i<A; i++) {
			cin >> name;
			cin >> n;
			a.clear();
			for (j=0; j<n; j++) {
				cin >> s;
				a.push_back(s);
			}
			p = prob(a);
			cout.precision(7);
			cout.width(9);
			cout << fixed << p << endl;
		}

	
	}

	return 0;
}