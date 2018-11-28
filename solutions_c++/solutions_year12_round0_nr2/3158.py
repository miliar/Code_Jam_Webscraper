
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int T;
int googlers, surprising, p;
vector<int> points;
vector<int> results;

void getInput(ifstream& inFile, bool first = false) {
	int readValue;

	if (!inFile)
		cout << "file read error" << endl;

	if (first) {
		inFile >> T;
		return;
	}
	points.clear();

	inFile >> googlers;
	inFile >> surprising;
	inFile >> p;

	for (int i = 0; i < googlers; i++) {
		inFile >> readValue;
		points.push_back(readValue);
	}

	/*
	int point;

	scanf("%d %d %d", &googlers, &surprising, &p);

	for (int i = 0; i < googlers; i++) {

		scanf("%d", &point);
		points.push_back(point);
	}*/
}

int test() {
	int result = 0;

	if (p == 1) {
		
		for (int i = 0; i < googlers; i++) {
			if (points[i])
				result++;
		}
		return result;
	}
	else if (!p) {

		return googlers;
	}
	else {

		int min = 3 * p - 2;

		for (int i = 0; i < googlers; i++) {

			if (points[i] >= min) 
				result++;
		}

		int surpMin = 3 * p - 4;
		int surpNum = 0;

		for (int i = 0; i < googlers && surpNum < surprising; i++) {

			if (points[i] >= surpMin && points[i] < min) {

				result++;
				surpNum++;
			}
		}
		return result;
	}
}

void showResults() {
	ofstream outFile;
	outFile.open("output.txt");

	for (int i = 0; i < T; i++) {
		outFile << "Case #" << i + 1 << ": " << results[i] << endl;
		cout << "Case #" << i + 1 << ": " << results[i] << endl;
	}

	outFile.close();
}

void main() {

	int result;
	char *inName = "input.txt";
    ifstream inFile(inName);

	getInput(inFile, true);
	
	for (int i = 0; i < T; i++) {

		getInput(inFile);
		result = test();
		results.push_back(result);
	}
	inFile.close();

	showResults();

	getchar();
}