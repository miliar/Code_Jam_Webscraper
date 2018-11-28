//#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>
#include <math.h>


using namespace std;
using std::string;


ifstream fin("C-small-attempt0.in");
ofstream fout("output.txt");

int num;

int wordlength;
int tasklength;
int bufferlength;

void count(char * word, char * task, int wordpos, int taskpos) 
{
	char c = task[taskpos];
	int i;
	
	if (taskpos < tasklength - 1) {
		int newwordpos = wordlength;
		
		for (i = wordpos; i < wordlength-1; i++) {
			if (word[i] == c) {
				newwordpos = i+1;
				//cout << word[i] << c << endl;
				//cout << wordpos << " " << taskpos << endl;
				break;
			}
		}
		
		if (newwordpos <= wordlength-1) {	// still work to do		
			count(word, task, newwordpos, taskpos+1);
			count(word, task, newwordpos, taskpos);
		}
	} else {	// taskpos == tasklength - 1
		for (i = wordpos; i < wordlength; i++) {
			if (word[i] == c) {
				num++;
			//cout << " here " << wordpos << " " << taskpos << endl;
			}
		}
	}
}


int main()
{
	int i;
	
	char line[500];
	char task[] = "welcome to code jam";
	char c;
	char buffer[50];
	char * numchar = new char[5];
	int numline = 0;
	
	tasklength = strlen(task);
	
	fin >> numline;
	fin.getline(line, 500);
	
	for (i = 0; i < numline; i++) {
		num = 0;
		
		fin.getline(line, 500);
		wordlength = strlen(line);
		cout << "wordlength: " << wordlength << endl;
		count(line, task, 0, 0);
		cout << "# words: " << num << endl;
		itoa(num, buffer, 10);
		fout << "Case #" << i+1 << ": ";
		bufferlength = strlen(buffer);
		
		for (int j = 4; j >= 1; j--) {
			if (bufferlength - j >= 0) {
				numchar[4-j] = buffer[bufferlength - j];
			} else {
				numchar[4-j] = '0';
			}
		}
		numchar[4] = '\0';
		fout << numchar << "\n";
	}
	
	fin.close();
	fout.close();
	
	// c = line[i];
	// while (c != '\0') {
		// cout << c << endl;
		// i++;
		// c = line[i];
	// }
	
	return 0;
}
