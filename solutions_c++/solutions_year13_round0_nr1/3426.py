#include<iostream>
#include<fstream>
#include<string>

using namespace std;

string pripad(int i, string* radky);

int main() {
	ifstream myReadFile;
	myReadFile.open("input.in");
	ofstream myWriteFile;
	myWriteFile.open("output.out");
	string output;
	if (myReadFile.is_open()) {
		myReadFile >> output;
		int pocet_pripadu = atoi(output.c_str());
		//pocet_pripadu = 4;
		cout << pocet_pripadu<<"\n";
		for (int i = 1;i<=pocet_pripadu;i++) {
			string* radky;
			radky = new string[4];
			for (int j = 0;j<4;j++) {
				myReadFile >> output;
				radky[j] = output;
			}
			string reseni = pripad(i, radky);
			cout<<"Case #"<<i<<": "<<reseni<<"\n";
			myWriteFile<<"Case #"<<i<<": "<<reseni<<"\n";
		}
	}
	myReadFile.close();
	myWriteFile.close();
	cin>>output;
	return 0;
}

string pripad(int i, string* radky) {
	string navrat = "";
	bool free_spot = false;
	for (int i = 0;i<4;i++) {
		cout << radky[i]<<"\n";
	}
	// projde vsechny vodorovne
	bool x_win = true;
	bool o_win = true;
	for (int i = 0;i<4;i++) {
		x_win = true;
		o_win = true;
		for (int j = 0;j<4;j++) {
			string s = radky[i].substr(j,1);
			if (!s.compare("X")) {
				o_win = false;
			}
			if (!s.compare("O")) {
				x_win = false;
			}
			if (!s.compare(".")) {
				x_win = false;
				o_win = false;
				free_spot = true;
			}
		}
		if (x_win) {
			navrat = "X won";
		}
		if (o_win) {
			navrat = "O won";
		}
	}
	// projde vsechny svisle
	for (int i = 0;i<4;i++) {
		x_win = true;
		o_win = true;
		for (int j = 0;j<4;j++) {
			string s = radky[j].substr(i,1);
			if (!s.compare("X")) {
				o_win = false;
			}
			if (!s.compare("O")) {
				x_win = false;
			}
			if (!s.compare(".")) {
				x_win = false;
				o_win = false;
			}
		}
		if (x_win) {
			navrat = "X won";
		}
		if (o_win) {
			navrat = "O won";
		}
	}
	// projde diagonalu zleva nahore doprava dolu
	x_win = true;
	o_win = true;
	for (int i = 0;i<4;i++) {

		string s = radky[i].substr(i,1);
		if (!s.compare("X")) {
			o_win = false;
		}
		if (!s.compare("O")) {
			x_win = false;
		}
		if (!s.compare(".")) {
			x_win = false;
			o_win = false;
		}
	}
	if (x_win) {
		navrat = "X won";
	}
	if (o_win) {
		navrat = "O won";
	}
	// projde diagonalu zleva nahore doprava dolu
	x_win = true;
	o_win = true;
	for (int i = 0;i<4;i++) {

		string s = radky[i].substr(3-i,1);
		if (!s.compare("X")) {
			o_win = false;
		}
		if (!s.compare("O")) {
			x_win = false;
		}
		if (!s.compare(".")) {
			x_win = false;
			o_win = false;
		}
	}
	if (x_win) {
		navrat = "X won";
	}
	if (o_win) {
		navrat = "O won";
	}
	// vystup
	if (!navrat.compare("")) {
		if (free_spot) {
			navrat = "Game has not completed";
		} else {
			navrat = "Draw";
		}
	}
	return navrat;
}