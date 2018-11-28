#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

string arrange(string a, int i)
{
	string newString = a.substr(i+1) + a. substr(0,i+1);
	return newString;
}

long check(long A, long B){
	int count = 0;
	vector<string> input;
	vector<string>::iterator p;
	set<string> result;
	vector<string> total;

	for (unsigned long long j=A; j<=B; j++) 
			input.push_back(to_string(j));

			for (int i=0; i<=B-A; i++){
			for (int k=0; k<input[i].length()-1; k++){
				result.insert(arrange(input[i], k));
				}
				for(set<string>::iterator p = result.begin(); p != result.end(); p++){
					if ((*p > input[i]) && (*p <= input[B-A])){ ++count;}
					
				}
		result.clear();
				
		}
	return count;
}


int main()
{
	long T, A, B;
		
	ifstream in("in.txt");
	ofstream out("output.txt");
	in >> T ;
	
	for (int i=1; i<=T; i++){
		in >> A >> B;

		out<< "Case #" << i << ": " << check(A, B) << endl;
		
				
	}
	out.close();
	in.close();
	return 0;
}
