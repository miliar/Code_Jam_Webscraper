 #define FILENAME "A-small-attempt6.in"

 #include <fstream>
 #include <iostream>
 #include <vector>
 #include <string>
 #include <sstream>
 #include <iterator>
 #include <algorithm>
 #include <cmath>
 #include <set>

 using namespace std;
 
 int SolveA(string str);
 int power(int x, int y) {
	 int result = 1;
		while(y--)
			result*=x;
	 return result;
 }
int main()
{
	int T;
	string str;
	fstream input(FILENAME,ios::in);
	input >> T;
	for(int i=0; i<T; i++) {
		input >> str;
		cout << "Case #" << i+1 << ": " << SolveA(str) << endl;
	}
	return 0;
}

int SolveA(string str) {
	set<char> symbols;
	int len = str.length();
	char arr[62];
	int index = 0;
	for(int i=0; i<len; i++) {
		if(symbols.count(str[i]) == 0) {
			symbols.insert(str[i]);
			arr[index++] = str[i];
		}
	}
	int size = symbols.size();
	int base = (size == 1) ? 2 : size;
	long int result = 0;
	int mem[10] = {1,0,2,3,4,5,6,7,8,9};
	for(int i=0; i<len; i++) {
		char ch = str[i];
		int pos = -1; 
		for(int j=0; j<len; j++) {
		   if(arr[j]==ch) pos = j;
		   if(pos != -1) break;
		}		
		int digit = mem[pos];
		result+= digit*power(base,len-i-1);
	}
		return result;
}
