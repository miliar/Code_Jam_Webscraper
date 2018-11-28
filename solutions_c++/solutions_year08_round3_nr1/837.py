// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include <set>
#include <algorithm>

using namespace std;

typedef struct {
	int x, y; 
} Point;

typedef struct {
	int freq;
	int index; 
} Letter;

struct classcomp {
  bool operator() (const int& lhs, const int& rhs) const
  {return lhs<rhs;}
};

struct Comparator
{
     bool operator()(Letter& l0, Letter& l1)
	 {
		 return (l0.freq > l1.freq); 
     }
};



int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input_file;

	if (argc < 2) return 1;
	input_file.open(argv[1]);
	if (!input_file.good()) return 1;

	int num_cases; 
	input_file >> num_cases;
	int max_letters_per_key;
	int num_keys_available; 
	int num_letters; 
	vector<Letter> letters; 
	int num_presses; 
	Letter letter; 
	//set<int,classcomp> letters_on_key; 
	vector<vector<Letter> > letters_on_keys;  
	for (int i = 0; i < num_cases; i++) {
		input_file >> max_letters_per_key >> num_keys_available >> num_letters;
		letters.resize(num_letters);
		for (int j = 0; j < num_letters; j++) {
			input_file >> letter.freq;
			letter.index = j;
			letters[j] = letter; 
		}
		sort(letters.begin(), letters.end(), Comparator()); 

		letters_on_keys.resize(num_keys_available);
		
		int key = 0; 
		for (int k = 0; k < num_letters; k++) {
			letters_on_keys[key].push_back(letters[k]);
			key++;
			if (key == num_keys_available) key = 0; 
		}
		
		num_presses = 0; 
		int size; 
		for (int j = 0; j < num_keys_available; j++) {
			size = (int)letters_on_keys[j].size();
			for (int m = 0; m < size; m++) {
				num_presses += (m+1)*letters_on_keys[j][m].freq;
			}
		}

		/*
		int k = 0;
		for (int j = 0; j < num_keys_available; j++) {
			letters_on_keys[j].push_back(letters[k]); 
			k += max_letters_per_key; 
			if (k >= num_letters) k %= num_letters;
		}
		*/
		cout << "Case #" << i+1 << ": " << num_presses << endl;
		

		letters.clear(); 
		letters_on_keys.clear();
	}



	return 0;
}

