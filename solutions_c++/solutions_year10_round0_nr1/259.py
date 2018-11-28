#include<iostream>

using namespace std;


int main(){
	int csn, a, b;

	cin >> csn;
	for(int cs = 1; cs <= csn && (cin >> a >> b); ++cs)
		cout << "Case #" << cs << ": " << ((b & ((1 << a) - 1)) == ((1 << a) - 1)?"ON":"OFF") << endl;

	return 0;
}
