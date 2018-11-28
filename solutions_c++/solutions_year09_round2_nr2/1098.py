#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
 	int n, c = 0;
 	cin >> n;
 	string st;
	getline(cin, st);
 	while (n-- && ++c) {
		  getline(cin, st);
		  char arr[st.size()+1];
		  arr[0] = '0';
		  strcpy(arr+1, st.c_str());
		  if (next_permutation(arr, arr + st.size() + 1)) {
		  	 if (arr[0] == '0')
	 			cout << "Case #" << c << ": " << (arr + 1) << endl;
 			 else
		  	 	 cout << "Case #" << c << ": " << arr << endl;
		  } else {
	  		 cout << "Case #" << c << ": " << st << endl;
 		 }
    }
}
