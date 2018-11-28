#include<iostream>
#include<fstream>

using namespace std;

int visit(string& s, int startpos, string& welcome, int next_letter){
//	cout << "visit";
	if(next_letter == welcome.length())
		return 1;
	if(startpos == s.length())
		return 0;
	size_t next_pos = s.find(welcome[next_letter], startpos);
//	cout << "kommer hertil";
	if(next_pos == string::npos)
		return 0;
	return visit(s, next_pos+1, welcome, next_letter+1) + visit(s, next_pos+1, welcome, next_letter);
}



int main(int argc, char argv[]){

	ifstream input("input.txt");
	ofstream output("output.txt");
	int N;
	input >> N;
	string line;
	getline(input, line);
	string welcome = "welcome to code jam";
	for(int i=0;i<N; i++){
		getline(input, line);
		cout << line << "\n";
		int result= visit(line, 0, welcome, 0);
		output << "Case #" << i+1 << ": ";
		if(result < 1000)
			output << "0";
		if(result < 100)
			output << "0";
		if(result < 10)
			output << "0";
		output << result % 10000 << "\n";
	}
}
		
