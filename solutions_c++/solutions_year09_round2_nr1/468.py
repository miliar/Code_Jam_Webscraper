#include <iostream>
#include <fstream>
#include <iomanip>


using namespace std;

	ifstream fin;
	ofstream fout;

class tree{
public:
	int ls, rs;
	double weight;
	char * feature;
};

tree trees[8000];
char * input;
int inputL, inputNow;
int treeLines, nowTreeLine, treeNum;
	int featureNum;
	char * animal[100];
	double ans;

char nextChar() {
	if (inputNow == inputL) {
		nowTreeLine ++;
		if (nowTreeLine > treeLines) {
			cout << "no more chars!" << endl;
			return '\0';
		}
		fin.getline(input, 255);
		inputL = strlen(input);
		input[inputL] = '\n';
		inputL ++;
		inputNow = 0;
	}

	return input[inputNow ++];
}

bool isBlank(char x) {
	return (x == ' ' || x == '\n');
}

char nextNoneBlankChar() {
	char x ;
	do {
		x = nextChar();
		if (!isBlank(x)) break;
	} while (1);
	return x;
}

void readTree(int index) {
	//get weight
	char x, * w = new char[100];
	int wl = 0, fl = 0;
	x = nextNoneBlankChar();
	if (x != '(') {
		cout << "wrong input 1!" << endl;
		return;
	}
	x = nextNoneBlankChar();
	while (x == '.' || (x >= '0' && x <= '9')) {
		w[wl ++] = x;
		x = nextChar();
	}
	w[wl] = '\0';
	trees[index].weight = atof(w);

	//get feature
	if (isBlank(x)) x = nextNoneBlankChar();
	if (x == ')') {
		trees[index].feature = NULL;
		trees[index].ls = trees[index].rs = -1;
		return;
	}
	trees[index].feature = new char[11];
	while (!isBlank(x)) {
		trees[index].feature[fl ++] = x;
		x = nextChar();
	}
	trees[index].feature[fl] = '\0';
	//get subtrees
	treeNum ++; trees[index].ls = treeNum;
	treeNum ++; trees[index].rs = treeNum;
	readTree(trees[index].ls);
	readTree(trees[index].rs);
	
	x = nextNoneBlankChar();
	if (x != ')') {
		cout << "wrong input 2!" << endl;
		return;
	}
	return;
}
void writeTree(int index, int suojin) {
	for (int i = 0; i < suojin; i++) cout << '\t';
	cout << trees[index].weight << ' ';
	if (trees[index].feature == NULL) {
		cout << endl;
		return;
	}
	cout << trees[index].feature << endl;
	writeTree(trees[index].ls, suojin + 1);
	writeTree(trees[index].rs, suojin + 1);
}

void find(int index) {
	ans *= trees[index].weight;

	if (trees[index].feature == NULL) return;

	bool flag = false;
	for (int i = 0; i < featureNum; i++)
		if (strcmp(trees[index].feature, animal[i]) == 0) {
			flag = true; break;
		}
	if (flag)
		find(trees[index].ls);
	else 
		find(trees[index].rs);
	return;
}

void output(double ans) {
	fout << int(ans) << '.';
	for (int i = 0; i < 7; i++) {
		ans *= 10;
		fout << int(ans) % 10;
	}
	fout << endl;
}

int main() {
	input = new char[255];

//	fin.open("A-small.in");
//	fout.open("A-small.out");
	fin.open("A-large.in");
	fout.open("A-large.out");
	int caseNum, animalNum;
	for (int i = 0; i < 100; i++) animal[i] = new char[255];

	fin >> caseNum;
	for (int cases = 1; cases <= caseNum; cases ++) {
		treeNum = 0;

		input[0] = '\0';
		inputL = 0; inputNow = 0;

		fin >> treeLines; 
		fin.getline(input, 255);
		nowTreeLine = 0;
		readTree(treeNum);
		
//		writeTree(0, 0);

		while (nowTreeLine < treeLines) {
			nowTreeLine ++;
			fin.getline(input, 255);			
		}

		fout << "Case #" << cases << ":\n";

		fin >> animalNum;

		for (int iani = 0; iani < animalNum; iani ++) {
			fin >> animal[0];
			fin >> featureNum;
			for (int i = 0; i < featureNum;i++)
				fin >> animal[i];
			ans = 1;
			find(0);
			output(ans);
		}


	}


	fin.close();
	fout.close();
	return 0;
}