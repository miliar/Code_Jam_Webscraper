#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

class classFeature {
public:
	double weight;
	string name;
	classFeature *leftSon, *rightSon;
};

ifstream inputFile;
ofstream outputFile;
char token;
string stringWeight, stringName;

void makeTree(classFeature *currentFeature) {
	while (true) {
		inputFile.get(token);
		if (token == '(')
			break;
	}

	while (true) {
		inputFile.get(token);
		if (!(token == ' ' || token == '\n'))
			break;
	}

	stringWeight = token;
	while (true) {
		inputFile.get(token);
		if (token == ' ' || token == '\n' || token == ')')
			break;

		stringWeight += token;
	}
	currentFeature->weight = atof(stringWeight.c_str());

	while (true) {
		if (!(token == ' ' || token == '\n'))
			break;

		inputFile.get(token);
	}

	if (token == ')')
		return;
	else {
		stringName = token;

		while (true) {
			inputFile.get(token);
			if (token == ' ' || token == '\n')
				break;

			stringName += token;
		}
		currentFeature->name = stringName;

		currentFeature->leftSon = new classFeature();
		makeTree(currentFeature->leftSon);
		currentFeature->rightSon = new classFeature();
		makeTree(currentFeature->rightSon);

		while (true) {
			inputFile.get(token);
			if (token == ')')
				break;
		}
	}
}

double calcProbability(map<string, bool> mapFeature, classFeature *currentFeature) {
	if (currentFeature->name == "")
		return currentFeature->weight;
	else {
		if (mapFeature[currentFeature->name] == true)
			return currentFeature->weight * calcProbability(mapFeature, currentFeature->leftSon);
		else
			return currentFeature->weight * calcProbability(mapFeature, currentFeature->rightSon);
	}
}

int main() {
	classFeature *root;
	int caseCount, lineCount, featureCount, i, j;
	string name, feature;
	map<string, bool> mapFeature;

	inputFile.open("A-large.in", ios::in);
	outputFile.open("output.txt", ios::out);
	
	inputFile >> caseCount;
	for (i = 1; i <= caseCount; i++) {
		//cout << "Case #" << i << endl;
		outputFile << "Case #" << i << ":" << endl;

		inputFile >> lineCount;
		root = new classFeature();
		makeTree(root);

		inputFile >> lineCount;
		for (; lineCount > 0; lineCount--) {
			inputFile >> name >> featureCount;
			mapFeature.clear();
			for (j = 0; j < featureCount; j++) {
				inputFile >> feature;
				mapFeature[feature] = true;
			}

			/*
			cout << fixed;
			cout.precision(7);
			cout << calcProbability(mapFeature, root) << endl;
			*/
			outputFile << fixed;
			outputFile.precision(7);
			outputFile << calcProbability(mapFeature, root) << endl;
		}
	}

	inputFile.close();
	outputFile.close();

	return 0;
}