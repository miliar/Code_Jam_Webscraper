#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define HASH_SIZE 10001

int hash_func(string a);

struct seng {
	string name;
	int ref;
};

void main() {
	ifstream inputfile;
	ofstream outputfile;
	char inputfilename[100];
	char outputfilename[100];
	struct seng s_table[HASH_SIZE];
	int N, S, Q, i, cycle, loop, n_loop, s_num;
	string temp;
	char temp2[256];
	
	cout << "Enter the input file name : ";
	cin >> inputfilename;
	cout << "Enter the output file name : ";
	cin >> outputfilename;

	inputfile.open(inputfilename);
	outputfile.open(outputfilename);

	inputfile >> N;
	getline(inputfile, temp);
	
	cycle = 0;
	while(N>0) {

		inputfile >> S;
		getline(inputfile, temp);

		for(i=0;i<HASH_SIZE;i++) {
			s_table[i].name = "";
			s_table[i].ref = -1;
		}

		cycle++;

		i = S;

		while(i>0) {
			//inputfile >> temp;
			getline(inputfile, temp);
			cout << temp << endl;
			
			if(s_table[hash_func(temp)].name.length() == 0)
				s_table[hash_func(temp)].name = temp;
			else
				cout << "hash conflict!" << endl;

			i--;
		}

		inputfile >> Q;
		getline(inputfile, temp);

		loop = 0;
		n_loop = 0;
		s_num = 0;

		while(Q>0) {
			//inputfile >> temp;
			getline(inputfile, temp);

			if(s_table[hash_func(temp)].ref != loop) {
				s_table[hash_func(temp)].ref = loop;
				n_loop++;
			}

			if(n_loop == S) {
				s_num++;
				loop++;
				n_loop = 1;
				s_table[hash_func(temp)].ref = loop;
			}

			Q--;
		}

		outputfile << "Case #" << cycle << ": " << s_num << "\n";

		N--;
	}

	inputfile.close();
	outputfile.close();

	system("pause");
}

int hash_func(string a) {
	int ret, i;
	ret = 0;
	for(i=0;i<a.length();i++)
		ret += (int)(a[i]*a[i]);
	return ret%HASH_SIZE;
}