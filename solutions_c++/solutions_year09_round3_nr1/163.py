/**********************
 * jhurwitz           *
 * Round 1C           *
 * "All Your Base"    *
 **********************/

#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

void base(int casenum)
{
	char line[100];
	fin >> line;
	long long chartonum[256];
	for (int i=0; i<256; i++)
		chartonum[i] = -1;
	long long base = 0;
	for (char* c = line; *c; c++)
		if (chartonum[*c] == -1) 
			chartonum[*c] = base++;
	//now we need to switch the 0 and 1
	for (int i=0; i<256; i++)
		if (chartonum[i]==0 || chartonum[i]==1)
			chartonum[i] = 1-chartonum[i];
	if (base==1) base++; //because the 0s are now 1s
	long long seconds = 0;
	for (char* c = line; *c; c++)
		seconds = base*seconds+chartonum[*c];
	fout << "Case #" << casenum << ": " << seconds << endl;
}

int main()
{
	int T;
	fin >> T;
	for (int i=0; i<T; i++)
		base(i+1);
}

