#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>

using namespace std;

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	//ifstream input("C-small.in");

	int numOfCase;
	cin >> numOfCase;
	
	char temp[10];
	cin.getline(temp, 10);

	string *datas = new string[numOfCase];
	for(int i = 0; i < numOfCase; i++) {
		char temp[501];
		cin.getline(temp, 501);
		
		datas[i] = temp;
		datas[i].insert(datas[i].begin(), ' ');
		//cout << datas[i] << endl;
	}

//	input.close();

	

	string givenString = " welcome to code jam";

	for(int i = 0; i < numOfCase; i++) {
		int **solve;
		solve = new int*[givenString.length()];
		for(int j = 0; j < givenString.length(); j++) {
			solve[j] = new int[datas[i].length()];
			for(int k = 0; k < datas[i].length(); k++) 
				if(j == 0) solve[j][k] = 1;
				else solve[j][k] = 0;
		}

		for(int j = 1; j < givenString.length(); j++) {
			for(int k = 1; k < datas[i].length(); k++) {
				if(givenString[j] == datas[i][k]) solve[j][k] = solve[j - 1][k - 1] + solve[j][k - 1];
				else solve[j][k] = solve[j][k - 1];
			}
		}

		
		cout << "Case #" << i + 1 << ": " << setw(4) << setfill('0') << solve[givenString.length() - 1][datas[i].length() - 1] << endl;


		for(int j = 0; j < givenString.length(); j++) {
			delete [] solve[j];
		}
		delete [] solve;
	}

	

	delete [] datas;

	return 0;
}
