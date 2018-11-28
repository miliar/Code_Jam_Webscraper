#include <fstream>
#include <string>
#include <vector>
using namespace std;

ofstream out("a.out");
ifstream in("a.in");

int ib[500][500] = {0};
int lets[1000] = {0};
char cline[501];

vector<int> b[500];
int total = 0;

void recursion(int index, string str){
	str.push_back(cline[index]);
	string strnew = str;
	if (b[index].size() == 0) {
		if (!strcmp(strnew.c_str(), "welcome to code jam")) total++;
		return;
	}
	for (int r = 0; r < b[index].size(); r++){
		recursion(b[index][r], strnew);
		strnew = str;
	}
}

int main(){
	int N;
	in >> N;
	in.get();
	for (int q = 0; q < N; q++){
		memset(cline, 0, 501);
		memset(lets, 0, 4000);
		for (int r = 0; r < 500; r++) b[r].clear();
		in.getline(cline, 501, '\n');
		string line = cline;
		for (int r = 0; r < line.size(); r++) lets[line[r]]++;
		for (int r = 0; r < line.size(); r++){
			char search1=0, search2=0, search3=0;
			if (line[r] == 'w') search1 = 'e';
			if (line[r] == 'e') search1 = 'l', search2 = ' ';
			if (line[r] == 'l') search1 = 'c';
			if (line[r] == 'c') search1 = 'o';
			if (line[r] == 'o') search1 = 'm', search2 = ' ', search3 = 'd';
			if (line[r] == 'm') search1 = 'e';
			if (line[r] == 't') search1 = 'o';
			if (line[r] == 'd') search1 = 'e';
			if (line[r] == 'j') search1 = 'a';
			if (line[r] == 'a') search1 = 'm';
			if (line[r] == ' ') search1 = 't', search2 = 'c', search3 = 'j';
			for (int p = r; p < line.size(); p++){
				if (cline[p] == search1) b[r].push_back(p);
				if (cline[p] == search2) b[r].push_back(p);
				if (cline[p] == search3) b[r].push_back(p);
			}
		}
		total = 0;
		for (int r = 0; r < line.size(); r++){
			string str;
			recursion(r, str);
		}
		total %= 10000;
		int zeros = 0;
		if (total < 1000) zeros = 1;
		if (total < 100) zeros = 2;
		if (total < 10) zeros = 3;
		out << "Case #" << q+1 << ": ";
		while (zeros > 0) out << '0', zeros--;
		out << total << endl;
	}
	return 0;
}