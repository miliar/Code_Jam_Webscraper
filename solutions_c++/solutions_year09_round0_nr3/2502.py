#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;
void findnext(int char_num, int p, int & count, string & word);
static char welcome[] = "welcome to code jam";
ofstream fout("C-small.out");

int main()
{
	ifstream fin("C-small.in");

	int N;
	fin >> N;
	char* tp = new char[500];
	fin.getline(tp, 500);

	for (int i=0; i<N; i++)
	{
		int count = 0;
		string word;
		char* c = new char[500];
		fin.getline(c, 500);
		word = c;
		//fout << word << "\n";
		findnext(0, 0, count, word);
		fout << "Case #" << i+1 << ": " << setfill ('0') << setw(4) << count << "\n";
	}

	return 0;
}

void findnext(int char_num, int p, int & count, string & word)
{
	for(p; p<word.length(); p++)
	{
		//fout << word[p] << "\n";
		if (word[p] == welcome[char_num])
		{
			if(char_num == 18){
				if (count==9999)
					count = 0;
				else
					count++;
			}
			else{
				findnext(char_num+1, p+1, count, word);
			}
		}
	}
}