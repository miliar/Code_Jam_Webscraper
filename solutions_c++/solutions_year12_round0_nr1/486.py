#include <iostream>
#include <fstream>

using namespace std;
ofstream fout ("output.out");
ifstream fin ("input.in");

#define MAX_N	100

int T, cases;
char words[MAX_N+4];
char convert[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

void work() {
	int i = 0;
	while (words[i]) {
		if (words[i]>='a' && words[i]<='z')
			words[i] = convert[words[i]-'a'];
		else if (words[i]>='A' && words[i]<='Z')
			words[i] = convert[words[i]-'A'] - 'a' + 'A';
		i ++;
	}
	fout << "Case #" << cases << ": " << words << endl;
}

int main() {
	fin >> T;
	fin.getline(words, sizeof(words));
	for (cases=1; cases<=T; cases++) {
		fin.getline(words, sizeof(words));
		work();
	}
	system("pause");
	return 0;
}
