#include <vector>
#include <list>
#include <map>
#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;


int main()
{
    int L, D, N;
    string in;
    cin >> in;
    L = atoi(in.c_str());
    cin >> in;
    D = atoi(in.c_str());
    cin >> in;
    N = atoi(in.c_str());
    string dict[D];
    for (int i = 0; i < D; ++i) {
	cin >> in;
	dict[i]=in;
    }

    for (int i = 0; i < N; ++i) {
	string word[L];
	cin >> in;
	for (int j = 0; j < L; ++j ) {
	    size_t found = in.find("(");
	    if (found == string::npos || found > 0) {
		word[j] = in[0];
		in = in.erase(0,1);
	    } else {
		word[j] = in.substr(1, in.find(")")-1);
		in = in.erase(0,in.find(")")+1);
	    }
	}

	int possible = 0;
	for (int j = 0; j < D; ++j) {
	    bool found = true;
	    for (int k = 0; k < L; ++k) {
		if (word[k].find(dict[j][k]) != string::npos)
		    continue;
		found = false;
		break;
	    }
	    if (found)
		++possible;
	}

	cout << "Case #" << i+1 << ": " << possible << endl;
    }

    return 0;
}