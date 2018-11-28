#include <string>
#include <iostream>
#include <fstream> 
using namespace std;
 
int num_haystack;
string haystack;
const int num_needle = 19;
const string needle = "welcome to code jam";
int tabular[500][19];
 
ifstream fin("C.in");
#define cin fin
FILE *file;
 
int ss(const int s_haystack, const int s_needle) {
	// If we already have the value, return it immediately
  if(tabular[s_haystack][s_needle] != -1) {
		return tabular[s_haystack][s_needle];
	}
  
	if(num_haystack - s_haystack < num_needle - s_needle) {
		tabular[s_haystack][s_needle] = 0;
		return 0;
	}
  
	if(num_haystack - s_haystack == num_needle - s_needle) {
		string sub_haystack = haystack.substr(s_haystack, num_haystack - s_haystack);
		string sub_needle = needle.substr(s_needle, num_needle - s_needle);
		tabular[s_haystack][s_needle] = (sub_haystack == sub_needle) ? 1 : 0;
		return tabular[s_haystack][s_needle];
	}
  
	int total = 0;
  
  //Advance position in haystack
	total += ss(s_haystack+1, s_needle);
  //Ensure only last 4 digits are being tracked.
	total %= 10000;
  
	// If the current characters match...
	if(haystack[s_haystack] == needle[s_needle]) {
    //move on to the next characters for both needle and haystack
		total += ss(s_haystack+1, s_needle+1);
    //Ensure only last 4 digits are being tracked.
		total %= 10000;
	}
	tabular[s_haystack][s_needle] = total;
	return total;
}
 
int main() {
	file = fopen("C.out", "w");
	int cases;
	cin >> cases;
	getline(cin, haystack);
	for (int n = 1; n <= cases; ++n) {
		getline(cin, haystack);
		memset(tabular, -1, 500 * 19);
		num_haystack = haystack.length();
		int cnt = ss(0, 0);
    //Pad with zeroes
		fprintf(file, "Case #%d: %04d\n", n, cnt);
	}
	return 0;
}
