#include<string>
#include<fstream>
#include<iostream>

using namespace std;

string s[100];

int main(){

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	int ntc,r,c;

	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> r >> c;
		for (int i=0;i<r;i++)
			cin >> s[i];
		for (int i=0;i<r-1;i++){
			for (int j=0;j<c-1;j++){
				if (s[i][j]=='#' && s[i+1][j]=='#' && s[i][j+1]=='#' && s[i+1][j+1]=='#')
					s[i][j]='/',s[i+1][j]='\\',s[i][j+1]='\\',s[i+1][j+1]='/';
			}
		}
		bool find = false;
		for (int i=0;i<r && !find;i++){
			for (int j=0;j<c;j++){
				if (s[i][j]=='#'){
					find = true;
					break;
				}

			}
		}
		cout << "Case #" << tc << ":" << endl;		
		if (find)
			cout << "Impossible" << endl;
		else{
			for (int i=0;i<r;i++)
				cout << s[i] << endl;
		}
	}

	return 0;
}