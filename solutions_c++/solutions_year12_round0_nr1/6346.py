#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<cmath>
#include<vector>

using namespace std;

int main() {
	ifstream fin("ainput.txt");
	int n;
	string str;
	fin >> n;
	vector<string> a, b;
	getline(fin, str);
	for (int i=0; i<n; i++) {
		getline(fin, str);
		a.push_back( str );
		cout << i << " " << str << endl;
	}

	for (int i=0; i<n; i++) {
		getline(fin, str);
		b.push_back( str );
		cout << i << " " << str << endl;
	}
	
	int mat[30];
	for (int i=0; i<26; i++) {
		mat[i] = -1;
	}

	for (int i=0; i<n; i++) {
		for (int j=0; j<a[i].size(); j++) {
			mat[ a[i][j]-'a' ] = b[i][j] - 'a';
		}
	}
	
	//mat[ 'o' - 'a' ] = 'e' - 'a';
	mat[ 'q' - 'a' ] = 'z' - 'a';
	mat[ 'z' - 'a' ] = 'q' - 'a';
	
	for (int j=0; j<a[0].size(); j++) {
		if ( a[0][j] == ' ' ) cout << " ";
		else cout << (char) (mat[ a[0][j] - 'a' ] + 'a');
	}
	cout << endl;
	
	for (int i=0; i<26; i++) {
		cout << (char) (i + 'a');
	}
	
	cout << endl;
	
	int g = 0;
	
	for (int i=0; i<26; i++) {
		if (mat[i] == -1) cout << " ";
		else cout << (char) (mat[i] + 'a');
	}
	
	ofstream fout("aoutput.txt");
	fin >> n;
	getline(fin, str);
	for (int i=0; i<n; i++) {
		getline(fin, str);
		fout << "Case #" << i+1 << ": ";
		for (int j=0; j<str.size(); j++) {
			if ( str[j] == ' ' ) fout << " ";
			else fout << (char) (mat[ str[j] - 'a' ] + 'a');
		}
		fout << endl;
		//fout << i << " " << str << endl;
	}
	
	fout.close();
	fin.close();
	return 0;
}
