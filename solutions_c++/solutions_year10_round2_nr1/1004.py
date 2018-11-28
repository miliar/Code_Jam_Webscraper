#include <iostream>
#include <list>
#include <vector>
#include <string>

using namespace std;

class Dossier {
	public:
		string name;
		list<Dossier> subs;

		Dossier(string myname) : name(myname) { }
		short add(string nameDossier) {
			if((*this)[nameDossier]->name == "~DONTEXIST") {
				Dossier nouveau(nameDossier);
				subs.push_back(nouveau);
				return 1;
			}
			return 0;
		}

		Dossier* operator[](string sub) {
			for(list<Dossier>::iterator i = subs.begin(); i!=subs.end() ; i++) {
				if(i->name == sub)
					return &(*i);
			}
			Dossier* no = new Dossier("~DONTEXIST");
			return no;
		}

		vector<string> print() {
			vector<string> paths;
			paths.push_back(name);
			for(list<Dossier>::iterator i=subs.begin() ; i!=subs.end() ; i++) {
				vector<string> subPaths = i->print();
				for(vector<string>::iterator j=subPaths.begin() ; j!=subPaths.end() ; j++) {
					if(name == "/")
						paths.push_back(name+(*j));
					else
						paths.push_back(name+"/"+(*j));
				}
			}
			return paths;
		}
};

void printDossiers(vector<string> dossiers) {
	for(vector<string>::iterator j=dossiers.begin() ; j!=dossiers.end() ; j++) {
		cout << (*j) << endl;
	}
}

int main() {
	int nbTests;
	cin >> nbTests;

	for(int t=1 ; t <= nbTests ; t++) {
		int n, m;
		cin >> n >> m;

		Dossier root("/");
		for(int i=0 ; i<n ; i++) {
			string path;
			cin >> path;

			Dossier* ptr = &root;
			string tmpDossier;
			for(int c=1 ; c<path.length() ; c++) {
				if(path[c] != '/')
					tmpDossier += path[c];
				else {
					ptr->add(tmpDossier);
					ptr = (*ptr)[tmpDossier];
					tmpDossier = "";
				}
			}
			ptr->add(tmpDossier);
		}

		int nbMakes = 0;
		for(int i=0 ; i<m ; i++) {
			string path;
			cin >> path;

			Dossier* ptr = &root;
			string tmpDossier;
			for(int c=1 ; c<path.length() ; c++) {
				if(path[c] != '/')
					tmpDossier += path[c];
				else {
					nbMakes += ptr->add(tmpDossier);
					ptr = (*ptr)[tmpDossier];
					tmpDossier = "";
				}
			}
			nbMakes += ptr->add(tmpDossier);
		}

		cout << "Case #" << t << ": " << nbMakes << endl;
	}
}
