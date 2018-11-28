#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <algorithm>
#include <regex.h>
using namespace std;
/*
string intToString(int toConvert)
{
	stringstream s; s << toConvert; return s.str();
}
 */

bool isRecycled(int numA, int numB){
	bool recycled = false;
	int count = 0;
	list<int> A, B;
	
	
	while ((double)numA / 10 > 0.0) {
		A.push_front(numA % 10); numA /= 10;
		B.push_front(numB % 10); numB /= 10;
		++count;
	}
	
	for (int i=0; i<count; ++i) {
		if (A.front() == B.front()) {
			for (list<int>::iterator Aiter = A.begin(), Biter = B.begin(); 
				 Aiter != A.end() || Biter != B.end(); ++Aiter, ++Biter){
				if (*Aiter != *Biter) {
					recycled = false;
					goto NEXT;
				}
			}
			recycled = true;
			goto THE_END;
		}
		NEXT:
		// shift numbers
		B.push_front(B.back());
		B.pop_back();
	}
	THE_END:
	return recycled;
	 
}

int main (int argc, char * const argv[]) {
	
    // HANDLE COMMAND-LINE ARGUMENTS
	//freopen("example.in", "rt", stdin);
	
	freopen(argv[1], "rt", stdin);
	if(argc == 3){
		freopen(argv[2], "wt", stdout);
	}
	else if(argc==2){
		string out = argv[1];
		out = out.substr(0, out.size() - 2);
		out += "out";
		cout << "Result file: " << out << endl;
		freopen(out.c_str(), "wt", stdout);
	}
	else {
		cout << "Input file required!\nUsage: ./" << argv[0] << " example.in [example.out]" << endl;
		return 0;	
	}
	
	
	int T = 0;
	cin >> T;
	
	for (int t=0; t<T; ++t) {
		int tempA, tempB;
		cin >> tempA >> tempB;
				
		int answer = 0;
		
		for (int i=tempA; i<=tempB; ++i) {
			for (int j=i+1; j<=tempB; ++j) {
				if (isRecycled(i, j)) {
					++answer;
				}
			}
		}
		cout << "Case #" << t+1 << ": " << answer << endl;
	}	
	return 0;
}

























