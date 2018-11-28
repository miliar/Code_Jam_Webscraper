#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>

// The maximum lenght of each line
#define G 102

using namespace std;

// ********************************************************************
// Static variables ***************************************************
// ********************************************************************

// The mapping of the letters
static map<char, char> alphabet;

// The example input
static char inputs[3][G] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};
// The example output
static char outputs[3][G] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
	};

// Where I'm going to put the solution of each test
static char solution[G];

// I use it to find the only one letter not translated
static bool letters[26];

// ####################################################################
// Functions ##########################################################
// ####################################################################

// Insert the letter c in the with the result trans and mark the letter
// trans as used
void insert_letter(char c, char trans) {
	alphabet[c] = trans;
	letters[trans-'a'] = false;
}

// Test if the char c is a space
bool is_not_space (char c) {
	return c != ' ';
}

// Test if the char c is in the map
bool is_in_map (char c) {
	return alphabet.count(c) > 0;
}

// Test if the char c is not in the map
bool is_not_in_map (char c) {
	return alphabet.count(c) == 0;
}

// I use the example input to get the map complete, but 'q'
void decode() {
	for (int i = 0; i < 3; ++i) {
		char *line1 = inputs[i], *line2 = outputs[i];
		for (int j = 0, l = strlen(line1); j < l; ++j) {
			char c1 = line1[j], c2 = line2[j];
			if (is_not_space(c1) && is_not_in_map(c1)) {
				insert_letter(line1[j], c2);
			}
		}
	}
}

// I have not just the translation of only one letter that means 'q', yet
void last() {
	for (int i = 0; i < 26; ++i) {
		if (is_not_in_map(i+'a')) {
			insert_letter(i+'a', 'q');
			break;
		}
	}
}

// Initialize the map with some values
void init() {
	for (int i = 0; i < 26; ++i) letters[i] = true;
	insert_letter('y', 'a');
	insert_letter('e', 'o');
	insert_letter('q', 'z');
	decode();
	last();
}

// Solve a test
void translate() {
	for (int i = 0, l = strlen(solution); i < l; ++i) {
		char c = solution[i];
		if (is_not_space(c)) {
			solution[i] = alphabet[c];
		}
	}
}

// When I have the solution for a case then show it
void print_solution(int c, FILE *fout) {
	fprintf(fout, "Case #%d: %s\n", c, solution);
}

// &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
// Main &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
// &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

int main (int argc, char *argv[]) {
	int cases;
	FILE *fin = fopen("A-small-attempt7.in", "r"), *fout = fopen("A-small-attempt7.out", "w");
	// Read the number of cases
	char *aux;
	fgets(aux, G, fin);
	cases = atoi(aux);

	// Use the examples to complete the mapping
	init();
	
	// For each case we translate:
	for (int i = 0; i < cases; ++i) {
		fgets(solution, G, fin);
		translate();
		print_solution(i+1, fout);
	}

	fclose(fin); fclose(fout);
	return 0;
}