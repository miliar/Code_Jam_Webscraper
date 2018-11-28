#include <iostream>
#include <cstdio>
#include <list>
using namespace std;





class node
{

public:

	node()
	{
		memset(letters, 0, sizeof(letters));
	}

	node* letters[26];

};






void append(node* n, const char* str)
{
	if (*str) {
		if (n->letters[*str - 'a']) {
			append(n->letters[*str - 'a'], str + 1);
		} else {
			n->letters[*str - 'a'] = new node();
			append(n->letters[*str - 'a'], str + 1);
		}
	}
}



void contains(node* n, const char* search, unsigned long& count)
{
	// Trail letters until we hit something	
	while ((*search != 0) && (*search != '(')) {
		if (n->letters[*search - 'a']) {
			n = n->letters[*search - 'a'];
			search++;
		} else {
			// this thing is not here
			return;
		}
	}

	if (*search == 0) {
		count++;

	} else {

		const char* end = search;
		search++;
		while (*end != ')') {
			end++;
		}

		while (search != end) {
			if (n->letters[*search - 'a']) {
				contains(n->letters[*search - 'a'], end+1, count);
			}
			search++;
		}
	}
}




int main(int argc, char* argv[])
{
	unsigned long L = 0;
	unsigned long D = 0;
	unsigned long N = 0;

	cin >> L >> D >> N;

	char line[16384];


	node* root = new node();

	cin.getline(line, 16384);
	for (unsigned long i=0; i < D; i++) {
		cin.getline(line, 16384);
		append(root, line);
	}

	for (unsigned long i=0; i < N; i++) {
		unsigned long count = 0;
		cin.getline(line, 16384);
		contains(root, line, count);
		cout << "Case #" << i+1 << ": " << count << endl;
	}


	return 0;
}
