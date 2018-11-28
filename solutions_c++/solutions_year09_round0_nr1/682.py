#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main()
{

	vector<string> dict;

	vector<int> possible;

	int L, D, N;
	int i, p;

	int counter;

	string temp;
	string token;
	string word;

	cin >> L >> D >> N;

	for (i=0; i<D; i++){

		cin >> temp;	
		dict.push_back(temp);
	}

	cin.ignore(10, '\n');
	//	for (i=0; i<D; i++) cout << dict[i] << endl;


	for (p=1; p<=N; p++){

		getline(cin, word, '\n');


		string::iterator pointer;
		counter = -1;

		possible.assign(D, 1);
//		cout << "Word is " << word << endl;

		for (pointer = word.begin(); pointer != word.end(); pointer++){

			token.clear();
			counter++;
			if (*pointer == '('){

				pointer++;
				while (*pointer != ')'){
					token.push_back(*pointer);
					pointer++;
				}
			}
			else{
				token.push_back(*pointer);
			}

//			cout << token << endl;

			string::iterator tpointer;
			vector<string>::iterator dpointer;

			int dword, poss;
			for (dword = 0, dpointer = dict.begin(); dpointer != dict.end(); dpointer++, dword++){
				poss = 0;
				for (tpointer = token.begin(); tpointer != token.end(); tpointer++){
//					cout << (*dpointer)[counter] << " vs " << *tpointer << endl;
			
					if ((*dpointer)[counter] == *tpointer) poss = 1;
				}
				if (poss == 0) possible[dword] = 0; 
			}
		}

		vector<int>::iterator ppointer;	
		int answer = 0;

		for (ppointer = possible.begin(); ppointer != possible.end(); ppointer++)
			
			if (*ppointer == 1) answer++;

		cout << "Case #" << p << ": " << answer << endl;


	}

	return 0;
}

