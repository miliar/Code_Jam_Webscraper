#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

//#include "stdafx.h"
//#include <iostream.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


using namespace std;

vector<long long> all;
bool used[100];

void get_all(char* str, int l, int pos, bool* used, char* num)
{
	if (pos==l) 
	{
		all.push_back(atoi(num));
		return;
	}

	for (int i=0; i<l; i++) {
		if (!used[i]) {
			num[pos] = str[i];
			used[i] = true;
			get_all(str, l, pos+1, used, num);
			used[i] = false;
		}
	}

}

int main()

{

	int T;
	long long N[500];

	string fn;
	fn = "B-small-attempt1.in";
	ifstream infile;
	infile.open (fn.c_str(), ifstream::in);
	infile>>T;
	
	for (int i=0; i<T; i++) {		
		infile>>N[i];
	}
	infile.close();


	ofstream outfile;
	outfile.open (fn.append(".out").c_str(), ifstream::out);

	for (int i=0; i<T; i++) {
		all.clear();
		outfile<<"Case #"<<i+1<<": ";

		vector<long long>::iterator it = all.end();
		long long data = N[i];
		
		while (true) {
			char str[100];
			itoa(data, str, 10);
			vector<int> flg(10, 0);
			for (int j=0; j<strlen(str); j++)
				flg[str[j]-'0']++;

			for (int j=0; j<strlen(str); j++)
				used[j]=false;

			char newnum[100];
			for (int j=0; j<100; j++)
				newnum[j]='\0';
			get_all(str, strlen(str), 0, used, newnum);

			sort(all.begin(), all.end());
			it = unique(all.begin(), all.end());
			all.resize(it - all.begin());
			it = find(all.begin(), all.end(), N[i]);
			if (all.end()-it == 1) data *= 10;
			else break;
		}



		outfile<<*(it+1)<<endl;

			
		


	}

	outfile.close();

	return 0;
}