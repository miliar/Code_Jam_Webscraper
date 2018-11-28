#include <fstream>
#include <map>
#include <iomanip>
#include <vector>
#include <string>

int main(){
	using namespace std;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int t;
	fin >> t;
	string s;
	char ch;
	vector<string> A(t);
	int i = -1;
	while(fin >> noskipws >> ch){
		if(ch == '\n'){
			i++;
		} else {
			A[i] += ch;
		}
	}
	map<char, char> tr;
	string s1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
	string s2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
	for(int i = 0; i < s1.size(); i++){
		tr[s1[i]] = s2[i];
	}
	for(int i = 0; i < t; i++){
		for(int j = 0; j < A[i].size(); j++){
			A[i][j] = tr[A[i][j]];
		}
	}
	for(int i = 0; i < t; i++){
		fout << "Case #" << i + 1 << ": ";
		for(int j = 0; j < A[i].size(); j++){
			fout << A[i][j];
		}
		fout << endl;
	}
	return 0;
}