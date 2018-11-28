#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define IFILE "D:\\jam\\A.in"
#define OFILE "D:\\jam\\A.out"

typedef struct snode {
	string value;
	struct snode *son;
	struct snode *brother;
} node;

int main() {
	int T, M, N;
	node root;
	root.value = "/";
	root.son = NULL;
	root.brother = NULL;
	ifstream input;
	input.open(IFILE);
	ofstream output;
	output.open(OFILE);
	input >> T;
	for (int i = 1; i <= T; i++) {
		input >> N >> M;
		int count = 0;
		root.son = NULL;
		root.brother = NULL;
		
		for (int j = 0; j < N; ++j) {	
			string s;
			input >> s;
			node *current = &root;
			size_t lastfound = 0;
			size_t newfound = 0;
			while (newfound != string::npos) {
				//cout << "bla";
				newfound = s.find_first_of("/", lastfound + 1);
				string t = s.substr(lastfound+1, newfound - lastfound - 1);
				lastfound = newfound;
				if (current->son == NULL) {
					current->son = new node;
					
					current = current->son;
					current->value = t;
					current->son = current->brother = NULL;
				}
				else {
					current = current->son;
					while (current->value != t) {
						
							if (current->brother == NULL) {
								current->brother = new node;
								
								current = current->brother;
								current->value = t;
								current->son = current->brother = NULL;
								
							}
							else {
								current = current->brother;
							}
					}
				}

				//cout << t << endl;
				
			}

		}

		for (int j = 0; j < M; ++j) {
			
			string s;
			input >> s;
			node *current = &root;
			size_t lastfound = 0;
			size_t newfound = 0;
			while (newfound != string::npos) {
				//cout << "bla";
				newfound = s.find_first_of("/", lastfound + 1);
				string t = s.substr(lastfound+1, newfound - lastfound - 1);
				lastfound = newfound;
				if (current->son == NULL) {
					current->son = new node;
					count++; //cout << t;
					current = current->son;
					current->value = t;
					current->son = current->brother = NULL;
				}
				else {
					current = current->son;
					while (current->value != t) {
						
							if (current->brother == NULL) {
								current->brother = new node;
								count++; //cout << t;
								current = current->brother;
								current->value = t;
								current->son = current->brother = NULL;
								
							}
							else {
								current = current->brother;
							}
					}
				}

				//cout << t << endl;
				
			}

		}
		output << "Case #" << i << ": " << count << endl;
	}

	input.close();
	output.close();
	return 0;
}
