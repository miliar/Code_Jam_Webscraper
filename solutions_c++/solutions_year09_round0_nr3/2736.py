// codejam.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <deque>
#include <vector>
#include <iomanip>


using namespace std;

static unsigned long long counter=0;
char sentence[] = {"welcome to code jam"};
int ssize=strlen(sentence);

int solve(const char * paragraph, int pindex, int sindex, int  size){
	if (sindex == ssize) {
		counter++;
		return 0;
	}
	for (int i=pindex; i<size; i++){
		if (paragraph[i] == sentence[sindex])
			solve(paragraph, i+1, sindex+1, size);
	}

	return 0;
}

int main()
{
	ofstream outfile("output.txt");
	

	string str;
	stringstream ss;


	ifstream infile("input.txt");

	getline(infile, str);
	ss << str;
	int N=0;
	ss >> N;
	cout << N << endl;
	for (int i=1; i<=N; i++){
		getline(infile, str);
		cout << str << endl;
		int pindex=0, sindex=0;
		counter = 0;
		solve(str.c_str(), pindex, sindex, str.size());
		stringstream ss;
		outfile.fill('0');
		outfile << "Case #" << i << ": " <<setw(4)<<counter%1000 << endl;

		
	}
	infile.close();
	int a=0;
	cin >> a;

}



